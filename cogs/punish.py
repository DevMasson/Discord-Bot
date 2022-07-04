import nextcord, os, main
from nextcord import slash_command, SlashOption, Interaction, Embed, SelectOption, ui
from nextcord.ext import commands
from nextcord.ui import Button, View
from datetime import datetime, timedelta, date
from main import * 



class PunishModal(ui.Modal):
    def __init__(self):
        super().__init__('🚨 Realizar uma Punição')

        self.emName = ui.TextInput(label = "Nome do usuário", min_length= 3, max_length= 30, required= True, placeholder="Mestre da Noite", style = nextcord.TextInputStyle.short)
        self.add_item(self.emName)
        
        self.emID = ui.TextInput(label = "SteamID", min_length= 17, max_length= 17, required= True, placeholder="76569811000028712", style = nextcord.TextInputStyle.short)
        self.add_item(self.emID)

        self.emReasons = ui.TextInput(label = "Motivos", min_length= 5, max_length= 30, required= True, placeholder="Teaming / Racismo / Hack", style = nextcord.TextInputStyle.short)
        self.add_item(self.emReasons)
        
        self.emEvidences = ui.TextInput(label = "Provas", min_length= 1, max_length= 124, required= True, placeholder="Videos e Prints no Discord", style = nextcord.TextInputStyle.short)
        self.add_item(self.emEvidences)
        
        self.emPunishment = ui.TextInput(label = "Punição", min_length= 1, max_length= 124, required= True, placeholder=" Dias / Permanente ", style = nextcord.TextInputStyle.short)
        self.add_item(self.emPunishment)
        
    async def callback(self, interaction: Interaction):
        # sourcery skip: use-datetime-now-not-today
   
        name = self.emName.value
        userid = self.emID.value
        reasons = self.emReasons.value
        evidences = self.emEvidences.value
        
        if self.emPunishment.value == "Permanente":
            punishment = 'Permanente'
        else:
            punishment = self.emPunishment.value
            finalDate = datetime.today() + timedelta(days=int(punishment))
            
        banDate = datetime.today().strftime('%d/%m/%Y')
        embed = Embed(title="**RELATÓRIO DE PUNIÇÃO 📝**" ,colour=0x5c0412)
        embed.add_field(name='**NOME:**', value=f"{name}", inline=False)
        embed.add_field(name='**STEAMID:**', value=f"{userid}", inline=False)
        embed.add_field(name='**MOTIVOS:**', value=f"{reasons}", inline=False)
        embed.add_field(name='**PROVAS:**', value=f"{evidences}", inline=False)
        if punishment == 'Permanente':
            embed.add_field(name='**PUNIÇÃO:**', value="Tempo: Permanente!", inline=False)
        else:
            embed.add_field(name='**PUNIÇÃO:**', value=f"Tempo: {punishment} dia(s) \n\nInicio: {banDate} \n\nFim: {finalDate.strftime('%d/%m/%Y')}", inline=False)

        await interaction.send(embed=embed)

        
class Punishment(commands.Cog):
    def __init__(self, client):
        
        self.client = client
        self.colour = 0x5c0412
        
    @slash_command(name = 'punir', description='Anunciar uma punição! ',guild_ids=[config.guild_id], default_member_permissions=8)
    async def punir(self, interaction: Interaction):
        await interaction.response.send_modal(PunishModal())
        
        
def setup(client):
    client.add_cog(Punishment(client))
    