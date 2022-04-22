from curses import window
from email import header
from operator import index
from matplotlib.pyplot import close
import pandas as pd
from binance.client import Client
import ta
import talib as tal


def load_data_function():
    klinest = Client().get_historical_klines("BTCUSDT",Client.KLINE_INTERVAL_1HOUR,"01 January 2021")

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
    return df

def data_to_csv_file(df):
    CSV_PATH='BTCUSDT_1hour_january_2021.csv'
    df.to_csv(CSV_PATH,index=True,sep=';',header=True)
    return 'Done'

def data_from_csv_file(csv_path):
    df = pd.read_csv(csv_path,sep=';')
    return df

 
