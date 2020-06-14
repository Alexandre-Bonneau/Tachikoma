import discord
import asyncio
import random
from bot_token import TOKEN
from message import *
random.seed()



client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    tab = await message_function(message)
    # print(tab)
    # if (len(tab)>0):
    #     for m in tab:
    #         print(m)
    #         await message.channel.send(m)




client.run(TOKEN)
# cd /d D:
# cd Programmation/Discordbot/Tachikoma
# python test2.py
