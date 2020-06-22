import discord
import asyncio
import random
from bot_token import TOKEN
from message import *




client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name="Trying its best"))



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    tab = await message_function(message)




client.run(TOKEN)
# cd /d D:
# cd Programmation/Discordbot/Tachikoma
# python test2.py
