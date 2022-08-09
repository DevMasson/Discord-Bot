import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext import commands

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

# Comando para Kickar um usuário
    @slash_command(name='kick', description='Kickar um usuário', guild_ids=[983506417292017704], default_member_permissions=8)
    async def kick(
        self,
        ctx:Interaction,
        member: nextcord.Member = nextcord.SlashOption(name='usuário', description='Selecione um usuário'),
        reason: str = nextcord.SlashOption(name='motivo', description='Escreva o motivo', required=False)
    ):
        if not reason: reason="No reason"
        await member.kick(reason=reason)
        await ctx.response.send_message(f"{member} has been kicked by {ctx.user.mention} for {reason}")

def setup(client):
    client.add_cog(Kick(client))