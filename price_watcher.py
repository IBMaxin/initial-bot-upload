# price_watcher.py

import yfinance as yf
import pandas as pd
import datetime
from ta.momentum import RSIIndicator
from ta.trend import MACD

TICKERS = ["BTC-USD", "XLE", "OXY", "CVX"]

def check_price_spikes():
    data = {}
    end = datetime.datetime.today()
    start = end - datetime.timedelta(days=60)

    for ticker in TICKERS:
        df = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=True)

        if df.empty or len(df) < 2:
            continue

        close_prices = df['Close'].squeeze()  # Force 1D series
        df['RSI'] = RSIIndicator(close=close_prices).rsi()
        macd = MACD(close=close_prices)
        df['MACD'] = macd.macd()
        df['MACD_Signal'] = macd.macd_signal()

        latest = df.iloc[-1]
        previous = df.iloc[-2]

        spike = (latest['Close'] - previous['Close']) / previous['Close']
        rsi = latest['RSI']
        macd_cross_up = latest['MACD'] > latest['MACD_Signal']
        macd_cross_down = latest['MACD'] < latest['MACD_Signal']

        data[ticker] = {
            "price": round(latest['Close'], 2),
            "spike": round(spike, 4),
            "rsi": round(rsi, 2),
            "macd_up": macd_cross_up,
            "macd_down": macd_cross_down
        }

    return data
