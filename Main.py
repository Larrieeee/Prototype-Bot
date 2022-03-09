# Variables --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from dotenv import load_dotenv
import os
load_dotenv()
discordToken = os.getenv("TOKEN")

from prefix import yooPrefix
bot = commands.Bot(command_prefix = yooPrefix())

import asyncio, datetime

# Functions --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.event
async def on_ready():
    print(bot.user)

# Pass an indefinite number of arguments. Command responds with "YOO WHATS GOOD" when the user inputs yoo what's
@bot.command(aliases = ["whats", "WHATS", "what's"])
async def whats_good(context, *good):
    await context.reply(f"YOOOOOOOOOOO WHATS GOOD <@{context.author.id}>")
    await context.message.add_reaction("<:hehehehaw:945416057626165308>")

@bot.command(name = "summon")
async def summon_user(context, username, amount = 5):

  for i in range(0, int(amount)):
    await context.send(f"Mr. Pham's slaves is summoning {username}. Requested {i + 1} times")
    await asyncio.sleep(1)

@bot.command(name = "wait")
async def interval_message(context, waitSeconds, *messageToSend,):

    now = datetime.datetime.now()
    waitAmount = now + datetime.timedelta(seconds = float(waitSeconds))

    wait_time = (waitAmount - now).total_seconds()

    # Waits the amount of time inputted by the user 
    await asyncio.sleep(wait_time)
    await context.send(" ".join(messageToSend))

    print(f"{context.author} used the wait command LMAO")

@bot.command(name = "hi")
async def hello_peter(context, user):
    if user.startswith("<@"):
        await context.send(f"hi {user}")

    else:
        return await context.send("Who is that?")

# Slash Commands --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.slash_command(name = "indirect_ping", description = "Ping some guy", guild_ids = [586680405302968321])
async def target_ping(interaction: Interaction, message:str):

    await interaction.response.send_message(f"{message}")

@bot.slash_command(name = "ball", description = "sack?", guild_ids = [586680405302968321])
async def ping_pong(interaction):

    await interaction.response.send_message("Sack")

@bot.slash_command(name = "larry", description = "who??", guild_ids = [586680405302968321])
async def talk_trash(interaction):
    await interaction.response.send_message("<:hehehehaw:945416057626165308>")

# MainSetup --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run(token)
# Note that the bot runs under the invite "applications.command"