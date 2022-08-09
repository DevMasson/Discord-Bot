import nextcord, os, main
from nextcord import slash_command, Interaction, Embed
from nextcord.ext import commands
from main import * 

class ReloadCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.colour = 0x4555ff

# Comando que recarrega as configurações do bot 
    @slash_command(name='reload', description='recarrega os cogs!', guild_ids=[983506417292017704], default_member_permissions=8)
    async def reload(self, ctx:Interaction):
        embed = Embed(title="**CONFIGURAÇÕES RECARREGADAS** <:1520blurplesettings:986095370922762300> " ,colour=4092125, description="Os comandos foram atualiados!! <:rules:983841920092614677>")
        for fn in os.listdir('./cogs'):
                if fn.endswith('.py'):
                    bot.unload_extension(f'cogs.{fn[:-3]}')
                    bot.load_extension(f"cogs.{fn[:-3]}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ReloadCommand(client))