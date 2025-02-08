
#anti spam/cooldown
import discord
import random
from jdr import *
import os
#from attest import *
#import playlists as p
random.seed()
jDR_Data = data_stat()
#attest_class = attest()
def nosharp(str1):
    return str1.split("#")[0]

def name(author):

    if(type(author) is discord.member.Member and author.nick != None):
        return author.nick
    return nosharp(str(author))

def has_permission(member,permission):

    for role in member.roles:
        print(role.permissions.__getattribute__(permission))
        if role.permissions.__getattribute__(permission):
            return True
    return False


def query(author):
    return

async def message_function(m, call_together_ai):
    """ Handles messages, including AI and custom commands. """

    content_lower = m.content.lower()

    # AI Chat Command
    if content_lower.startswith("$ask"):
        prompt = m.content[len("$ask "):].strip()
        if not prompt:
            return "Please provide a question."

        await m.channel.send("Thinking... 🤖")
        return call_together_ai(prompt)

    # Basic Auto-Responses
    responses = {
        "j'ai faim": f"T'as perdu : {name(m.author)}",
        "bonjour": f"Bonjour {name(m.author)}",
        "jour": f"Bonjour {name(m.author)}",
        "bonne nuit": random.choice(["Nenuit", "Bonne nuit", "See you space cowboy"]) + f" {name(m.author)}",
        "nenuit": random.choice(["Nenuit", "Bonne nuit", "See you space cowboy"]) + f" {name(m.author)}",
        "ping": "pong"
    }

    if content_lower in responses and m.author.id != 203619925179236352:
        return responses[content_lower]

    # Display user ID
    if content_lower == "$id":
        return f"L'ID de {name(m.author)} est: {m.author.id}"

    # Moderation Commands
    if content_lower.startswith("$victim") and has_permission(m.author, "move_members"):
        for member in m.mentions:
            await member.move_to(m.guild.get_channel(369161932730662922))
        return None

    if content_lower.startswith("$kick") and has_permission(m.author, "move_members"):
        member_name = m.content.split("$kick")[-1].strip()
        member = m.guild.get_member_named(member_name)
        if member:
            await member.move_to(m.guild.get_channel(369161932730662922))
        else:
            return f"User {member_name} not found."
        return None

    # Dice Rolls
    if content_lower.startswith("$dé"):
        try:
            value = int(m.content.split("$dé")[-1].strip())
            if value <= 0:
                return "Les dés doivent être des entiers positifs."
            rd = random.randint(1, value)
            return str(rd)
        except ValueError:
            return "Format invalide. Utilisation: `$dé <nombre>`"

    # RPG Dice Rolls
    if content_lower.startswith("$roll"):
        id = m.author.id
        roll_message = m.content[len("$roll "):].strip()
        return jDR_Data.roll(roll_message, id)

    # Server Reboot Command
    if content_lower.startswith("$reboot") and has_permission(m.author, "administrator"):
        await m.channel.send("Redémarrage en cours...")
        os.system("reboot")
        return None

    return None  # No message sent
