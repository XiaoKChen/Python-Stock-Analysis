import csv
import json
import requests

def get_stock_data(ticker, start_date, end_date, interval, api_key):
    url = f"https://api.twelvedata.com/time_series?&symbol={ticker}&timezone=Pacific/Honolulu&start_date={start_date}&end_date={end_date}&interval={interval}&apikey={api_key}"
    print(url)
    response = requests.get(url).json()
    
    jsonfile = open('../json_data/Data.json', 'w')
    json.dump(response, jsonfile)
    
def json_to_csv():
    with open(f'../json_data/Data.json') as file:
        data = json.load(file)

    DataList = data['values']
    
    data_file = open('../csv_data/Data.csv', 'w')
 
    csv_writer = csv.writer(data_file)
 
    # Counter variable used for writing
    # headers to the CSV file
    count = 0
 
    for item in DataList:
        if count == 0:
 
            # Writing headers of CSV file
            header = item.keys()
            csv_writer.writerow(header)
            count += 1
 
    # Writing data of CSV file
        csv_writer.writerow(item.values())
 
    data_file.close()