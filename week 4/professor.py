import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        number_one = generate_integer(level)
        number_two = generate_integer(level)
        correct_answer = number_one + number_two
        for attempt in range(3):
            try:
                user_input = int(input(f"{number_one} + {number_two} = "))
                if user_input == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            if attempt == 2:
                        print(f"{number_one} + {number_two} = {correct_answer}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = input("Level: ")
            if level in ["1", "2", "3"]:
                return int(level)
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
