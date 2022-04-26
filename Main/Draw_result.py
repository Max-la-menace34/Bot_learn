import Load_data
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


def afficher_ohlcv(csv_path):
    df_data= Load_data.data_from_csv_file(csv_path)
    #fig = px.line(df_data,x='timestamp',y='close')
    fig =go.Figure(data=go.Ohlc(x=df_data['timestamp'],
    open=df_data["open"],
    high=df_data['high'],
    low=df_data['low'],
    close=df_data['close'],
    increasing_line_color='cyan',
    decreasing_line_color='gray'))
    return fig.show()

def afficher_evolution_des_closes(csv_path):
    df_data= Load_data.data_from_csv_file(csv_path)
    fig = px.line(df_data,x='timestamp',y='close',title='Evolution des closes en fonction du temps')
    return fig.show()

def affihcer_buy_and_sell_Backtest(csv_path,list_backtest):
    df_data= Load_data.data_from_csv_file(csv_path)
    fig =go.Figure(data=go.Ohlc(x=df_data['timestamp'],
    open=df_data["open"],
    high=df_data['high'],
    low=df_data['low'],
    close=df_data['close']))
    for index in range(len(list_backtest)):
        if list_backtest[index][1]=="buy":
            fig.add_vline(x=list_backtest[index][0],line_color='green')
        elif list_backtest[index][1]=="sell":
            fig.add_vline(x=list_backtest[index][0],line_color='red')
        else:
            print("Error to print a line")   
    return fig.show()




    


