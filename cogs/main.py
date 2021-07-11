import datetime, json, random
import discord
from discord.ext import commands
from core.classes import Cog_Extension

#Main 繼承commands.cog類別
class Main(Cog_Extension):
    
    @commands.command()
    #ctx = context (上下文)
    async def ping(self, ctx):
        #latency is float in second
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')
    
    @commands.command()
    async def embedtest(self, ctx):
        embed=discord.Embed(title="NextBotDev", url="https://i.imgur.com/ThSZyyL.png", color=0x575757, timestamp=datetime.datetime.now())
        embed.set_author(name="NextBotDev ", url="https://i.imgur.com/ThSZyyL.png", icon_url="https://i.imgur.com/ThSZyyL.png")
        embed.set_thumbnail(url="https://i.imgur.com/ThSZyyL.png")
        embed.add_field(name="Fields1-name", value="value1", inline=True)
        embed.add_field(name="Fields2-name", value="value2", inline=True)
        embed.add_field(name="Fields3-name", value="value3", inline=True)
        embed.add_field(name="Fields4-name", value="value4", inline=True)
        embed.set_footer(text="lin157644#1337")
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
    
    @commands.command()
    async def kick(self, ctx, *, msg:str):
        # member = discord.utils.find(lambda m: m.name == ctx, self.channel.guild.members)
        if ctx.author == ctx.guild.owner:
          member = discord.utils.get(ctx.guild.members, name=msg)
          try:
            # await discord.Member.kick(member, reason='Test')
            await member.move_to(None)
            await ctx.send(f'已處決『{msg}』')
          except:
              await ctx.send('Kick Fail QQ')
    
    @commands.command()
    async def tpall(self, ctx, cha:int):
        voice_channel = self.bot.get_channel(cha)
        members = ctx.guild.members
        for ppl in members:
            await ppl.move_to(voice_channel)
        # await self.bot.move_member(members, voice_channel)
    
    @commands.command()
    async def ban(self, ctx, sinner:int):
        sinner = ctx.guild.get_member(sinner)
        if ctx.author == ctx.guild.owner:
          await sinner.ban(reason='Bad')
          await ctx.send(f'已處決『{sinner.name}』')
    
    @commands.command()
    async def 猜拳(self, ctx, msg):
        win = random.choice([0, 1, 2])
        if msg == '剪刀':
            if win == 0:
                await ctx.send(ctx.author.mention+'布 您贏了')
            elif win == 1:
                await ctx.send(ctx.author.mention+'剪刀 平手')
            else:
                await ctx.send(ctx.author.mention+'石頭 您輸了')
        if msg == '石頭':
            if win == 0:
                await ctx.send(ctx.author.mention+'剪刀 您贏了')
            elif win == 1:
                await ctx.send(ctx.author.mention+'石頭 平手')
            else:
                await ctx.send(ctx.author.mention+'布 您輸了')
        if msg == '布':
            if win == 0:
                await ctx.send(ctx.author.mention+'石頭 您贏了')
            elif win == 1:
                await ctx.send(ctx.author.mention+'布 平手')
            else:
                await ctx.send('剪刀 您輸了')
    @commands.group(invoke_without_command=True)
    async def ouo(self, ctx):
        pass
    @ouo.command()
    async def 老皮(self, ctx):
        await ctx.send('我不會打撞球')
    @ouo.command()
    async def 許君豪(self, ctx):
        await ctx.send('這要怎麼打')
    @ouo.command()
    async def 林家昌(self, ctx):
        await ctx.send('這就是個笑話')
    @ouo.command()
    async def 呂玹緯(self, ctx):
        await ctx.send('簡育傑:我看到呂玹緯一次就扁一次')

    @commands.command()
    async def emoji(self, ctx, msg):
        print(msg)

#load_extension entry point
def setup(bot):
    bot.add_cog(Main(bot))

