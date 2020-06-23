#anti spam/cooldown
import discord
import random
import playlists as p
random.seed()
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

async def message_function(m):

    ret_value = []
    if "j'ai faim" in(m.content.lower()):
        await m.channel.send("T'as perdu : " +name(m.author))

    if "bonjour" in(m.content.lower() ) or "jour" == m.content.lower():
        await m.channel.send("Bonjour " +name(m.author))
    if "bonne nuit" in(m.content.lower()) or "nenuit" in(m.content.lower()):
        x = random.randint(0,2)
        await m.channel.send(["Nenuit ","Bonne nuit ", "See you space cowboy" ][x]+ (name(m.author)) * (x<2))

    if "$victim" in (m.content.lower()):
        if has_permission(m.author,"move_members"):
            for k in m.mentions:
                await k.move_to(m.author.guild.get_channel(369161932730662922))
        else:
            await m.channel.send(name(m.author)+" tu n'as pas la permission")
    if "$kick" in (m.content.lower()):
        if has_permission(m.author,"move_members"):
            for k in m.content.split("$kick")[-1].split(" "):
                print("p^pppp")
                print(k)
                print("ppppp")
                member = m.guild.get_member_named(k)
                print("mmmmmmm")
                print(member)
                print("mmmmm")
                 
                if member:
                    await member.move_to(m.author.guild.get_channel(369161932730662922))
        else:
            await m.channel.send(name(m.author)+" tu n'as pas la permission")
    # if "$mute" in (m.content.lower()):
    #     if has_permission(m.author,"mute_members"):
    #         for k in m.mentions:
    #             await k.move_to()
    #     else:
    #         await m.channel.send(name(m.author)+" tu n'as pas la permission")



    if "$p" in (m.content):
        end = m.content.split("$p")
        if "-play" in end:
            pname = end.split("-play")
            pl=p.playlist()
            pid = pl.get_playlist(pname)
            pl.get_song_addr(pid)
            for k in pl:
                await m.channel.send("-q "+k)
    if "$dé" in(m.content):

        k=(m.content.split("$dé")[-1]).split("$")[0]
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
