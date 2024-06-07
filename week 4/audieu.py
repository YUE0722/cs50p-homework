import inflect
p = inflect.engine()

name = []
while True:
    try:
        name.append(input("Name: "))
# cannot use name = name.append(input("Name: "))
    except EOFError:
        print()
        break

print(f"adieu, audieu to {p.join(name)}")