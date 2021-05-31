from discord.ext import commands

#Cog_Extension 繼承 commands.cog的類別
class Cog_Extension(commands.Cog):
    #初始化
    #bot 是Cog_extension的一個屬性
    #這裡的bot是作為引數傳入
    def __init__(self, bot):
        self.bot = bot