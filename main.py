import nextcord, config, os, asyncio
from nextcord.ext import commands
from nextcord import Embed, Interaction, slash_command

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print("----------------------------")
    print(f"{bot.user} is online...")
    print("----------------------------")

for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f"cogs.{fn[:-3]}")

bot.run(config.TOKEN)