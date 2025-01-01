import sys
sys.path.append("/Users/giorgias/Library/Mobile Documents/com~apple~CloudDocs/Documents/Test_Github/commands")
import discord
import config
from discord.ext import commands
from commands.quiz_commands import quizCommands
from commands.database import Score


intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Hello, your Bot works")
    try:
        await bot.add_cog(quizCommands(bot))
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


bot.run(config.token)