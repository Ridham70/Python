def main():
    a = input("Greeting: ").strip()
    amt = value(a)
    print(f"${amt}")


def value(greeting):
    greeting = greeting.lower()
    if "hello" in greeting :
        return 0
    elif greeting[0] == "h" :
        return 20
    else :
        return 100




if __name__ == "__main__":
    main()
