# main_final.py

from price_watcher import check_price_spikes
from news_scanner import scan_news_sentiment
from strategy_logic import generate_signals
from trade_executor import execute_trade
from portfolio_manager import allocate_capital
import time
import datetime

print("📈 Running Full Market Bot with Risk + Indicators...\n")

# Step 1: Check for price spikes
price_data = check_price_spikes()

# Step 2: Scan news and compute sentiment
sentiment_data = scan_news_sentiment()

# Step 3: Generate buy/sell/hold signals
signals = generate_signals(price_data, sentiment_data)

# Step 4: Execute trades (paper trade)
for ticker, decision in signals.items():
    execute_trade(ticker, decision, price_data, sentiment_data)

# Step 5: Allocate new capital if it's a deposit day
today = datetime.datetime.today()
if today.day in [1, 15]:  # auto-invest every 1st & 15th
    allocate_capital()

print("\n✅ All tasks complete. Logs updated.")
 
