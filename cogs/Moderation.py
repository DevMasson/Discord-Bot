from distutils.log import error
import nextcord, asyncio
from nextcord import slash_command, Interaction
from nextcord.ext import commands

class Moderation(commands.Cog):
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


# Comando para limpar as mensagens
    @slash_command(name='clear', description='Limpar as mensagens', guild_ids=[983506417292017704], default_member_permissions= 8)
    async def clear(
        self,
        ctx:Interaction,
        amount: int = nextcord.SlashOption(name='quantidade', description='Quantidade de mensagens', required=False)
    ):
        if amount > 100:
            await ctx.response.send_message("Não é possível limpar mais de 100 mensagens.")
        await ctx.channel.purge(limit=amount)
        msg = await ctx.response.send_message(f"{ctx.user.mention} limpou {amount} mensagens.")
        await asyncio.sleep(3)
        await msg.delete()

def setup(client):
    client.add_cog(Moderation(client))