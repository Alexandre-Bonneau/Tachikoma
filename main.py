import discord
import asyncio
import random
from bot_token import TOKEN
from message import *
from together import Together

TOGETHER_AI_KEY = "b1a36c050a36d93019cf8e7f4d21444f04934ba2a5be591b1aea734c13f2c2bf"

client_ai = Together(api_key=TOGETHER_AI_KEY)
intents = discord.Intents.default()  # Allow the use of custom intents
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity_ = discord.Activity(type = discord.ActivityType.playing, name="Trying its best")
    await client.change_presence(status=discord.Status.online, activity=activity_)

def call_together_ai(prompt):
    """ Calls TogetherAI and returns a valid response or error message """
    response = client_ai.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|end_of_sentence|>"],
        stream=False
    )

    # Debugging: Print full response for inspection
    print("Raw API Response:", response)

    # Ensure response has the correct structure
    if "choices" in response and len(response["choices"]) > 0:
        message_content = response["choices"][0].get("message", {}).get("content", "").strip()

        if message_content:
            return message_content  # Return actual AI response
        else:
            return "🤖 I couldn't generate a response. Try again!"
    else:
        return "❌ Error: Unexpected API response format."


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    tab = await message_function(message,call_together_ai)
    print('rrr')
    print(tab)
    if tab:
        print("here")
        print(dir(tab))
        
        await message.channel.send("rrr")
        await message.channel.send(tab)
        



client.run(TOKEN)
# cd /d D:
# cd Programmation/Discordbot/Tachikoma
# python test2.py
