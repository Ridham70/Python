d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
amount = 0
while 1:
    try:
        i = input("Item: ").title()
        if i in d:
            amount += d[i]
            print(f"Total: ${amount:.2f}")
    except EOFError:
        print()
        break

