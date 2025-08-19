import sys

if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
    try:
        with open(sys.argv[1]) as f :
            count = 0
            for line in f :
                if not line.lstrip().startswith("#") and line.lstrip() != "" :
                    count += 1
            print(count)

    except FileNotFoundError :
        sys.exit("File does not exist")

elif len(sys.argv) < 2 :
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2 :
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

