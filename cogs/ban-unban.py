import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

# Comando para banir um usuário
    @slash_command(name='ban', description='Bane um usuário', guild_ids=[983506417292017704], default_member_permissions= 8)
    async def ban(
        self,
        ctx:Interaction,
        member: nextcord.Member = nextcord.SlashOption(name='usuário', description='Selecione um usuário'),
        reason: str = nextcord.SlashOption(name='motivo', description='Escreva o motivo', required=False)
    ):
        if not reason: reason = "Sem Motivo"
        await member.ban(reason=reason)
        await ctx.response.send_message(f"{member} foi banido por {ctx.user.mention} por {reason}")

# Comando para desbanir um usuário
    @slash_command(name='unban', description='Desbanir um usuário', guild_ids=[983506417292017704], default_member_permissions= 8)
    async def unban(
        self,
        ctx:Interaction,
        member: nextcord.User = nextcord.SlashOption(name='usuário', description='Selecione um usuário')
    ): 
        await ctx.guild.unban(user=member)
        await ctx.response.send_message(f"{member} foi desbanido por {ctx.user.mention}.")

def setup(client):
    client.add_cog(Ban(client))