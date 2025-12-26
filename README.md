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
```
## 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/discord-auto-delete-bot.git
cd discord-auto-delete-bot
```
### 2. Create a Discord Bot

1. Go to the **Discord Developer Portal**
2. Create a new application
3. Add a bot
4. Copy the **Bot Token**
5. Enable **Message Content Intent**

---

### 3. Configure the Bot

Open the bot file and replace:

```python
TOKEN = "YOUR-TOKEN"
```

### 4. Run the Bot

```bash
python bot.py
```

## 🧠 Commands

| Command | Description |
|--------|------------|
| `!timer 10s` | Auto-delete messages after 10 seconds |
| `!timer 5m` | Auto-delete messages after 5 minutes |
| `!timer 2h` | Auto-delete messages after 2 hours |
| `!stop` | Stop auto-deleting messages in the channel |
| `!clean` | Delete all messages in the channel |
| `!ping` | Check bot latency |

> 📌 **Note:**  
> Only messages sent *after* the `!timer` command is activated will be deleted.

## 🔐 Required Permissions

The bot requires the following permissions:

- Read Messages
- Read Message History
- Manage Messages

---

## ⚠️ Important Notes

- `!clean` permanently deletes **all messages** in a channel — use with caution
- Timers are **channel-specific**
- Bot ignores messages sent by other bots
- Auto-deletion checks every second for accuracy

---

## 🛠 Customization Ideas

- Convert commands to slash commands
- Add role-based permissions
- Store timers in a database
- Per-user auto-delete timers
- Add logging and moderation features

---

## 📄 License

This project is licensed under the **MIT License**.

