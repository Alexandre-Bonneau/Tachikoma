import discord
import random
import socket  # À placer en haut du fichier si pas déjà importé
import subprocess

def get_public_ip():
    try:
        result = subprocess.run(
            ["curl", "-4", "ifconfig.me"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Erreur : {e}"
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("1.1.1.1", 80))  # connexion fictive pour déterminer l'interface utilisée
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return f"Erreur locale : {e}"


# Utility functions
def name(author):
    """ Returns the best possible display name for a user. """
    return author.nick if isinstance(author, discord.Member) and author.nick else str(author).split("#")[0]

def has_permission(member, permission):
    """ Checks if a user has a specific permission. """
    return any(getattr(role.permissions, permission, False) for role in member.roles)

# Main message handler function
async def message_function(m, call_together_ai):
    """ Handles messages, including AI and custom commands. """

    content_lower = m.content.lower()  # Correct usage of 'm'

    # AI Chat Command
    if content_lower.startswith("$ask"):
        prompt = m.content[len("$ask "):].strip()
        if not prompt:
            return "Please provide a question."

        await m.channel.send("Thinking... 🤖")
        return call_together_ai(prompt)

    # Basic Auto-Responses (Ensure 'm' is used)
    responses = {
        "j'ai faim": f"T'as perdu : {name(m.author)}",
        "bonjour": f"Bonjour {name(m.author)}",
        "jour": f"Bonjour {name(m.author)}",
        "bonne nuit": random.choice(["Nenuit", "Bonne nuit", "See you space cowboy"]) + f" {name(m.author)}",
        "nenuit": random.choice(["Nenuit", "Bonne nuit", "See you space cowboy"]) + f" {name(m.author)}",
        "ping": "pong"
    }

    if content_lower in responses:# and m.author.id != 203619925179236352:
        return responses[content_lower]

    # Display user ID
    if content_lower == "$id":
        return f"L'ID de {name(m.author)} est: {m.author.id}"
    # IP command - only for you
    
    if content_lower == "$ip" and m.author.id == 227088616575205376:
        local_ip = get_local_ip()
        public_ip = get_public_ip()
        return f"🌐 IP publique : {public_ip} -p 61810 \n🏠 IP locale : {local_ip}"

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
