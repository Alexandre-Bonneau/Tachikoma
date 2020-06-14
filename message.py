#anti spam/cooldown
import discord
import random

def nosharp(str1):
    return str1.split("#")[0]

def name(author):
    if(type(author) is discord.user.User):
        return nosharp(str(author))
    if(type(author) is discord.member.Member):
        return author.nick
    return "noname"

def has_permission(member,permission):
    for role in member.roles:
        if role.permissions.__getattribute__(permission):
            return True
    return False


def query(author):
    return

async def message_function(m):

    ret_value = []
    if "j'ai faim" in(m.content.lower()):
        await m.channel.send("T'as perdu : " +name(m.author))

    if "bonjour" in(m.content.lower()):
        await m.channel.send("Bonjour : " +name(m.author))
    
    if "$victim" in (m.content.lower()) and has_permission(m.author,"move_members"):
        for k in m.mentions:
            await k.move_to(m.author.guild.get_channel(369161932730662922))
    if "$dé" in(m.content):

        k=(m.content.split("$dé")[-1]).split("$")[0]
        int(k)
        rd = -1
        try:
            value = int(k)

            if value<=0:
                    await m.channel.send("Les dés sont des entiers positifs")
            else:
                rd = random.randint(0,value-1)
                if((rd ==0 or rd ==9) and value ==10):
                    rd2 = random.randint(0,value-1)
                    rd = 10*rd+rd2
                    if(rd>=95):
                        await m.channel.send("Oh le critique de " + name(m.author))
                    if(rd<5):
                        await m.channel.send( "Cheh, critique de " + name(m.author))
                        rd = "0"+str(rd)
                await m.channel.send( rd)
        except:
            await m.channel.send( "Les dés sont des entiers positifs")

    return 0
