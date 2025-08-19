x, y, z = input("Expression: ").strip().split(" ")
if y == "+" :
    print(float(x) + float(z))
elif y == "-" :
    print(float(x) - float(z))
elif y == "*" :
    print(float(x) * float(z))
elif y == "/" :
    print(float(x) / float(z))
else :
    print("Enter valid expression!")

