import requests

def fetch_stocks():
    url = "https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data and "data" in data["data"]:
        stock_data = data["data"]["data"]
        for stock in stock_data:
            symbol = stock["symbol"]
            name = stock["name"]
            return name , symbol
        
    else:
        raise Exception("unable to fetch the data of the stocks")   



def main():
    try:
        name, symbol = fetch_stocks()
        print(f"the details if the stock \n name : {name} \n symbol: {symbol}")
    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    main()
