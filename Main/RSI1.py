import ta
import talib as tal
import pandas as pd
import Draw_result
def RSI_strat(df,down,up):
    list_des_ventes_et_des_achats=[]
    df['RSI']=tal.RSI(df['close'],timeperiod=30)
    usdt=1000
    btc=0
    lastIndex=df.first_valid_index()
    for index, row in df.iterrows():

        if df['RSI'][lastIndex]>up and btc>0.0001:
                    usdt = btc* df['close'][index]
                    usdt = usdt - 0.0007*usdt
                    btc = 0
                    list_des_ventes_et_des_achats.append([df['timestamp'][index],"sell"])
        if df['RSI'][lastIndex]<down and usdt>10:
                    btc = usdt/df['close'][index]
                    btc = btc -0.007*btc
                    usdt=0
                    list_des_ventes_et_des_achats.append([df['timestamp'][index],"buy"])
        lastIndex = index
    finalResult = usdt + btc*df['close'].iloc[-1]
    csv_path='Main/BTCUSDT_1hour_january_2021.csv'
    Draw_result. affihcer_buy_and_sell_Backtest(csv_path,list_des_ventes_et_des_achats)   
    return finalResult