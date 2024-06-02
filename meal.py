def main():
    time = input("What time is it? ").strip().split(":")
# define time before using convert(time)
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    if 12 <= convert(time) <= 13:
        print("lunch time")
    if 18 <= convert(time) <= 19:
        print("dinner time")

def convert(time):
    x, y = time
    x = float(x)
    y = float(float(y)/60)
    return float(x + y)
# return means return float(x +  y) to convert(time)

if __name__ == "__main__":
    main()