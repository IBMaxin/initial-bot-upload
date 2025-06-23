# Hybrid Trading Bot

**Live, Automated Momentum Bot** for BTC, XLE, OXY, and CVX.  
Fuses RSI, MACD, and NLP sentiment to trigger smart trades.

---

### ✅ Features
- RSI + MACD trend analysis
- Spike & sentiment detection from news headlines
- Multi-asset support: BTC-USD, XLE, OXY, CVX
- Automated $50 biweekly investment into:
  - SCHD, VYM, O, LTC (dividend ETFs)
- Risk management: stop-loss, take-profit, max drawdown
- Trade logging with full rationale
- JSON-configured portfolio logic

---

### 🔧 Setup Instructions
```bash
git clone https://github.com/IBMaxin/initial-bot-upload.git
cd initial-bot-upload
python -m venv venv
venv\Scripts\activate     # or source venv/bin/activate
pip install -r requirements.txt
python main.py
