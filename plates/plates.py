def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the length is between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # Check if the first two characters are alphabetic
    if not s[0:2].isalpha():
        return False

    # Check for numbers and special characters
    has_number = False
    for i, c in enumerate(s):
        if c.isdigit():
            has_number = True
            # Check if the first number is '0'
            if c == '0' and i == 2:
                return False
            # Ensure numbers appear consecutively at the end
            if i < len(s) - 1 and not s[i + 1].isdigit():
                return False
        elif not c.isalpha():
            return False

    return True


main()
