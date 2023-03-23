import json

def popluate_data():
    global DataList, HighList
    with open(f'../json_data/Data.json') as file:
        data = json.load(file)

    DataList = data['values']
    HighList = []

def get_data_slope():
    for High in DataList:
        HighList.append(float(High["high"]))
        
    firHigh, secHigh = sorted(HighList)[-1], sorted(HighList)[-2]
    firTime, secTime = '', ''

    for High in DataList:
        if float(High['high']) == firHigh:
            firTime = High['datetime']
            break
            
    for High in DataList:   
        if float(High['high']) == secHigh:
            secTime = High['datetime']
            break
        
    print(f'{firTime} : {firHigh}')
    print(f'{secTime} : {secHigh}')