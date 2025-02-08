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
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",  # Now using Mistral
        {"role": "system", "content": "You are an advanced AI Discord Bot Called Tachikoma. Answer concisely and accurately."}
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.5,
        top_p=0.9,
        stop=["<|end_of_sentence|>"],
        stream=False
    )

    response_dict = response.model_dump()  # Convert response to dictionary

    # Extract AI response
    if "choices" in response_dict and len(response_dict["choices"]) > 0:
        return response_dict["choices"][0]["message"]["content"].strip()
    else:
        return "🤖 AI did not return a valid response."



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
    
    if tab:
        
        await message.channel.send(tab)
        



client.run(TOKEN)
# cd /d D:
# cd Programmation/Discordbot/Tachikoma
# python test2.py
