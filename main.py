import discord
import asyncio
import random
from bot_token import TOKEN
from message import *
from together import Together
client_ai = Together()
intents = discord.Intents.default()  # Allow the use of custom intents
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity_ = discord.Activity(type = discord.ActivityType.playing, name="Trying its best")
    await client.change_presence(status=discord.Status.online, activity=activity_)

def call_together_ai(prompt):
    response = client_ai.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|end_of_sentence|>"],
        stream=False  # Set to False for single response
    )
    
    return response.choices[0].message.content

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    tab = await message_function(message)




client.run(TOKEN)
# cd /d D:
# cd Programmation/Discordbot/Tachikoma
# python test2.py
