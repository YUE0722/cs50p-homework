math = input("Expression: "). strip()

x, y, z = math.split(" ")
x = float(x)
z = float(z)

if y == "+":
    print(f"{(x + z):.1f}")
elif y == "-":
    print(f"{(x - z):.1f}")
elif y == "*":
    print(f"{(x * z):.1f}")
elif y == "/":
    print(f"{(x / z):.1f}")
# remember how to use format string
