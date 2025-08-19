def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue  # Retry the loop on error
        # Now pass the percentage to the gauge function
        result = gauge(percentage)
        print(result)
        break  # Exit the loop if successful

def convert(fraction):
    while True:
        try:
            n, d = fraction.split("/")
            numerator = int(n)
            denominator = int(d)
            if denominator == 0:
                raise ZeroDivisionError("Denominator cannot be zero.")
            if numerator > denominator:
                raise ValueError("Numerator cannot be greater than denominator.")
            percentage = round((numerator / denominator) * 100)
            return percentage
        except (ValueError, ZeroDivisionError) as e:
            raise e

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
