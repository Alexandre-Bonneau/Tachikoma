
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

async def message_function(m):
    if message.content.startswith("$ask"):
        prompt = message.content[len("$ask "):]
        if not prompt:
            await message.channel.send("Please provide a question.")
            return

        await message.channel.send("Thinking... 🤖")
        response = call_together_ai(prompt)
        await message.channel.send(response)

    if (m.author == 880383298512228373):
        return
    ret_value = []
    if "j'ai faim" in(m.content.lower()):
        await m.channel.send("T'as perdu : " +name(m.author))

    if "bonjour" in(m.content.lower() ) or "jour" == m.content.lower():

        await m.channel.send("Bonjour " +name(m.author) )
    if "$id" in(m.content.lower() ):

        await m.channel.send("L'id de " +name(m.author) +" est: "+ str(m.author.id) )
        #await m.channel.send(str(m.author in m.guild.get_role(643923862714712097).members))


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
            for k in m.content.split("$kick")[-1].split(" ")[-1]:
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
        print("p")
        end = m.content.split("$p")[-1]
        if "-play" in end:
            print("-p")
            print(end)
            pname = end.split("-play")[-1].split(' ')[-1]
            print(pname)
            pl=p.playlist()
            pid = pl.get_playlist(pname)
            print(pid)
            plist = pl.get_song_addr(pid)
            for k in plist:
                await m.channel.send("-q "+k)
    if "$dé" in(m.content):

        k=(m.content.split("$dé")[-1]).split("$")[0]
        rd = -1
        try:
            value = int(k)

            if value<=0:
                    await m.channel.send("Les dés sont des entiers positifs")
            else:
                rd = random.randint(1,value)
                if value == 10 :
                    rd -=1
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
    if "$md" in(m.content):

        #nb = eval((m.content.split("$md")[-1]))
        dicecollist = (m.content.split("$md")[1]).split(' ')
        dicelist =[]
        nmdice = 1
        for i in dicecollist:
            if len(i)>0:
                dicelist.append(i)
        for i in dicelist:
            for j in eval(i[0]):
                rd = random.randint(1,6)
                await m.channel.send("Dé n°"+str(nmdice) +" : "+i[1])
                if i[1]=="J":
                    if  rd<=4:
                        await m.channel.send(":crossed_swords:")
                    if rd==5:
                        await m.channel.send(":crossed_swords: :crossed_swords: :boom:")
                    if rd==6:
                        await m.channel.send(":o:")
                if i[1]=="R":
                    if rd<=2:
                        await m.channel.send(":crossed_swords:")
                    if rd>2 and rd<=4:
                        await m.channel.send(":crossed_swords: :crossed_swords: :boom:")
                    if rd ==5:
                        await m.channel.send(":crossed_swords: :crossed_swords: :crossed_swords: :diamond_shape_with_a_dot_inside:")
                    if rd ==6:
                        await m.channel.send(":o:")
                if i[1]=="B":
                    if rd<=3:
                        await m.channel.send(":shield:")
                    if rd==4:
                        await m.channel.send(":shield: :shield: :boom:")
                    if rd >=5:
                        await m.channel.send(":o:")

                if i[1]=="G":
                    if rd<=2:
                        await m.channel.send(":shield: :shield: :boom:")
                    if rd==3:
                        await m.channel.send(":shield:")
                    if rd==4:
                        await m.channel.send(":shield: :shield:  :shield: :diamond_shape_with_a_dot_inside:")
                    if rd >=5:
                        await m.channel.send(":o:")

                nmdice+=1
    if "$roll" in (m.content):
        message=(m.content.split("$roll")[-1])
        id = m.author.id
        value = jDR_Data.roll(message,id)
        for i in value:
            await m.channel.send(i)
    if "$reboot" in (m.content):
        id=m.author.id
        if  m.channel.send(str(m.author in m.guild.get_role(643923862714712097).members)):
            os.system("reboot")

    if "ping" in (m.content) and m.author.id != 203619925179236352:
        await m.channel.send("pong")
 #   if "$attest" in (m.content):
 #       id = m.author.id
 #       value = attest_class.send(id)
 #       if m.author.dm_channel == None:
 #           await m.author.create_dm()
 #       file = discord.File(value, filename="attestation.pdf")
 #       # embed = discord.Embed()
 #       # embed.set_image(url="attachment://image.pdf")
 #       await m.author.dm_channel.send(file=file)
 #       await m.channel.send("attestation générée et envoyée en MP")

    return 0
