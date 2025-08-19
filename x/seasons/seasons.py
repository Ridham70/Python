import re, sys, inflect

from datetime import date


def main():
    try:
        print(min_to_word(date_to_min(get_date())))
    except ValueError:
        sys.exit("Invalid date")

def get_date():
    if match := re.match(r"^(\d{4})-(\d{2})-(\d{2})$", input("Date of Birth: ")):
        return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    else:
       return sys.exit("Invalid date")

def date_to_min(dob):
    d_born = dob
    d_today = date.today()
    if d_born < d_today :
        difference = d_today - d_born
        minutes = difference.days * 24 * 60
        return minutes
    else :
        return sys.exit("Date cannot be in the future")

def min_to_word(min):
    p = inflect.engine()
    words = p.number_to_words(min, andword="")
    return f"{words.capitalize()} minutes"



if __name__ == "__main__":
    main()
