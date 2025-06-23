# strategy_logic.py

def generate_signals(price_data, sentiment_data):
    signals = {}
    sentiment = sentiment_data["avg_sentiment"]

    for ticker, info in price_data.items():
        # Pull values and flatten Series into usable types
        try:
            spike = float(info["spike"].iloc[0]) if hasattr(info["spike"], "iloc") else float(info["spike"])
        except:
            spike = 0.0

        try:
            rsi_val = float(info["rsi"].iloc[0]) if hasattr(info["rsi"], "iloc") else float(info["rsi"])
        except:
            rsi_val = 50.0

        try:
            macd_up = bool(info["macd_up"].iloc[0]) if hasattr(info["macd_up"], "iloc") else bool(info["macd_up"])
        except:
            macd_up = False

        try:
            macd_down = bool(info["macd_down"].iloc[0]) if hasattr(info["macd_down"], "iloc") else bool(info["macd_down"])
        except:
            macd_down = False

        decision = "HOLD"

        if rsi_val < 30 and macd_up and sentiment > 0.2 and spike > 0.01:
            decision = "BUY"
        elif rsi_val > 70 and macd_down and sentiment < -0.2 and spike < -0.01:
            decision = "SELL"

        print(f"📊 {ticker}: {decision} | Spike: {spike} | RSI: {rsi_val} | MACD↑: {macd_up} | Sentiment: {sentiment}")
        signals[ticker] = decision

    return signals
