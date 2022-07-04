import nextcord, os, main
from nextcord import slash_command, SlashOption, Interaction, Embed, SelectOption, ui
from nextcord.ext import commands
from nextcord.ui import Button, View
from main import * 




class Dropdown(nextcord.ui.Select):
    def __init__(self):
        options = [
            SelectOption(label="Atendimento", value="atendimento", emoji="📨"),  
            SelectOption(label="Denúncia", value="denuncia", emoji="🚨"),
            SelectOption(label="Sugestão", value="sugestao", emoji="💡"),
            SelectOption(label="Compras", value="compras", emoji="🛒"),
        ]
        super().__init__(
            placeholder="Selecione uma opção...",
            min_values=1,
            max_values=1,
            options=options, 
            custom_id="persistent_view:dropdown_help"
        )
        
    async def callback(self, interaction: Interaction):
        if self.values[0] == "atendimento":
            await interaction.response.send_message("Clique abaixo para criar um ticket",ephemeral=True, view=StartTicket())
        
        elif self.values[0] == "sugestao":
            await interaction.response.send_message("Clique abaixo para criar um ticket",ephemeral=True, view=SuggestionTicket())
            
        elif self.values[0] == "compras":
            await interaction.response.send_message("Clique abaixo para criar um ticket",ephemeral=True, view=BuyButton())
            
        elif self.values[0] == 'denuncia':
            await interaction.response.send_message('Para fazer uma denúncia, vamos precisar do **Motivo da denúncia, Autores do ocorrido e Provas.**\n*Lembrando que denúncias por teaming somente por videos.*\n\nPara prosseguir com sua denúncia, crie um ticket abaixo.', ephemeral=True, view=ReportTicket())
class DropdownView(ui.View):
    def __init__(self): 
        super().__init__(timeout=None)
        self.add_item(Dropdown())


class StartTicket(ui.View):  # Botao de Atendimento
    def __init__(self):
        super().__init__(timeout=None)
        self.value=None
        self.colour = 0x4555ff

        
        
    @nextcord.ui.button(
        style= nextcord.ButtonStyle.blurple,
        label="➕Abrir Ticket",
        custom_id="StartTicketButton:callback",
     )
    async def callback(self,button:nextcord.ui.button, interaction: Interaction):
        self.value = True
        self.stop()


        ticket = True
        for thread in interaction.channel.threads:
            if f"{interaction.user.name}" in thread.name:
                if thread.archived:
                    ticket = True

                else:
                    ticket = False
                    await interaction.response.send_message(ephemeral=True, content="Você já tem um pedido de atendimento em andamento!")

                    return


        if ticket == True:
            ticket = await interaction.channel.create_thread(name=f"Atendimento de {interaction.user.name}",auto_archive_duration=10080)
            await ticket.edit(invitable=False)

            await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")
            embed = Embed(title="📩  **|** Seu foi ticket criado!",
                      description='Envie todas as informações possíveis sobre seu caso e aguarde até que um atendente responda.\n\nApós a sua questão ser sanada, você pode usar o botão abaixo para encerrar o atendimento!"', 
                      colour=self.colour)

            await ticket.send(embed=embed, view=CloseButton())
            await ticket.send(f"{interaction.user.mention}")
        
        




class ReportTicket(ui.View):  # Botao de Report
    def __init__(self):
        super().__init__(timeout=None)
        self.value=None
        self.colour = 0x5c0412

        
        
    @nextcord.ui.button(
        style= nextcord.ButtonStyle.blurple,
        label="🚨Abrir Denúncia",
        custom_id="ReportTickerButton:callback",
     )
    async def callback(self,button:nextcord.ui.button, interaction: Interaction):
        self.value = True
        self.stop()


        ticket = True
        for thread in interaction.channel.threads:
            if f"Ticket de Denúncia de {interaction.user.name}" in thread.name:
                if thread.archived:
                    ticket = True

                else:
                    ticket = False
                    await interaction.response.send_message(ephemeral=True, content="Você já tem um ticket de denúncia em andamento!")

                    return


        if ticket == True:
            ticket = await interaction.channel.create_thread(name=f"Ticket de Denúncia de {interaction.user.name}",auto_archive_duration=10080)
            await ticket.edit(invitable=False)

            await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")
            embed = Embed(title="🚨  **|** Seu pedido de Denúncia foi aberto!",
                      description='Envie todas as informações e provas possíveis sobre seu caso e aguarde até que um atendente responda.\n\nApós a sua questão ser sanada, você pode usar o botão abaixo para encerrar o atendimento!"', 
                      colour=self.colour)

            await ticket.send(embed=embed, view=CloseButton())
            await ticket.send(f"{interaction.user.mention}")


class SuggestionTicket(ui.View):  # Botao de Sugestão
    def __init__(self):
        super().__init__(timeout=None)
        self.value=None
        self.colour = 0x9c8203


        
        
    @nextcord.ui.button(
        style= nextcord.ButtonStyle.blurple,
        label="💡 Indicar Sugestão",
        custom_id="SuguestaoButton:callback",
     )
    async def callback(self,button:nextcord.ui.button, interaction: Interaction):
        self.value = True
        self.stop()


        ticket = True
        for thread in interaction.channel.threads:
            if f"Sugestão de {interaction.user.name}" in thread.name:
                if thread.archived:
                    ticket = True

                else:
                    ticket = False
                    await interaction.response.send_message(ephemeral=True, content="Você já tem um ticket de sugestão em andamento!")

                    return


        if ticket == True:
            ticket = await interaction.channel.create_thread(name=f"Sugestão de {interaction.user.name}",auto_archive_duration=10080)
            await ticket.edit(invitable=False)

            await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket de sugestão para você! {ticket.mention}")
            embed = Embed(title="💡   **|** Seu pedido sugestão foi aberto!",
                      description='Envie todas as informações possíveis sobre sua sugestão e aguarde até que um atendente responda.\n\nApós a sua questão ser sanada, você pode usar o botão abaixo para encerrar o atendimento!"', 
                      colour=self.colour)

            await ticket.send(embed=embed, view=CloseButton())
            await ticket.send(f"{interaction.user.mention}")



class BuyButton(ui.View):  # Botao de Sugestão
    def __init__(self):
        super().__init__(timeout=None)
        self.value=None
        self.colour = 0x125200


    @nextcord.ui.button(
        style= nextcord.ButtonStyle.blurple,
        label="🛒 Realizar uma Compra",
        custom_id="BuyButton:callback",
     )
    async def callback(self,button:nextcord.ui.button, interaction: Interaction):
        self.value = True
        self.stop()


        ticket = True
        for thread in interaction.channel.threads:
            if f"Carrinho de {interaction.user.name}" in thread.name:
                if thread.archived:
                    ticket = True

                else:
                    ticket = False
                    await interaction.response.send_message(ephemeral=True, content="Você já tem um carrinho aberto!")

                    return


        if ticket == True:
            ticket = await interaction.channel.create_thread(name=f"Carrinho de {interaction.user.name}",auto_archive_duration=10080)
            await ticket.edit(invitable=False)

            await interaction.response.send_message(ephemeral=True,content=f"Criei um carrinho para você! {ticket.mention}")
            embed = Embed(title="🛒   **|** Seu pedido carrinho foi aberto!",
                      description='Envie todas as informações possíveis sobre o que voce quer adquirir e aguarde até que um atendente responda.\n\nApós a sua questão ser sanada, você pode usar o botão abaixo para encerrar o atendimento!"', 
                      colour=self.colour)

            await ticket.send(embed=embed, view=CloseButton())
            await ticket.send(f"{interaction.user.mention}")

            print(interaction.data)
class BuyButton(ui.View):  # Botao de Sugestão
    def __init__(self):
        super().__init__(timeout=None)
        self.value=None
        self.colour = 0x125200


    @nextcord.ui.button(
        style= nextcord.ButtonStyle.blurple,
        label="🛒 Realizar uma Compra",
        custom_id="BuyButton:callback",
     )
    async def callback(self,button:nextcord.ui.button, interaction: Interaction):
        self.value = True
        self.stop()


        ticket = True
        for thread in interaction.channel.threads:
            if f"Carrinho de {interaction.user.name}" in thread.name:
                if thread.archived:
                    ticket = True

                else:
                    ticket = False
                    await interaction.response.send_message(ephemeral=True, content="Você já tem um carrinho aberto!")

                    return


        if ticket == True:
            ticket = await interaction.channel.create_thread(name=f"Carrinho de {interaction.user.name}",auto_archive_duration=10080)
            await ticket.edit(invitable=False)

            await interaction.response.send_message(ephemeral=True,content=f"Criei um carrinho para você! {ticket.mention}")
            embed = Embed(title="🛒   **|** Seu pedido carrinho foi aberto!",
                      description='Envie todas as informações possíveis sobre o que voce quer adquirir e aguarde até que um atendente responda.\n\nApós a sua questão ser sanada, você pode usar o botão abaixo para encerrar o atendimento!"', 
                      colour=self.colour)

            await ticket.send(embed=embed, view=CloseButton())
            await ticket.send(f"{interaction.user.mention}")
            
            
            
class CloseButton(ui.View):  # Botao de Sugestão
    def __init__(self):
        super().__init__(timeout=None)
        self.value=None
        self.colour = 0x125200


    @nextcord.ui.button(
        style= nextcord.ButtonStyle.secondary,
        label="❌ Fechar",
        custom_id="CloseButton:callback",
        )
    async def callback(self,button:nextcord.ui.button, interaction: Interaction):
        self.value = True
        self.stop()

        if str(interaction.data):
            await interaction.response.send_message(ephemeral=True, content="Fechando ticket...")
            await asyncio.sleep(2)
            await interaction.followup.send(ephemeral=True, content=f"Ticket fechado por! {interaction.user.mention}")
            await interaction.channel.edit(archived=True)


async def setup_hook(self) -> None:
    self.add_view(DropdownView())


class Ticket(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.colour = 0x5865F2
        
    @slash_command(name = 'setup', description='Setup',guild_ids=[config.guild_id], default_member_permissions=8)
    async def setup(self, interaction: Interaction):
        channel = self.client.get_channel(983506417732452363) # TROCAR PARA CANAL DE SUPORTE
        embed = Embed(title="Central de Ajuda do Mestre da Noite",
                      description='Nessa seção, você pode tirar suas dúvidas, reportar jogadores, comprar vips ou entrar em contato com a nossa equipe do Mestre da Noite', 
                      colour=self.colour)
        
        embed.add_field(name='⠀⠀⠀⠀⠀⠀⠀',
                        value='Para evitar problemas, leia as opções com atenção e lembre-se de tentar pedir ajuda no chat, talvez um de nossos membros ou staffs te ajude. 😉')
        embed.set_image(url='https://i.imgur.com/ea6mqGg.png')
        await interaction.response.send_message('Comando executado com sucesso!', ephemeral=True)
        await interaction.channel.send(embed=embed)
        await channel.send(view=DropdownView()) 


    @slash_command(guild_ids=[config.guild_id], name="fecharticket",description='Feche um atendimento atual.')
    async def fecharticket(self, interaction: Interaction):
        await interaction.response.send_message(ephemeral=True, content="Fechando ticket...")
        await asyncio.sleep(2)
        await interaction.followup.send(ephemeral=True, content=f"Ticket fechado por! {interaction.user.mention}")
        await interaction.channel.edit(archived=True)



def setup(client):
    client.add_cog(Ticket(client))








