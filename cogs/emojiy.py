import nextcord
from nextcord import slash_command, Interaction
from nextcord.ext import commands

class Emojify(commands.Cog):
    def __init__(self, client):
        self.client = client

# Emojify Command
    @slash_command(name='emoji', description='transforma texto em emoji', guild_ids=[983506417292017704])
    async def emojify(        
        self,
        ctx:Interaction,
        text: str = nextcord.SlashOption(name='texto', description='texto para ser transformado', required=True)
    ):
        emojis = []
        for s in text:
            if s.isdecimal():
                num2emo = {
                    "0": ":zero:", "1": ":one:", "2": ":two:", "3": ":three:", 
                    "4": ":four:", "5": ":five:", "6": ":six:", "7": ":seven:", 
                    "8": ":eight:", "9": ":nine:"}
                emojis.append(f":{num2emo(s)}:")
            elif s.isalpha():
                emojis.append(f":regional_indicator_{s.lower()}:")
            else: 
                emojis.append(s)
        await ctx.response.send_message(f"{' '.join(emojis)}")

def setup(client):
    client.add_cog(Emojify(client))