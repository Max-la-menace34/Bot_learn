from curses import window
from unittest import result
from matplotlib.pyplot import close
import pandas as pd
from binance.client import Client
import ta
import talib as tal
import Load_data
import Backtest

CSV_PATH='BTCUSDT_1hour_january_2021.csv'
df = Load_data.data_from_csv_file(CSV_PATH)
total_result=[]
for jours_petit in range(150,250,1):
    for jour_long in range(550,650,1):
        result_prix = Backtest.first_strat(df,jours_petit,jour_long)
        total_result.append([result_prix,jours_petit,jour_long])
        if len(total_result)>15:
            print("On est à jour_long=",jour_long,"jour_petit",jours_petit)
            total_result.sort(reverse=True)
            total_result=total_result[:5]
total_result.sort(reverse=True)
print(total_result)
#print(Backtest.first_strat(df,200,600))