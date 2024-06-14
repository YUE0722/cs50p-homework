from datetime import date
from datetime import timedelta
import inflect
import re
import sys


p = inflect.engine()


def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid format")
    minutes = find_difference(birth_date, date.today())
    print(p.number_to_words(minutes, andword=""), p.plural("minute", minutes))


def find_difference(start_day, end_day):
    difference = end_day - start_day
    return difference.days * 24 * 60


if __name__ == "__main__":
    main()
