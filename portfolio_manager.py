# portfolio_manager.py

import datetime
import csv
import random

DIVIDEND_TICKERS = ["SCHD", "VYM", "O", "LTC"]

def allocate_capital(amount=50):
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chosen = random.choice(DIVIDEND_TICKERS)  # You can replace with smarter logic later

    with open("log_trades.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, chosen, "INVEST", "50.00", "Scheduled $50 investment (biweekly)"])

    print(f"💰 Auto-Invested $50 into {chosen} on schedule.")
 
