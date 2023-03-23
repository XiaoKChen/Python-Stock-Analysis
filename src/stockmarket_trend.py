import csv
import time
import requests

def get_stock_price(ticker, api_key):
    url = f"https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    print(f'{time.ctime(time.time())} : {price}')
    return (time.ctime(time.time()), price)

def output_to_csv(input_time, input_price):
    writer.writerow({'Time':input_time, 'Price':input_price})
    
def create_csv():
    global writer
    csv_file  = open(f'../csv_data/{time.ctime(starttime)}.csv', 'w')
    fieldname = ['Time', 'Price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()

starttime = time.time()