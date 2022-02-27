# Variables --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import nextcord
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