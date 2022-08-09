import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

# Comando para pingar o bot
    @slash_command(name='ping', description='Ver o ping do bot!', guild_ids=[983506417292017704])
    async def ping(
        self,
        ctx:Interaction
    ):
        await ctx.response.send_message(f"Pong {round(self.client.latency * 1000)}ms ! 🏓")

def setup(client):
    client.add_cog(Ping(client))