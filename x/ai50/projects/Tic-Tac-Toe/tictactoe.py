"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Raises ValueError if the action is illegal.
    """
    i, j = action

    # Validate bounds
    if not (0 <= i <= 2 and 0 <= j <= 2):
        raise ValueError("Action coordinates out of bounds")

    # Validate the cell is empty
    if board[i][j] is not EMPTY:
        raise ValueError("Cell is already taken")

    # Determine whose turn it is
    current_player = player(board)

    # Deep-copy the board
    new_board = [row[:] for row in board]

    # Apply the move
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Returns X if X has three in a row, O if O has three in a row,
    otherwise None.
    """
    # Rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if the game is over, False otherwise.
    A game is over if someone has won or if every cell is occupied.
    """
    # Game already won
    if winner(board) is not None:
        return True

    # Any empty cell left
    for row in board:
        if EMPTY in row:
            return False

    # All cells filled
    return True


def utility(board):
    """
    Returns 1 if X has won, -1 if O has won, 0 otherwise.
    Assumes the board is terminal.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Returns None if the board is terminal.
    """
    if terminal(board):
        return None

    # alpha-beta pruning
    def max_value(b, alpha, beta):
        if terminal(b):
            return utility(b), None
        v = -math.inf
        best_action = None
        for action in actions(b):
            min_v, _ = min_value(result(b, action), alpha, beta)
            if min_v > v:
                v, best_action = min_v, action
            alpha = max(alpha, v)
            if alpha >= beta:
                break
        return v, best_action

    def min_value(b, alpha, beta):
        if terminal(b):
            return utility(b), None
        v = math.inf
        best_action = None
        for action in actions(b):
            max_v, _ = max_value(result(b, action), alpha, beta)
            if max_v < v:
                v, best_action = max_v, action
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v, best_action

    current_player = player(board)
    if current_player == X:
        _, move = max_value(board, -math.inf, math.inf)
    else:
        _, move = min_value(board, -math.inf, math.inf)

    return move
