from tabulate import tabulate
import csv
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

menu = []
if sys.argv[1] == "sicilian.csv" or sys.argv[1] == "regular.csv":
    try:
        with open("sicilian.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
        print(tabulate(menu, headers = "firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found")
