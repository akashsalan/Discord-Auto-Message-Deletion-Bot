import discord
from discord.ext import commands
import asyncio
import re
import time

TOKEN = "YOUR-TOKEN"  # Replace with your bot token

# Bot setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Required for message reading
bot = commands.Bot(command_prefix="!", intents=intents)

# Timed deletion storage
delete_timers = {}
active_messages = {}  # Store only messages sent after !timer is used
cleaning_active = {}

# Command: Start timed message deletion
@bot.command()
async def timer(ctx, duration: str):
    """Enable auto-deletion of messages after a specified time (e.g., !timer 10s, !timer 5m, !timer 2h)"""
    channel_id = ctx.channel.id

    # Convert duration to seconds
    multiplier = {"s": 1, "m": 60, "h": 3600}
    unit = duration[-1]
    if unit not in multiplier or not duration[:-1].isdigit():
        await ctx.send("Invalid format! Use `!timer 10s`, `!timer 5m`, or `!timer 2h`.", delete_after=5)
        return
    
    seconds = int(duration[:-1]) * multiplier[unit]
    
    # Activate timer for the channel
    delete_timers[channel_id] = seconds
    active_messages[channel_id] = []  # Track new messages sent after timer starts
    await ctx.send(f"\U0001F551 Auto-delete set for {duration}. Messages will disappear after {duration}.", delete_after=5)

    # Delete command message itself
    try:
        await ctx.message.delete()
    except discord.errors.NotFound:
        pass

    # Start auto-deletion process
    while channel_id in delete_timers:
        await asyncio.sleep(1)  # Check every second
        
        if channel_id not in active_messages:
            break

        current_time = time.time()
        for message in active_messages[channel_id][:]:
            if current_time - message.created_at.timestamp() >= delete_timers[channel_id]:
                try:
                    await message.delete()
                    active_messages[channel_id].remove(message)
                    await asyncio.sleep(0.2)  # Prevent rate limiting
                except discord.errors.NotFound:
                    pass

# Event: Track new messages to delete
@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore bot messages

    channel_id = message.channel.id
    if channel_id in delete_timers:
        active_messages[channel_id].append(message)  # Only store messages after !timer

    await bot.process_commands(message)  # Allow commands to work

# Command: Stop auto-deletion
@bot.command()
async def stop(ctx):
    """Stop auto-deleting messages"""
    channel_id = ctx.channel.id
    delete_timers.pop(channel_id, None)  # Stop timed deletion
    active_messages.pop(channel_id, None)  # Clear stored messages
    cleaning_active.pop(channel_id, None)  # Stop cleaning if active
    await ctx.send("\U0001F6D1 Auto-deletion has been stopped!", delete_after=5)

    try:
        await ctx.message.delete()
    except discord.errors.NotFound:
        pass

# Command: Clean entire channel
@bot.command()
async def clean(ctx):
    """Delete all messages in the channel"""
    channel_id = ctx.channel.id
    cleaning_active[channel_id] = True
    await ctx.send("\U0001F9F9 Cleaning chat...", delete_after=3)
    
    while cleaning_active.get(channel_id):
        deleted = await ctx.channel.purge(limit=50)
        if not deleted:
            break  # Stop if no more messages
        await asyncio.sleep(1)  # Prevent rate limits
    
    cleaning_active.pop(channel_id, None)

# Command: Check bot is online
@bot.command()
async def ping(ctx):
    """Check if the bot is responsive"""
    await ctx.send(f"\U0001F3D3 Pong! {round(bot.latency * 1000)}ms")

# Run the bot
bot.run(TOKEN)
