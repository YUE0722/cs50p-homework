import random
import sys

while True:
    try:
        level = int(input("Level: "))
        number = random.randint(1, level)
        if level <= 0:
            raise ValueError
        break
    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()
    except ValueError:
        pass
