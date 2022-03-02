# Variables --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from tokenize import Name
import nextcord
from nextcord import Interaction
from nextcord.ext import commands 

from dotenv import load_dotenv
load_dotenv()
import os

bot = commands.Bot(command_prefix = "uh ")
discordToken = os.getenv("Token")

import requests
weatherKey = os.getenv("weatherKey")
from pprint import pprint

# Functions --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.event
async def on_ready():
    await bot.change_presence(activity = nextcord.activity.Game("Nextcord"))
    print(f"{bot.user} is working as it should..")

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    try:
        await message.add_reaction(reactionEmoji)
    except NameError:
        print("No emoji set")

    await bot.process_commands(message)

@bot.slash_command(guild_ids=[586680405302968321])
async def ding(interaction: Interaction):
    await interaction.response.send_message("Pong!")

@bot.command(name = "setemoji".lower())
async def change_reaction(context, emoji):
    
    try:
        global reactionEmoji
        reactionEmoji = emoji
        await context.message.add_reaction(emoji)
    
    except nextcord.HTTPException:
        await context.reply("Not an emoji?")

# Primitive weather detection command
@bot.command()
async def weather(context, city):

    # Calls the weather API 
    base_url =  f"http://api.openweathermap.org/data/2.5/weather?appid={weatherKey}&q={city}"
    
    # Grabs the data in a json format (https://www.youtube.com/watch?v=9N6a-VLBa2I)
    weather_data = requests.get(base_url).json()

    try:
        await context.reply(weather_data["wind"])
    except KeyError:
        await context.reply("City not found")

# MainSetup --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run(discordToken)