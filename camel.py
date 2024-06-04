c = input("camelCame: ")
print("snake_case: ")
for s in c:
    if s.islower():
        print(s, end="")
    else:
        print(f"_{s.lower()}", end = "")