import discord
import asyncio
import random
from bot_token import TOKEN
from message import *


intents = discord.Intents.default()  # Allow the use of custom intents
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity_ = discord.Activity(type = discord.ActivityType.playing, name="Trying its best")
    await client.change_presence(status=discord.Status.online, activity=activity_)



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    tab = await message_function(message)




client.run(TOKEN)
# cd /d D:
# cd Programmation/Discordbot/Tachikoma
# python test2.py
