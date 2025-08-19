def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_replaced = d.replace("$", "")
    return float(d_replaced)


def percent_to_float(p):
    p_replaced = p.replace("%", "")
    p_converted = float(p_replaced)/100
    return p_converted



main()
