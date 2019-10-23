import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=18577cdff577b0376cdf7024fed7b1bd&base=EUR&symbols=USD")
    print(res.status_code)
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"]["USD"]
    print(f"1 EUR is equal to {rate} USD")

if __name__ == "__main__":
    main()
