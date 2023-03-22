import os
import threading
import requests
import time
from dotenv import load_dotenv
load_dotenv()

ticker = "AAPL"
api_key = os.environ['APIKEY']

def get_stock_price():
    url = f"https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    print(f'{time.ctime(time.time())} : {price}')

starttime = time.time()
while True:
    get_stock_price()
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))