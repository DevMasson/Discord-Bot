import nextcord, os, main, asyncio
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType
from nextcord.ext import commands
from main import *

class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.colour = 0x4555ff

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(config.guild_id)
    channel = guild.get_channel(config.welcome_channel_id)
    rules = guild.get_channel(config.rules_channel_id)
    msg = await channel.send(f"🎉 **Bem-Vindo {member.mention} ao servidor!** \n➥ Leia as regras em: {rules.mention} \n➥ Você é o **{guild.member_count}** membro aqui!")
    await member.send(f"Bem-Vindo {member.mention} ao **{guild.name}!** Melhor servidor de **V RISING** do Brasil! 🍻")
    await asyncio.sleep(30)
    await msg.delete()

def setup(client):
    client.add_cog(Welcome(client))