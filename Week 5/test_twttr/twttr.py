def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")

def shorten(word):
    output = []
    for letter in word:
        if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            continue
        else:
            output.append(letter)
    return "".join(output)

if __name__ == "__main__":
    main()
