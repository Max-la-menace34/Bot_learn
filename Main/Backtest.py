from curses import window
from matplotlib.pyplot import close
import pandas as pd
from binance.client import Client
import ta
import talib as tal
import Load_data
import SMA1
import RSI1


"""
klinest = Client().get_historical_klines("BTCUSDT",Client.KLINE_INTERVAL_1HOUR,"01 January 2022")

df = pd.DataFrame(klinest,columns=['timestamp','open','high','low','close','volume','close-time','quote_av','trades','tb_base_av','tb_quote_av','ignore'])
del df['ignore']
del df['close-time']
del df['quote_av']
del df['trades']
del df['tb_base_av']
del df['tb_quote_av']
df['close']=pd.to_numeric(df['close'])
df['high']=pd.to_numeric(df['high'])
df['low']=pd.to_numeric(df['low'])
df['open']=pd.to_numeric(df['open'])
df['timestamp']=pd.to_numeric(df['timestamp'])
df['volume']=pd.to_numeric(df['volume'])

df = df.set_index(df['timestamp'])
df.index =pd.to_datetime(df.index, unit='ms')
del df['timestamp']
"""

CSV_PATH='Main/BTCUSDT_1hour_january_2021.csv'
df = Load_data.data_from_csv_file(CSV_PATH)




print("Final result", RSI1.RSI_strat(df,20,80),'USDT')
print("Just holding",(1000/df['close'].iloc[0])*df['close'].iloc[-1],'USDT')
