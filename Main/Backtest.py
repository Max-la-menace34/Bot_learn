from curses import window
from matplotlib.pyplot import close
import pandas as pd
from binance.client import Client
import ta
import talib as tal
import Load_data
import Draw_result
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

CSV_PATH='BTCUSDT_1hour_january_2021.csv'
df = Load_data.data_from_csv_file(CSV_PATH)
#Création de la première stratégie

def first_strat(df,jours_petit,jour_long):
    rsi=False
    macd=True
    list_des_ventes_et_des_achats=[]
    df['SMA200']= ta.trend.sma_indicator(df['close'],jours_petit)#200
    df['SMA600']=ta.trend.sma_indicator(df['close'],jour_long)#600
    df['RSI']=tal.RSI(df['close'],timeperiod=30)
    usdt=1000
    btc=0
    lastIndex=df.first_valid_index()

    for index, row in df.iterrows():
        if rsi==True:
            if df['RSI'][index]>80 and btc>0.0001:
                usdt = btc* df['close'][index]
                usdt = usdt - 0.0007*usdt
                btc = 0
                list_des_ventes_et_des_achats.append([df['timestamp'][index],"sell"])
                #print("Sell BTC at ",df['close'][index],'$ the',index)
            if df['RSI'][index]<20 and usdt>10:
                btc = usdt/df['close'][index]
                btc = btc -0.007*btc
                usdt=0
                list_des_ventes_et_des_achats.append([df['timestamp'][index],"buy"])
                #print("Buy BTC at ", df['close'][index], '$ the', index)
        if macd==True:

            if df['SMA200'][lastIndex]>df['SMA600'][lastIndex] and usdt>10:
                btc = usdt/df['close'][index]
                btc = btc -0.007*btc
                usdt=0
                list_des_ventes_et_des_achats.append([df['timestamp'][index],"buy"])
                #print("Buy BTC at ", df['close'][index], '$ the', index)
            if df['SMA200'][lastIndex]<df['SMA600'][lastIndex] and btc>0.0001:
                usdt = btc* df['close'][index]
                usdt = usdt - 0.0007*usdt
                btc = 0
                list_des_ventes_et_des_achats.append([df['timestamp'][index],"sell"])
                #print("Sell BTC at ",df['close'][index],'$ the',index)
        lastIndex = index
    finalResult = usdt + btc*df['close'].iloc[-1]
    csv_path='BTCUSDT_1hour_january_2021.csv'
    Draw_result. affihcer_buy_and_sell_Backtest(csv_path,list_des_ventes_et_des_achats)   
    return finalResult


print("Final result", first_strat(df,197,603),'USDT')
print("Just holding",(1000/df['close'].iloc[0])*df['close'].iloc[-1],'USDT')
