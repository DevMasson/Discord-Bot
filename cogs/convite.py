import nextcord
from nextcord import slash_command, Interaction, Embed
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

class Convite(commands.Cog):
    def __init__(self, client):
        self.client = client

# Comando que mostra o link de convite do servidor!
    @slash_command(name='convite', description='Mostra o link de convite do servidor', guild_ids=[983506417292017704])
    async def convite(self, ctx:Interaction):
        embed = Embed(title="<:external_link2:992246876948680784> **LINKS ÚTEIS**" ,colour=4092125, description="Informações relacionadas ao nosso servidor! 🇧🇷")
        embed.set_thumbnail("https://media.discordapp.net/attachments/983506417732452362/992217430539640943/LOGO_DISCORD_MESTRE_DA_NOITE.png?width=605&height=605")
        embed.add_field(name='_ _', value="<:discordround:983841913046179840> **[DISCORD](https://discord.gg/mestredanoite)**", inline=True)
        embed.add_field(name='_ _', value=":globe_with_meridians: **[SITE](https://v-rising.vercel.app)**", inline=True)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Convite(client))