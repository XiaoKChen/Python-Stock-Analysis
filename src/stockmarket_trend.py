import os
import csv
import threading
import requests
import time
from dotenv import load_dotenv
load_dotenv()

def get_stock_price():
    url = f"https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    print(f'{time.ctime(time.time())} : {price}')
    return (time.ctime(time.time()), price)

def output_to_csv(input_time, input_price):
    writer.writerow({input_time, input_price})

ticker    = 'AAPL'
api_key   = os.environ['APIKEY']
starttime = time.time()
csv_file  = open(f'../csv_data/{time.ctime(starttime)}.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow({'Time', 'Price'})

while True:
    input_time, input_price = get_stock_price()
    output_to_csv(input_time, input_price)
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))