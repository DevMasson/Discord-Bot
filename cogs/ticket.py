import nextcord, os, main
from nextcord import slash_command, Interaction, Embed, SelectOption, ui
from nextcord.ext import commands
from main import * 

class Ticket(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.colour = 0x4555ff

class Dropdown(nextcord.ui.Select):
    def __init__(self):
        options = [
            SelectOption(value="atendimento",label="Atendimento", emoji="📨"),
            SelectOption(value="denuncia",label="Denúncia", emoji="🚨"),
            SelectOption(value="sugestao",label="Sugestão", emoji="✅"),
        ]
        super().__init__(
            placeholder="Selecione uma opção...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="persistent_view:dropdown_help"
        )
    async def callback(self, interaction: Interaction):
        if self.values[0] in ["atendimento", "denuncia", "sugestao"]:
            await interaction.response.send_message("Clique abaixo para criar um ticket",ephemeral=True,view=CreateTicket())

class DropdownView(ui.View):
    def __init__(self): 
        super().__init__(timeout=None)

        self.add_item(Dropdown())

class CreateTicket(ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value=None

    @nextcord.ui.button(label="Abrir Ticket",style=nextcord.ButtonStyle.blurple,emoji="➕")
    async def confirm(self,interaction: Interaction, button: ui.Button):
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

        if ticket is None:
            ticket = await interaction.channel.create_thread(name=f"{interaction.user.name} ({interaction.user.id})",auto_archive_duration=10080)#,type=discord.ChannelType.public_thread)
            await ticket.edit(invitable=False)

        else:
            await ticket.unarchive()
            await ticket.edit(name=f"{interaction.user.name} ({interaction.user.id})",auto_archive_duration=10080,invitable=False)
        await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")
        await ticket.send(f"📩  **|** {interaction.user.mention} ticket criado! Envie todas as informações possíveis sobre seu caso e aguarde até que um atendente responda.\n\nApós a sua questão ser sanada, você pode usar `/fecharticket` para encerrar o atendimento!")

    async def setup_hook(self) -> None:
        self.add_view(DropdownView())

@slash_command(guild_ids=config.guild_id, name = 'setup', description='Setup', default_member_permissions=8)
async def setup(interaction: Interaction):
    await interaction.response.send_message("Mensagem do painel",view=DropdownView()) 

@slash_command(guild_ids=config.guild_id, name="fecharticket",description='Feche um atendimento atual.', default_member_permissions=8)
async def _fecharticket(interaction: nextcord.Interaction):
    mod = interaction.guild.get_role(config.mod_role_id)
    if str(interaction.user.id) in interaction.channel.name or mod in interaction.author.roles:
        await interaction.response.send_message(f"O ticket foi arquivado por {interaction.user.mention}, obrigado por entrar em contato!")
        await interaction.channel.edit(archived=True)
    else:
        await interaction.response.send_message("Isso não pode ser feito aqui...")

def setup(client):
    client.add_cog(Ticket(client))