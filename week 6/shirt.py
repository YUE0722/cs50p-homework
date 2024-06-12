import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

type = (".jpg", ".png", ".jpeg")
if sys.argv[1].endswith(type) and sys.argv[2].endswith(type):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as image:
            size = shirt.size
            ImageOps.fit(image, size)
            Image.paste(shirt, shirt)
            Image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("File not found")

else:
    sys.exit("Wrong file type")
