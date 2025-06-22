# trade_executor.py

import csv
import datetime

def execute_trade(ticker, decision, price_data, sentiment_data):
    if decision == "HOLD":
        return

    info = price_data[ticker]
    sentiment = sentiment_data["avg_sentiment"]
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    price = info["price"]

    rationale = (
        f"Spike={info['spike']}, RSI={info['rsi']}, "
        f"MACD_Up={info['macd_up']}, Sentiment={sentiment}"
    )

    with open("log_trades.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([now, ticker, decision, price, rationale])

    print(f"💥 {decision} EXECUTED on {ticker} at ${price} | {rationale}")
 
