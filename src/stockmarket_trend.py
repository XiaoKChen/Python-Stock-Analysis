import os
import requests
import time
from dotenv import load_dotenv
load_dotenv()

ticker = "AAPL"
api_key = os.environ['APIKEY']

def get_stock_price(import_ticker, import_api_key):
    url = f"https://api.twelvedata.com/price?symbol={import_ticker}&apikey={import_api_key}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    return price

stock_price = get_stock_price(ticker, api_key)

print(f'{time.time}:{stock_price}')