# Variables --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import nextcord
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

# MainSetup --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run(discordToken)