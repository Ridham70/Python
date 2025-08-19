import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

before = sys.argv[1]
after = sys.argv[2]
extension = (".jpeg", ".jpg", ".png")

if not before.lower().endswith(extension) or not after.lower().endswith(extension):
    sys.exit("Invalid input or output")

e_before = before.split(".")
e_after = after.split(".")

if not e_before[-1] == e_after[-1]:
    sys.exit("Input and output have different extensions")

try :
    user_image = Image.open(before, "r")

except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")
size = shirt.size
user_image = ImageOps.fit(user_image, size)
user_image.paste(shirt, shirt)
user_image.save(after)
