import os
from dotenv import load_dotenv
load_dotenv()

ticker     = 'AAPL'
api_key    = os.environ['APIKEY']
end_date   = '2023-04-12 05:00:00' # 2023-03-22 10:00:00
interval   = '1min' # 1min
wait_time  = 5.0 # 60.0 in sec 
start_date = '2023-04-12 03:30:00' # 2023-03-22 03:30:00