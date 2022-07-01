import nextcord, config, main
from nextcord import slash_command, Interaction
from nextcord.ext import commands
from main import *

class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client

# Create a Log on message edit
@bot.event
async def on_message_edit(message_before, message_after):
    if message_before.author.bot:
        return
    guild = bot.get_guild(config.guild_id)
    channel = guild.get_channel(config.logs_channel_id)
    await channel.send(f"📝 **{message_before.author.mention}** editou o seguinte mensagem: \n{message_before.content}")

def setup(client):
    client.add_cog(Logs(client))