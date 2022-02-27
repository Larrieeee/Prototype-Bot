# Variables --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from dotenv import load_dotenv
import os
import discord

load_dotenv()
discordToken = os.getenv("Token")

from discord.ext import commands, tasks
bot = commands.Bot(command_prefix = "uh ")

# Use with discord.ext tasks.loop to doing things like update bot presence 
from itertools import cycle
cycleStatus = cycle(["Sketching", "Polynomials", "Simulator"])

# Functions --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@tasks.loop(seconds = 8)
async def playGame():
    await bot.change_presence(activity = discord.Game(next(cycleStatus)))

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")
    
    await bot.change_presence(activity = discord.Game("Keyword Monkey"))
    playGame.start()

@bot.command(name = "test")
async def whats_good(context, user = "<@490277278136270874>"):

    await context.reply(f"YOO WHATS GOOD {user}")

@bot.command(pass_context = True)
async def joinVoice(context):
    
    inVoice = context.author.voice

    # If context.author.voice is not nil 
    if (inVoice):
        await inVoice.channel.connect()
    
    else:
        await context.send("Not in channel")

# Error handler for discord.ext bot
@bot.event
async def on_command_error(context, error):
    
    if isinstance(error, commands.MissingRequiredArgument):
        await context.reply("I'm missing some information. Try again")

    if isinstance(error, commands.CommandNotFound):
        await context.reply("Not a valid command bozo")

# MainSetup --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run(discordToken)

# ReadNotes --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# We can add defalut parameters if the user forgets to input one

# context.reply = replys to the message.author
# context.send = sends a regular message

# bot.latency = gives your ping time (in seconds)

# name = custom call of function (one way to call)
# aliases = multiple ways to call same function

# You can use fileName[-integerNumber] to remove characters off a string