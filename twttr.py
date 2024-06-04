i = input("Input: ")
print("Output: ", end = "")
for l in i:
    if l in ["a", "e", "i", "o", "u"]:
        print("", end = "")
    else:
        print(l, end = "")