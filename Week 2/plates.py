def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Alphanumeric
    if not s.isalnum():
        return False
    # At least two letters
    i = s[0:2]
    if not i.isalpha():
        return False
    # Max 6 letters, min 2 letters
    j = len(s)
    if not 2 <= j <= 6:
        return False
    # Numbers cannot be used in the middle of a plate
    k = len(s) - 1
    if s[k].isalpha():
        if not s.isalpha():
            return False
    # Return True if all conditions followed
    return True

main()
