# import keep_alive
import json
import os
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
BOT_ID=os.getenv('PUBLIC_KEY')
GUILD_ID=os.getenv('GUILD_ID')
BOT_PUBLIC_KEY = os.getenv('PUBLIC_KEY')

#Discord.py 1.5 新增Intents selective receive event
#https://discordpy.readthedocs.io/en/latest/intents.html#member-intent
intents = discord.Intents.all()

#('File name', 'mode', encoding)
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

#Build Entity
bot = commands.Bot(command_prefix='[',intents = intents)
slash = SlashCommand(bot, override_type = True, sync_commands=True)

#Bot Ready
@bot.event
async def on_ready():
    channel = bot.get_channel(int(jdata['Bot_channel']))
    await channel.send('OuO Bot is now Online')
    print("\\OuO Bot is online/")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print(f'Extension {extension} Loaded!')
    await ctx.send(F'Extension {extension} Loaded!')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print(f'Extension {extension} Unloaded!')
    await ctx.send(F'Extension {extension} Unloaded!')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    print(f'Extension {extension} Reloaded!')
    await ctx.send(F'Extension {extension} Reloaded!')

#Load Error Handler
bot.load_extension(f'core.error')

#Load Default Extension
for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and not(filename.startswith('__')):
        #filename[:-3] 省略後三字 (.py)
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Imported {filename}!')

#Inside Json, the arrengement of data is in the form of dictionary
#Which means every data have a corrspond key
if __name__ == "__main__":
    # keep_alive.keep_alive()
    bot.run(TOKEN)