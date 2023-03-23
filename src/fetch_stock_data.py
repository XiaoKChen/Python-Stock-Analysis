import json
import requests

def get_stock_data(ticker, start_date, end_date, interval, api_key):
    url = f"https://api.twelvedata.com/time_series?&symbol={ticker}&timezone=Pacific/Honolulu&start_date={start_date}&end_date={end_date}&interval={interval}&apikey={api_key}"
    print(url)
    response = requests.get(url).json()
    
    jsonfile = open('../json_data/Data.json', 'w')
    json.dump(response, jsonfile)