import inflect
p = inflect.engine()


x = []
while 1 :
    try :
        name = input("Name: ")
        x.append(name)

    except EOFError :
        print()
        break
print(f"Adieu, adieu, to {p.join(x)}")

