# 🕒 Discord Auto Message Deletion Bot

A lightweight **Discord moderation bot** built with `discord.py` that automatically deletes messages after a specified time, cleans channels, and provides simple utility commands.

---

## ✨ Features

- ⏱ **Timed Message Deletion**
  - Automatically deletes new messages after a specified duration
  - Supports seconds, minutes, and hours (`10s`, `5m`, `2h`)
- 🧹 **Channel Cleaning**
  - Bulk delete all messages in a channel
- 🛑 **Stop Auto-Deletion**
  - Disable message deletion per channel
- 🏓 **Ping Command**
  - Check if the bot is online and responsive
- ⚡ **Rate-Limit Safe**
  - Built-in delays to prevent Discord API abuse

---

## 📦 Requirements

- Python **3.8 or higher**
- `discord.py` **v2.0+**

Install dependencies:
```bash
pip install -U discord.py
