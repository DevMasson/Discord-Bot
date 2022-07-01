import nextcord, os, main, datetime, asyncio
from nextcord import Embed, Interaction, slash_command, Member, SlashOption, ChannelType, ui
from nextcord.ext import commands
from main import *
from datetime import date, timedelta

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.colour = 0x4555ff


    @slash_command(name='server-info', description='Server information!', guild_ids=[983506417292017704])
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


    @slash_command(name='user-info', description='See information of the mentioned user', guild_ids=[983506417292017704])
    async def user_info(self, ctx:Interaction, member: nextcord.Member = nextcord.SlashOption(name='member', description='Mention a user', required=False)):
        if not member:
            member = ctx.user
        
        date_format = "%a, %d %b %Y %i:%M %p"
        embed = Embed(colour=self.colour)
        embed.add_field(name='Name', value=member.name)
        embed.add_field(name='ID', value=member.id)
        embed.add_field(name='User joined at', value=member.joined_at.strftime(date_format))
        embed.add_field(name='Account age', value=member.created_at)
        await ctx.response.send_message(embed=embed)

    @slash_command(name='create-embed', description='Create embed.', guild_ids=[983506417292017704], default_member_permissions=8)
    async def embed_create(self, 
    ctx:Interaction,
    channel: nextcord.abc.GuildChannel = nextcord.SlashOption(channel_types=[ChannelType.text],name='channel', description='Please select a channel', required=False),
    author: str = nextcord.SlashOption(name='embed-author', description='Entre the author msg', required=False),
    author_icon: nextcord.Attachment = nextcord.SlashOption(name='embed-author-icon', description='Please select a image file', required=False),
    title: str = nextcord.SlashOption(name='embed-title', description='Entre title msg.', required=False),
    description: str = nextcord.SlashOption(name='embed-description', description='Entre description msg.', required=False),
    footer: str = nextcord.SlashOption(name='embed-footer', description='Entre footer msg.', required=False),
    footer_icon: nextcord.Attachment = nextcord.SlashOption(name='embed-footer-icon', description='Please select a image file for footer icon', required=False),
    image: nextcord.Attachment = nextcord.SlashOption(name='embed-image', description='Please select a image file for embed image', required=False),
    thumbnail: nextcord.Attachment = nextcord.SlashOption(name='embed-thumbnail', description='Please select a image file for embed thumbnail', required=False),
    colour: str = nextcord.SlashOption(name='embed-colour', description='Please provide a hex code', required=False)
    ):  # sourcery skip: low-code-quality
        embed = nextcord.Embed()
        if not channel:
            channel = ctx.channel
        if author is not None and author_icon is not None:
            embed.set_author(name=author, icon_url=author_icon)
        elif author is not None:
            embed.set_author(name=author)
        if title:
            embed.title=title
        if description:
            embed.description=description
        if footer_icon is not None:
            embed.set_footer(text=footer, icon_url=footer_icon)
        elif footer is not None:
            embed.set_footer(text=footer)
        if image:
            embed.set_image(url=image)
        if thumbnail:
            embed.set_thumbnail(url=thumbnail)
        if colour:
            embed.colour = int(f"0x{colour}", 16)
        if not author and not title and not description and not footer and not image and not thumbnail and not colour:
            await ctx.response.send_message("Please write any of these values", ephemeral=True)
        else:
            await channel.send(embed=embed)
            await ctx.response.send_message(f"Embed sent to {channel}")

    class PuniçãoModal(ui.Modal, title= "Relatório de Punição"):
        nome = ui.TextInput(label="Nome do usuário:", style = nextcord.TextInput.style.short, placeholder="Mestre da Noite", required=True)
        steamid = ui.TextInput(label="SteamID do usuário:", style = nextcord.TextInput.style.short, placeholder="7656981100002", required=True)
        motivos = ui.TextInput(label="Motivos da Punição:", style = nextcord.TextInput.style.short, placeholder="Teaming / Racismo / Hack", required=True)
        provas = ui.TextInput(label="Provas:", style = nextcord.TextInput.style.short, placeholder="Videos e Prints no Discord", required=True)
        punicao = ui.TextInput(label="Tempo da Punição:", style = nextcord.TextInput.style.short, placeholder="1", required=True)
        
        async def on_submit(self, ctx:Interaction):
            final = datetime.now() - timedelta(days=int(self.punicao))
            embed =   Embed(title="**RELATÓRIO DE PUNIÇÃO 📝**" ,colour=4092125)
            embed.add_field(name='**NOME:**', value=f"{self.nome}", inline=True)
            embed.add_field(name='**STEAMID:**', value=f"{self.steamid}", inline=True)
            embed.add_field(name='**MOTIVOS:**', value=f"{self.motivos}", inline=False)
            embed.add_field(name='**PROVAS:**', value=f"{self.provas}", inline=True)
            embed.add_field(name='**PUNIÇÃO:**', value=f"Tempo: {self.punicao} dia(s) \nInicio: {datetime.now()} \nFim: {final}", inline=True)
            await ctx.send(embed=embed)
            await ctx.response.send_message("Punição enviada com sucesso!")

    @slash_command(name='punição', description='Envia relatório de punição', guild_ids=[983506417292017704])
    async def punicao(ctx:Interaction):
        await ctx.response.send_modal(modal=PunicãoModal())



def setup(client):
    client.add_cog(Utility(client))