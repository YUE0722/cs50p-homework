import sys
import requests

try:
    if sys.argv != 2:
        sys.exit
    number_of_bitcoin = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json = response.json()
    rate_in_float = float(json["bpi"]["USD"]["rate_float"])
    amount = number_of_bitcoin * rate_in_float
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit
except ValueError:
    sys.exit("not a number")
