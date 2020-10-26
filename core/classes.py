import discord
from discord.ext import commands

#Cog_Extension 繼承 commands.cog的類別
class Cog_Extension(commands.Cog):
    #初始化
    def __init__(self, bot):
        self.bot = bot
        #作為引數傳入