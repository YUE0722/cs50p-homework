grocery = {}
while True:
    try:
        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        if not item in grocery:
            grocery[item] = 1
    except EOFError:
        print()
        break
grocery_sorted = sorted(grocery.items())
for item, count in grocery_sorted:
    print(f"{count}{item}")