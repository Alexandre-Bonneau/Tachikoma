#anti spam/cooldown
import discord
import random
global test  = 0
def nosharp(str1):
    return str1.split("#")[0]

def name(author):
    if(type(author) is discord.user.User):
        return nosharp(str(author))
    if(type(author) is discord.member.Member):
        return author.nick
    return "noname"


def query(author):
    return

def message_function(m):

    ret_value = []
    print(m.content)
    if "j'ai faim" in(m.content.lower()):
        test+=1
        ret_value.append("T'as perdu : " +name(m.author))
    if "bonjour" in(m.content.lower()):
        ret_value.append("Bonjour : " +name(m.author))

    if "$dé" in(m.content):

        k=(m.content.split("$dé")[-1]).split("$")[0]
        int(k)
        rd = -1
        # try:
        value = int(k)

        if value<=0:
                ret_value.append("Les dés sont des entiers positifs")
        else:
            rd = random.randint(0,value-1)
            if((rd ==0 or rd ==9) and value ==10):
                rd2 = random.randint(0,value-1)
                rd = 10*rd+rd2
                if(rd>=96):
                    ret_value.append("Oh le critique de " + name(m.author))
                if(rd<=5):
                    ret_value.append( "Cheh, critique de " + name(m.author))
                    rd = "0"+str(rd)
            ret_value.append( rd)
        # except:
        #     ret_value.append( "Les dés sont des entiers positifs")

    return ret_value
