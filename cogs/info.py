import nextcord, os, main, datetime, asyncio
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType, ui
from nextcord.ext import commands
from main import *
from datetime import date, timedelta


class Infos(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.colour = 0x4555ff

            
    @slash_command(name='server-info', description='Server information!', guild_ids=[config.guild_id])
    async def server_info(self, ctx: Interaction):
        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
        embed = Embed(colour=self.colour)
        embed.set_author(name=ctx.guild)
        embed.add_field(name='Owned by', value=ctx.guild.owner)
        embed.add_field(name='Owner id', value=ctx.guild.owner_id)
        embed.add_field(name='Verification Level', value=ctx.guild.verification_level)
        embed.add_field(name='Members', value=ctx.guild.member_count)
        embed.add_field(name='Bots', value=list_of_bots)
        embed.add_field(name='Top role', value=ctx.guild.roles[-2])
        embed.add_field(name='Guild created', value=ctx.guild.created_at)
        await ctx.response.send_message(embed=embed)
        
        

    @slash_command(name='user-info', description='See information of the mentioned user', guild_ids=[config.guild_id])
    async def user_info(self, ctx, user: Member):
        if user is None:
            user = ctx.user
        
        roles = [role.name for role in user.roles]
        userid = ctx.user.id

        embed = Embed(colour=self.colour)
        embed.set_author(name=f"Informações do usuário -> {user}")
        embed.set_thumbnail(url=user.avatar)
        embed.add_field(name="Nome de Usuário", value=user.display_name, inline=False)
        embed.add_field(name="ID", value=user.id, inline=False)
        embed.add_field(name="Entrou no servido em:", value=user.joined_at.strftime("%d/%m/%Y %H:%M"), inline=False)
        embed.add_field(name=f"Cargos: ({len(roles)})", value=", ".join(roles), inline=False)
        embed.add_field(name="⠀⠀⠀⠀⠀⠀",value=f"Solicitado por <@{userid}>")
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Infos(client))