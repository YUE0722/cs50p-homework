def main():
    gauge(convert(input("Fraction: ")))

def convert(fraction):
    while True:
        try:
            i, j = map(int, faction.split("/"))
            return round(i / j * 100)
            if j == 0:
                raise ZeroDivisionError
            elif i > j:
                raise ValueError
        except (ZeroDivisionError, ValueError):
            pass

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
