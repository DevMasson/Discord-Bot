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
        if self.values[0] in ["atendimento", "sugestao", 'compras']:
            await interaction.response.send_message("Clique abaixo para criar um ticket",ephemeral=True, view=CreateTicket())
        elif self.values[0] == 'denuncia':
            await interaction.response.send_message('Para fazer uma denúncia, vamos precisar do **Motivo da denúncia, Autores do ocorrido e Provas.**\n*Lembrando que denúncias por teaming somente por videos.*\n\nPara prosseguir com sua denúncia, crie um ticket abaixo.', ephemeral=True, view=CreateTicket())
class DropdownView(ui.View):
    def __init__(self): 
        super().__init__(timeout=None)

        self.add_item(Dropdown())
class CreateTicket(ui.View):
    def __init__(self):
        super().__init__(timeout=300)

    @nextcord.ui.button(label='Abrir Ticket',style=nextcord.ButtonStyle.blurple,emoji="➕")
    async def confirm(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        self.value = True
        self.stop()

        ticket = None
        for thread in interaction.channel.threads:
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(ephemeral=True, content="Você já tem um atendimento em andamento!")
                    return

        if ticket != None:
            await ticket.locked(False)
            await ticket.edit(name=f"{interaction.user.name} ({interaction.user.name})",auto_archive_duration=10080,invitable=False)

        else:
            ticket = await interaction.channel.create_thread(name=f"{interaction.user.name} ({interaction.user.name})",auto_archive_duration=10080)
            await ticket.edit(invitable=False)

        await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")
        await ticket.send(f"📩  **|** {interaction.user.mention} ticket criado! Envie todas as informações possíveis sobre seu caso e aguarde até que um atendente responda.\n\nApós a sua questão ser sanada, você pode usar `/fecharticket` para encerrar o atendimento!\n\n <@&{config.owner_roleID}>, <@&{config.admin_roleID}>")

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
    async def _fecharticket(interaction: Interaction):
        mod = interaction.guild.get_role(config.admin_roleID)
        if str(interaction.user.id) in interaction.channel.name or mod in interaction.author.roles:
            await interaction.response.send_message(f"O ticket foi arquivado por {interaction.user.mention}, obrigado por entrar em contato!")
            await interaction.channel.edit(archived=True)
        else:
            await interaction.response.send_message("Isso não pode ser feito aqui...")


def setup(client):
    client.add_cog(Ticket(client))








