import json

def popluate_data():
    global DataList, TempList
    with open(f'../json_data/Data.json') as file:
        data = json.load(file)

    DataList = data['values']
    TempList = []

def get_data_slope():
    filterDataList = []
    
    for High in DataList:
        TempList.append(float(High["high"]))
    
    Temp = sorted(TempList)[-1]
    
    for a in DataList:
        if (float(a["high"]) == Temp):
            highestPeak_index = DataList.index(a)
            highestPeak = DataList[DataList.index(a)]["high"]
            highestTime = DataList[DataList.index(a)]["datetime"]
            break
            
    print(f'[{highestPeak_index}]{highestTime} : {highestPeak}')
    
    for a in DataList:
        if (DataList.index(a) >= highestPeak_index):
            filterDataList.append(a)
            
    print(filterDataList)
    print()
    print()
    print(DataList)