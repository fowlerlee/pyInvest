import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def setup_priceplot(sym, time):
    for symbol in sym:
        df = yf.download(tickers=symbol, period=time)
        print(df.index)
        print(df.head())
        print(df.loc["2022-12-15":"2023-01-06"])
        print(df.loc["2019":])
        print(df.info())
        print("volume x close price")
        print(df.Volume.mul(df.Close))
        df.Close.plot(figsize=(12, 8), fontsize=12)
        plt.ylabel("Price(US Dollar)")
        plt.title(f"{symbol} price chart", fontsize=15)
        plt.show()
        df.loc["2022-6", "Volume"].plot(figsize=(12, 8), kind="bar")
        plt.ylabel("Volume(shares)")
        plt.title(f"{symbol} daily volume traded", fontsize=15)
        plt.show()


def dividends(sym, time):
    for symbol in sym:
        df = yf.download(tickers=symbol, period=time, actions=True)
        print(f"The dividends for {symbol} stocks")
        print(df.loc[df.Dividends != 0])
        print(f"The dividends for {symbol} is {df.Dividends.sum()}")
        print(f"The stock increase for {symbol} is {df.Close[-1] - df.Close[0]}")
#       print(f"The stock splits for {symbol} stocks")
#       print(df.loc[df.Stock_Splits != 0])
        df.loc[df.Dividends != 0].Dividends.plot()
        plt.ylabel("Dividends")
        plt.title(f"{symbol} dividends (US Dollar)", fontsize=15)
        plt.show()


if __name__ == '__main__':
    time_period = "max"  # 1y or 1mo
    apple = "AAPL"
    volvo = "VLVLY"
    nordea = "NDA-SE.ST"
    sandvik = "SAND.ST"
    seb = "SEB-A.ST"
    stock1 = [apple, volvo]
    stock2 = [seb, nordea, sandvik]
  #  setup_priceplot(stock1, time_period)
  #  dividends(stock1, time_period)
#    setup_priceplot(stock2, time_period)
    dividends(stock2, time_period)
