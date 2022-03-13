# Variables --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from dotenv import load_dotenv
import os
load_dotenv(".env")

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

discordToken = os.getenv("TOKEN")
bot = commands.Bot(command_prefix = "pls ")

# Functions --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.event
async def on_ready():
    print(f"{bot.user} has turned itself on!")
    await bot.change_presence(activity = nextcord.Game(name = "Test"))

@bot.slash_command(name = "ping", description = "ping pong?", guild_ids = [949110139531722802])
async def ping_pong(interaction: Interaction):

    await interaction.response.send_message("Pong!")

# MainSetup --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run(discordToken)