import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    pattern = r"^([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$"
    if time := re.search(pattern, s):
        time_part = list(time.groups())
        if time_part[1] is None:
            time_part[1] = "00"
        if time_part[4] is None:
            time_part[4] = "00"
        lhs_time = convert_hour(time_part[0], time_part[1], time_part[2])
        rhs_time = convert_hour(time_part[3], time_part[4], time_part[5])
        return f"{lhs_time} to {rhs_time}"
    else :
        raise ValueError

def convert_hour(hh, mm, xx):
    hour = int(hh)
    minute = int(mm)
    if xx == "PM":
        if hour != 12:
            hour += 12
    else:
        if hour == 12:
            hour = 0
    return f"{hour:02d}:{minute:02d}"




if __name__ == "__main__":
    main()
