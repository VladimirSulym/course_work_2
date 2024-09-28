import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_data_request_curr_stock(currency: str) -> float:
    """Функция запрашивает указанный курс валют к рублю по внешнему API"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "to": "RUB",
        "from": currency,
        "amount": "1",
    }
    headers = {"apikey": os.getenv("API_KEY")}
    response = requests.get(url, headers=headers, params=payload)
    result = response.json()
    return round(result["result"], 2)


def get_data_request_curr_trade(stock: str) -> float:
    """Функция запрашивает стоимость указанных акций по внешнему API"""
    url = f"https://api.marketstack.com/v1/eod?access_key={os.getenv("API_KEY_MARKETSTACK")}"
    payload = {"symbols": stock}
    response = requests.get(url, params=payload)
    result = response.json()
    print(result)
    return round(result["data"][0]["close"], 2)


# if __name__ == "__main__":
#     print(get_data_request_curr_stock("EUR"))
#     print(get_data_request_curr_trade("AAPL"))
