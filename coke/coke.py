ad = 50
while ad > 0:
    print(f"Amount Due: {ad}")
    coin = int(input("Enter coin: "))
    if coin in [25, 10, 5]:
        ad -= coin
    else:
        print("Invalid coin. Please enter 25, 10, or 5 cents.")

change = abs(ad)
print(f"Change Owed: {change}")
