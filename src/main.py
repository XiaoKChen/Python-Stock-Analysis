import sys
sys.path.append('../config')
import time
import config
from fetch_stock_data import get_stock_data, json_to_csv
from determine_data_slope import get_data_slope, popluate_data
from stockmarket_trend import get_stock_price, output_to_csv, create_csv, starttime

if __name__ == '__main__' :
    
    try:
        mode = int(sys.argv[1])
        
        if (mode == 1):
            get_stock_data(config.ticker, config.start_date, config.end_date, config.interval, config.api_key)
            json_to_csv()
        elif (mode == 2):
            popluate_data()
            get_data_slope()
        elif (mode == 3):
            create_csv()

            while True:
                input_time, input_price = get_stock_price(config.ticker, config.api_key)
                output_to_csv(input_time, input_price)
                time.sleep(config.wait_time - ((time.time() - starttime) % config.wait_time)) 
        else:
            print(f'Please enter a value ( 1, 2, 3 )')
            print(f'1 : fetch_stock_data')
            print(f'2 : determine_data_slope')
            print(f'3 : stockmarket_trend')
            print(f'Example : python3 main.py 1')
    except:
        print(f'Please enter a value ( 1, 2, 3 )')
        print(f'1 : fetch_stock_data')
        print(f'2 : determine_data_slope')
        print(f'3 : stockmarket_trend')
        print(f'Example : python3 main.py 1')


    
    ################################################
    ### This Only Work In Python 3.10 Or Greater ###
    ################################################
    # match mode:
    #     case 1:
    #         get_stock_data(config.ticker, config.start_date, config.end_date, config.interval, config.api_key)
    #     case 2:
    #         get_data_slope()
    #     case 3:
    #         create_csv()
        
    #         while True:
    #             input_time, input_price = get_stock_price(config.ticker, config.api_key)
    #             output_to_csv(input_time, input_price)
    #             time.sleep(60.0 - ((time.time() - starttime) % 60.0)) 
    #     case _:
    #         print(f'Please enter a value ( 1, 2, 3 )')
    #         print(f'1 : fetch_stock_data')
    #         print(f'2 : determine_data_slope')
    #         print(f'3 : stockmarket_trend')
    #         print(f'Example : python3 main.py 1')