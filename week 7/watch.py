import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.match(r"<iframe.*?src=\"https?://(?:www\.)?youtube\.com/embed/([^ ]*)\".*", s):
        web = "https://youtu.be/" + match.group(1)
        return web
    else:
        return None

if __name__ == "__main__":
    main()
