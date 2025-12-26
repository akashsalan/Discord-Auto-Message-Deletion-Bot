🕒 Discord Auto Message Deletion Bot

A lightweight Discord bot built with discord.py that automatically deletes messages after a specified time, cleans channels, and provides simple moderation utilities.

✨ Features

⏱ Timed message deletion

Automatically delete new messages after a set duration (seconds, minutes, or hours)

🧹 Channel cleaning

Bulk delete all messages in a channel

🛑 Stop deletion anytime

Disable auto-deletion per channel

🏓 Ping command

Check bot latency and online status

⚡ Rate-limit friendly

Uses delays to avoid Discord API abuse

📦 Requirements

Python 3.8+

discord.py (v2.0 or newer)

Install dependencies:

pip install -U discord.py

🚀 Setup & Installation

Clone the repository

git clone https://github.com/yourusername/discord-auto-delete-bot.git
cd discord-auto-delete-bot


Create a Discord Bot

Go to the Discord Developer Portal

Create a new application

Add a bot and copy the Bot Token

Enable Message Content Intent

Configure the bot
Replace the token in the code:

TOKEN = "YOUR-TOKEN"


Run the bot

python bot.py

🧠 Commands
Command	Description
!timer 10s	Auto-delete new messages after 10 seconds
!timer 5m	Auto-delete new messages after 5 minutes
!timer 2h	Auto-delete new messages after 2 hours
!stop	Stop auto-deleting messages in the channel
!clean	Delete all messages in the channel
!ping	Check bot latency

📌 Note: Only messages sent after !timer is activated will be deleted.

🔐 Permissions Needed

Make sure the bot has:

Read Messages

Manage Messages

Read Message History

⚠️ Important Notes

The !clean command deletes all messages in a channel — use with caution

Timers are per-channel

Bot ignores messages from other bots

Deletion runs every second for accuracy

🛠 Customization Ideas

Add per-user timers

Add role-based permissions

Save timers to a database

Slash command support (/timer, /stop, etc.)

📄 License

This project is licensed under the MIT License — free to use, modify, and distribute.

❤️ Contributing

Pull requests are welcome!
If you find a bug or have a feature idea, feel free to open an issue.
