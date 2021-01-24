import discord
from discord.embeds import Embed
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import json

#後
#main 繼承commands.cog類別
class Main(Cog_Extension):
    
    @commands.command()
    #ctx = context (上下文)
    #A:(上文) (user, id, user current server, user channel)
    #latency is float in second
    async def ping(self, ccc):
        await ccc.send(f'{round(self.bot.latency*1000)} (ms)')
    
    @commands.command()
    async def embedtest(self, ctx):
        embed=discord.Embed(title="123", url="http://url.test", color=0x575757, timestamp=datetime.datetime.now())
        embed.set_author(name="author name ", url="https://author-link.test", icon_url="https://author-icon.test")
        embed.set_thumbnail(url="http://icon.test")
        embed.add_field(name="Fields1-name", value="value1", inline=True)
        embed.add_field(name="Fields2-name", value="value2", inline=True)
        embed.add_field(name="Fields3-name", value="value3", inline=True)
        embed.add_field(name="Fields4-name", value="value4", inline=True)
        embed.set_footer(text="Footer-Text")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def embed(self, ctx, *, msg):
        jfile=json.loads(msg)
        embed=discord.Embed(title=jfile.get("title"), url=jfile.get("url", ""), color=jfile.get("color", 5198940), timestamp=datetime.datetime.now())
        if "author" in jfile:
            embed.set_author(name=jfile.get("author").get("name"), url=jfile.get("author").get("url", ""), icon_url=jfile.get("author").get("icon_url", ""))
        if "thumbnail" in jfile:
            embed.set_thumbnail(url=jfile.get("thumbnail"))
        if "image" in jfile:
            embed.set_image(url=jfile.get("image"))
        for i in jfile.get("fields"):
            embed.add_field(name=i.get("name"), value=i.get("value"), inline=i.get("inline"))
        if "footer" in jfile:
            embed.set_footer(text=jfile.get("footer").get("text"), icon_url=jfile.get("footer").get("icon_url", ""))
        await ctx.send(context="",embed=embed)
    
    @commands.command()
    #*,msg代表 不管之後有幾個argument都視為msg
    #,*msg代表用"分開??
    async def say(self, ctx, *, msg):
        #這裡傳入的msg是str
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def purge(self, ctx, num:int):
        #記得加一
        await ctx.channel.purge(limit=num+1)
    
#load_extension的entry point
#註冊類別
#傳入body的bot的bot??
def setup(bot):
    bot.add_cog(Main(bot))

