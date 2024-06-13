import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    s = s.strip()
    match = re.fullmatch(r"(\d{1,2}):?(\d{1,2})? (AM|PM) to (\d{1,2}):?(\d{1,2})? (AM|PM)", s)
    if not match:
        raise ValueError

    st_hour, st_min, st_ap, end_hour, end_min, end_ap = match.groups()

    if st_min == None:
        st_min = 0
    if end_min == None:
        end_min = 0

    st_hour, st_min, end_hour, end_min = map(int, [st_hour, st_min, end_hour, end_min])

    if st_hour > 12 or end_hour > 12:
        raise ValueError
    if st_min > 59 or end_min > 59:
        raise ValueError

    if st_ap == "PM":
        st_hour += 12

    if end_ap == "PM":
        end_hour += 12

    return f"{st_hour:02d}:{st_min:02d} to {end_hour:02d}:{end_min:02d}"

if __name__ == "__main__":
    main()
