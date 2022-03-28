# Variables --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv(".env")

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from datetime import datetime 
import asyncio, math
from settings import yooPrefix

discordToken = os.getenv("TOKEN")
bot = commands.Bot(command_prefix = "pls ")

# Functions --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.event
async def on_ready():
    print(f"{bot.user} has turned itself on!")
    startTime = datetime.timestamp(datetime.now())

    while True:
        await asyncio.sleep(5)
        currentTime = datetime.timestamp(datetime.now())
        elapsedTime = round((float(currentTime) - float(startTime)))

        await bot.change_presence(activity = nextcord.Game(name = f"for {round((elapsedTime / 360), 2)} Hours"))

@bot.slash_command(name = "ping", description = "ping pong?", guild_ids = [949110139531722802])
async def ping_pong(interaction: Interaction):
    await interaction.response.send_message("Pong!")

# Remove the default 'help' command 
bot.remove_command("help")

@bot.command(name = "help")
async def help_command(context, *arg):
    userName = context.author

    await userName.send("Hello")

# MainSetup --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run(discordToken)