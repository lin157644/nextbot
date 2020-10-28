import discord
from discord.ext import commands
from core.classes import Cog_Extension

#後
#main 繼承commands.cog類別
class Main(Cog_Extension):
    
    @commands.command()
    #ctx = context (上下文)
    #A:(上文) (user, id, user current server, user channel)
    #latency is float in second
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

#先
#註冊類別
#傳入body的bot的bot??
def setup(bot):
    bot.add_cog(Main(bot))