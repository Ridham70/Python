cc = list(input("camelCase: "))

print("snack_case: ", end = "")
for letter in cc :
    if letter.isupper():
        print("_" + letter.lower(), end = "")
    else :
        print(letter, end = "")
print()
