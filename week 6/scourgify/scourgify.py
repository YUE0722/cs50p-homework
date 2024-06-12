import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                first_name, last_name = row["name"].split(", ")
                house = row["house"]
                with open(sys.argv[2], "a") as file:
                    writer = csv.DictWriter(file, fieldnames=["FirstName", "LastName", "House"])
                    writer.writerow({"FirstName": first_name, "LastName": last_name, "House": house})

    except FileNotFoundError:
        sys.exit("File not found")
else:
    sys.exit("Not a CSV file")
