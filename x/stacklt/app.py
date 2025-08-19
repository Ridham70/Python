from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from forms import LoginForm, RegistrationForm, QuestionForm, AnswerForm
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import models after db initialization
from models import User, Question, Answer, Tag, Vote

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    questions = Question.query.order_by(Question.created_at.desc()).all()
    return render_template('questions/list.html', questions=questions)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        flash('Invalid email or password', 'danger')
    return render_template('auth/login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/ask', methods=['GET', 'POST'])
@login_required
def ask():
    form = QuestionForm()
    if form.validate_on_submit():
        question = Question(
            title=form.title.data,
            body=form.body.data,
            user_id=current_user.id
        )
        db.session.add(question)

        # Handle tags
        tag_names = [t.strip() for t in form.tags.data.split(',') if t.strip()]
        for name in tag_names:
            tag = Tag.query.filter_by(name=name).first()
            if not tag:
                tag = Tag(name=name)
                db.session.add(tag)
            question.tags.append(tag)

        db.session.commit()
        flash('Your question has been posted!', 'success')
        return redirect(url_for('question_detail', question_id=question.id))
    return render_template('questions/ask.html', form=form)

@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question_detail(question_id):
    question = Question.query.get_or_404(question_id)
    form = AnswerForm()

    if form.validate_on_submit() and current_user.is_authenticated:
        answer = Answer(
            body=form.body.data,
            user_id=current_user.id,
            question_id=question.id
        )
        db.session.add(answer)
        db.session.commit()
        flash('Your answer has been posted!', 'success')
        return redirect(url_for('question_detail', question_id=question.id))

    answers = Answer.query.filter_by(question_id=question.id).order_by(Answer.created_at.desc()).all()
    return render_template('questions/detail.html', question=question, answers=answers, form=form)

@app.route('/vote/<string:model>/<int:obj_id>/<string:action>', methods=['POST'])
@login_required
def vote(model, obj_id, action):
    if model == 'answer':
        obj = Answer.query.get_or_404(obj_id)
    elif model == 'question':
        obj = Question.query.get_or_404(obj_id)
    else:
        flash('Invalid vote target', 'danger')
        return redirect(url_for('index'))

    # Check if user already voted
    existing_vote = Vote.query.filter_by(
        user_id=current_user.id,
        answer_id=obj_id if model == 'answer' else None,
        question_id=obj_id if model == 'question' else None
    ).first()

    if existing_vote:
        if existing_vote.vote_type == action:
            # User is clicking the same vote button again - remove the vote
            db.session.delete(existing_vote)
            if action == 'up':
                obj.votes -= 1
            else:
                obj.votes += 1
        else:
            # User is changing their vote
            if action == 'up':
                obj.votes += 2  # Remove downvote (-1) and add upvote (+1) = net +2
            else:
                obj.votes -= 2  # Remove upvote (+1) and add downvote (-1) = net -2
            existing_vote.vote_type = action
    else:
        # New vote
        vote = Vote(
            user_id=current_user.id,
            vote_type=action,
            answer_id=obj_id if model == 'answer' else None,
            question_id=obj_id if model == 'question' else None
        )
        db.session.add(vote)
        if action == 'up':
            obj.votes += 1
        else:
            obj.votes -= 1

    db.session.commit()
    return redirect(request.referrer or url_for('index'))

@app.route('/profile/<string:username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    questions = Question.query.filter_by(user_id=user.id).order_by(Question.created_at.desc()).all()
    answers = Answer.query.filter_by(user_id=user.id).order_by(Answer.created_at.desc()).all()
    return render_template('users/profile.html', user=user, questions=questions, answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
