import discord
import asyncio
import random
from bot_token import TOKEN
from message import *
from together import Together

TOGETHER_AI_KEY = "b1a36c050a36d93019cf8e7f4d21444f04934ba2a5be591b1aea734c13f2c2bf"

client_ai = Together(api_key=TOGETHER_AI_KEY)
intents = discord.Intents.default()
intents.message_content = True  # Nécessaire pour lire le contenu des messages
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    activity = discord.Activity(type=discord.ActivityType.playing, name="Trying its best")
    await client.change_presence(status=discord.Status.online, activity=activity)

def call_together_ai(prompt):
    """Calls TogetherAI and returns a valid response or error message."""
    response = client_ai.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[
            {"role": "system", "content": "You are an advanced AI Discord Bot called Tachikoma. Answer concisely and accurately."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.5,
        top_p=0.9,
        stop=["<|end_of_sentence|>"],
        stream=False
    )

    response_dict = response.model_dump()

    if "choices" in response_dict and len(response_dict["choices"]) > 0:
        return response_dict["choices"][0]["message"]["content"].strip()
    else:
        return "🤖 AI did not return a valid response."

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    reply = await message_function(message, call_together_ai)
    
    if reply:
        await message.channel.send(reply)

client.run(TOKEN)
