# XRPL Wallet Tracker Bot

A Telegram bot that tracks wallets on the XRP Ledger.

## 🔍 Features

- `/balance` – Show XRPL token balances
- `/created` – See tokens created by a wallet
- `/liquidity` – Show recent liquidity events
- `/bubble` – Visual wallet maps
- `/ancestry` – Wallet activation lineage
- Wallet age, alerts, insights, and more...

## ⚙️ Setup

```bash
git clone https://github.com/missxtina11/xrpl-wallet-tracker-bot.git
cd xrpl-wallet-tracker-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Then fill in your token info
python main.py
