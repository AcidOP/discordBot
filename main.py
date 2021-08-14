# !/usr/bin/python3

import os
import json
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!",case_insensitive=True , intents=discord.Intents.all())

token = "<discord token>"

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")

@bot.event
async def on_message(message):
    # Bot will not reply to the bot itself
    if message.author == bot.user:
        return

    await bot.process_commands(message)

# Load your cogs (if any)
for file in os.listdir("/path/to/your/cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")
        print(f"The extension {file} was loaded.")


bot.run(token)
