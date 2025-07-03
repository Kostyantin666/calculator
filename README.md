# 🗞️ Lenta.ru News Parser + Telegram Bot (with GUI)

Desktop app that fetches fresh news from [lenta.ru](https://lenta.ru), displays them in a GUI, and sends to Telegram in one click.

## 💻 Features
- Parses headlines, links and timestamps from Lenta.ru
- Shows latest news in a simple GUI (Tkinter)
- Sends news to Telegram with one button
- Dark theme with automatic refresh
- History of last 10 news items

## 📦 How to run

```bash
pip install -r requirements.txt
python news_gui_bot.py
```

## 🚀 Build to .exe

```bash
pyinstaller --onefile --windowed --icon=news_icon_1.ico news_gui_bot.py
```

## 📷 Screenshots

> (img/screen_npb_1.png)(img/screen_npb_2.png)

## 🛠 Tech stack

- Python 3
- Tkinter
- BeautifulSoup4
- python-telegram-bot
- Asyncio

## 🧠 Author

Konstantin
