import random

# Get valid level input
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

# Generate the target number once
x = random.randint(1, n)

# Guessing loop
while True:
    try:
        g = int(input("Guess: "))
        if g < x:
            print("Too small!")
        elif g > x:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass  # Reject non-numeric input and prompt again
