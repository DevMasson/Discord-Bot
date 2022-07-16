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
        
        self.emClan = ui.TextInput(label = "Nome do Clan", min_length= 3, max_length= 20, required= True, placeholder=" Admins ", style = nextcord.TextInputStyle.short)
        self.add_item(self.emClan)

        self.emName1 = ui.TextInput(label = "Nome do Primeiro Integrante", min_length= 3, max_length= 35, required= True, placeholder="Mestre da Noite", style = nextcord.TextInputStyle.short)
        self.add_item(self.emName1)
        
        self.emName2 = ui.TextInput(label = "Nome do Segundo Integrante", min_length= 3, max_length= 17, required= True, placeholder="MSS", style = nextcord.TextInputStyle.short)
        self.add_item(self.emName2)

        

        
    async def callback(self, interaction: Interaction):
        emclan = self.emClan.value
        emName1 = self.emName1.value
        emName2 = self.emName2.value

        
        # guild = self.client.get_guild(config.guild_id)
        # for member in guild.members:
        #     if emName1 in member.display_name:
        #         emName1 = member.id
        

        embed = Embed(title="**CLAN REGISTRADO ✅**" ,colour=0x5865F2)
        embed.add_field(name='**NOME DO CLAN:**', value=f"{emclan}", inline=False)
        embed.add_field(name='**INTEGRANTES:**', value=f"🧛🏻・{emName1}\n🧛🏻・{emName2}", inline=False)
        await interaction.channel.send(embed=embed)
        

class RegisterClan(ui.View):  
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
        await interaction.response.send_modal(RegisterModal())



class FormRegister(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.colour = 0x5865F2
        
    @commands.Cog.listener()    
    async def on_ready(self): 
        if not self.client.persistent_views_added:           
                self.client.persistent_views_added = True
    @slash_command(name = 'cadastrar', description='Cadastrar',guild_ids=[config.guild_id])
    async def cadastrar(self, interaction: Interaction):
        embed = Embed(title="Central de Registro",
                      description='Nessa seção, você pode registrar seu clan(trio), implementamos esse sistema para tentar controlar alianças e teaming. Agradecemos a compreensão de todos! 😉', 
                      colour=self.colour)
        
        embed.add_field(name='⠀⠀⠀⠀⠀⠀⠀',
                        value='Para evitar problemas, leia as opções com atenção e revise os dados antes de enviar. caso preencha algo errado chame alguem de nossa equipe!\n\nLembrando que o nome do seu personagem e seu nome do discord devem ser idênticos!')
        
        
        
        embed.set_image(url='https://i.imgur.com/T9kZhYr.png')
        await interaction.response.send_message(embed=embed, view=RegisterClan(), ephemeral=True)
        # await interaction.channel.send(embed=embed, view=RegisterClan())
        
        
def setup(client):
    client.add_cog(FormRegister(client))
