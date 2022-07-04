import nextcord, config, os, asyncio
from nextcord.ext import commands
from nextcord import Object
from cogs.ticket import DropdownView


class Bot(commands.Bot): 
     def __init__(self, *args, **kwargs): 
         super().__init__(*args, **kwargs) 
         self.persistent_views_added = False

intents = nextcord.Intents.default()
intents.members = True
bot = Bot(command_prefix='$', intents=intents)

# class client(nextcord.Client):
#     def __init__(self):
#         super().__init__(intents=nextcord.Intents.default())
#         self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma ve

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await bot.change_presence(activity=nextcord.Streaming(name="Melhor Servidor Brasileiro!", url='https://www.twitch.tv/uno2k19'))

    # if not self.synced:
    #     await bot.sync(guild = Object(id=config.guild_id))
    #     self.synced = True
    print("----------------------------")
    print(f"{bot.user} is online...")
    print("----------------------------")
    

for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f"cogs.{fn[:-3]}")

bot.run(config.TOKEN)