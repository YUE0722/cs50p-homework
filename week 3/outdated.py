month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        x, y, z = map(int, date.split("/"))
        break
        if x > 12 or x < 1:
            raise
        if y > 31:
            raise
    except ValueError:
        x, y, z = date.replace(", ", " ").split(" ")
        x = month.index(x) + 1
        y = int(y)
        z = int(z)
        break
    except RuntimeError:
        pass

print(f"{z}-{x:02d}-{y:02d}")