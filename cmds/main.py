import discord
from discord.ext import commands
from core.classes import Cog_Extension

#main 繼承commands.cog類別
class Main(Cog_Extension):
    
    @commands.command()
    #ctx = context (上下文)
    #A:(上文) (user, id, user current server, user channel)
    #latency is float in second
    async def ping(self, ctx):
        await ctx.send(f'{round(bot.latency*1000)} (ms)')

def setup(bot):
    bot.add_cog(Main(bot))