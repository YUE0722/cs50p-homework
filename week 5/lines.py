import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

number_of_lines = 0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line == "":
                continue
            if line.startswith("#"):
                continue
            else:
                number_of_lines += 1

except FileNotFoundError:
    if sys.argv[1].endswith(".py"):
        sys.exit("File does not exit")
    else:
        sys.exit("Not a python file")
