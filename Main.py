# Variables --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from dotenv import load_dotenv
import os
load_dotenv()
discordToken = os.getenv("Token")

from prefix import yooPrefix
bot = commands.Bot(command_prefix = yooPrefix())

# Functions --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.event
async def on_ready():
    print(bot.user)

# Pass an indefinite number of arguments. Command responds with "YOO WHATS GOOD" when the user inputs yoo what's
@bot.command(aliases = ["whats", "WHATS", "what's"])
async def whats_good(context, *good):
    await context.reply(f"YOOOOOOOOOOO WHATS GOOD <@{context.author.id}>")
    await context.message.add_reaction("<:hehehehaw:945416057626165308>")

# Slash Commands --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.slash_command(name = "indirect_ping", description = "Ping some guy", guild_ids = [586680405302968321])
async def target_ping(interaction: Interaction, message:str):

    await interaction.response.send_message(f"{message}")

# MainSetup --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run(discordToken)
# Note that the bot runs under the invite "applications.command"