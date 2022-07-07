from turtle import color
import nextcord, os
from nextcord import slash_command, SlashOption, Interaction, Embed, SelectOption, ui
from nextcord.ext import commands
from nextcord.ui import Button, View
import config
import asyncio

class RegisterModal(ui.Modal):
    def __init__(self):
        super().__init__('📝 Realizar Cadastro de Clan')
        
        self.emClan = ui.TextInput(label = "Nome do Clan", min_length= 1, max_length= 20, required= True, placeholder=" Admins ", style = nextcord.TextInputStyle.short)
        self.add_item(self.emClan)

        self.emName1 = ui.TextInput(label = "Nome do Integrante", min_length= 3, max_length= 35, required= True, placeholder="Mestre da Noite", style = nextcord.TextInputStyle.short)
        self.add_item(self.emName1)
        
        self.emID1 = ui.TextInput(label = "SteamID do Integrante", min_length= 17, max_length= 17, required= True, placeholder="76569811000028712", style = nextcord.TextInputStyle.short)
        self.add_item(self.emID1)

        self.emName2 = ui.TextInput(label = "Nome do Integrante", min_length= 3, max_length= 35, required= True, placeholder="MSS", style = nextcord.TextInputStyle.short)
        self.add_item(self.emName2)
        
        self.emID2 = ui.TextInput(label = "SteamID do Integrante", min_length= 17, max_length= 17, required= True, placeholder="7656721000069836", style = nextcord.TextInputStyle.short)
        self.add_item(self.emID2)
        
    async def callback(self, interaction: Interaction):
        emclan = self.emClan.value
        emName1 = self.emName1.value
        emID1 = self.emID1.value
        emName2 = self.emName2.value
        emID2 = self.emID2.value
        

        embed = Embed(title="**RELATÓRIO DE REGISTRO 📝**" ,colour=0x5865F2)
        embed.add_field(name='**NOME DO CLAN:**', value=f"{emclan}", inline=False)
        embed.add_field(name='**INTEGRANTE:**', value=f"{emName1}", inline=False)
        embed.add_field(name='**STEAMID:**', value=f"{emID1}", inline=False)
        embed.add_field(name='**INTEGRANTE:**', value=f"{emName2}", inline=False)
        embed.add_field(name='**STEAMID:**', value=f"{emID2}", inline=False)
        await interaction.send(embed=embed)
        

class RegisterClan(ui.View):  # Botao de Atendimento
    def __init__(self):
        super().__init__(timeout=None)
        self.value=None
        self.colour = 0x5865F2
 
    @nextcord.ui.button(
        style= nextcord.ButtonStyle.blurple,
        label="📝 Cadastrar Clan",
        custom_id="RegisterClan:callback",
     )
    async def callback(self,button:nextcord.ui.button, interaction: Interaction):
        self.value = True
        self.stop()
        await interaction.response.send_modal(RegisterModal())



class FormRegister(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.colour = 0x5865F2
        
    @commands.Cog.listener()    
    async def on_ready(self): 
        if not self.client.persistent_views_added: 
                self.client.add_view(RegisterClan())
                self.client.persistent_views_added = True
    @slash_command(name = 'form', description='Form',guild_ids=[config.guild_id], default_member_permissions=8)
    async def setup(self, interaction: Interaction):
        embed = Embed(title="Central de Registro",
                      description='Nessa seção, você pode registrar seu clan(dupla), implementamos esse sistema para tentar controlar alianças e teaming. Agradecemos a compreensão de todos! 😉', 
                      colour=self.colour)
        
        embed.add_field(name='⠀⠀⠀⠀⠀⠀⠀',
                        value='Para evitar problemas, leia as opções com atenção e revise os dados antes de enviar. caso preencha algo errado chame alguem de nossa equipe!')
        embed.set_image(url='https://i.imgur.com/ea6mqGg.png')
        await interaction.response.send_message('Comando executado com sucesso!', ephemeral=True)
        await interaction.channel.send(embed=embed, view=RegisterClan())
        
        
def setup(client):
    client.add_cog(FormRegister(client))
