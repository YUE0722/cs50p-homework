while True:
    try:
        i, j = map(int, input("Fraction: ").split("/"))
        if j == 0:
            raise ZeroDivisionError
        elif i > j:
            raise ValueError
    except (ZeroDivisionError, ValueError):
        continue
    else:
        break

percentage = i / j * 100
if percentage >= 99:
    print("F")
elif percentage <= 1:
    print("E")
else:
    print(f"{percentage}%")
