import os, json
from discord.ext import commands
from core.classes import Cog_Extension
from dotenv import load_dotenv
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option, create_choice

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
BOT_ID=os.getenv('PUBLIC_KEY')
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
GUILD_ID=jdata['guild_id']
class Slash(Cog_Extension):

    def has_move_member_permissions():
        original = commands.has_guild_permissions(move_members=True).predicate
        async def extended_check(ctx):
            if ctx.guild is None:
                return False
            return ctx.guild.owner_id == ctx.author.id or await original(ctx)
        return commands.check(extended_check)
    
    @cog_ext.cog_slash(name="ping", description="This is just a test command, nothing more.", guild_ids=GUILD_ID)
    async def ping(self, ctx):
        await ctx.send(f"Pong! ({self.bot.latency*1000}ms)")

    @cog_ext.cog_slash(name="test",
                description="This is just a test command, nothing more.",
                options=[
                create_option(
                    name="optone",
                    description="This is the first option we have.",
                    option_type=3,
                    required=False
                )
                ],
                guild_ids=GUILD_ID)
    async def test(self, ctx, optone: str='Nothing'):
        await ctx.send(content=f"I got you, you said {optone}!")
    
    @cog_ext.cog_slash(name="say",
                description="讓機器人為你說什麼",
                options=[
                create_option(
                    name="context",
                    description="要說的內容",
                    option_type=3,
                    required=True
                )
                ],
                guild_ids=GUILD_ID)
    async def say(self, ctx, context: str='什麼都沒有'):
        await ctx.send(content=f" {context}")
    
    @cog_ext.cog_slash(name="tpall",
                description="tp所有人",
                options=[
                create_option(
                    name="channel",
                    description="傳送座標",
                    option_type=7,
                    required=True
                )
                ],
                guild_ids=GUILD_ID)
    @has_move_member_permissions()
    async def tpall_slash(self, ctx, channel):
        for ppl in ctx.author.voice.channel.members:
            await ppl.move_to(channel)
        await ctx.send("tp 成功")
    
    @cog_ext.cog_slash(name="watch",
                description="你是變態吧",
                options=[
                create_option(
                    name="cha",
                    description="要偷窺的房間",
                    option_type=7,
                    required=True
                )
                ],
                guild_ids=GUILD_ID)
    async def watch_slash(self, ctx, cha):
        output=""
        for ppl in cha.members:
            if ppl.activity != None:
                output = output + ppl.display_name + ": " + ppl.activity.name + '\n'
        if output=="":
            await ctx.send('大家都死了')
        else:
            await ctx.send(output)

    @cog_ext.cog_slash(name="gamemode",
                description="切換遊戲模式",
                options=[
                create_option(
                    name="mode",
                    description="遊戲模式",
                    option_type=4,
                    required=True,
                    choices=[
                        create_choice(name='survival', value=0),
                        create_choice(name='creative', value=1),
                        create_choice(name='adventure', value=2)
                    ]
                )
                ],
                guild_ids=GUILD_ID)
    async def _gamemode(self, ctx, mode):
        if(mode==0):
            await ctx.send('生存模式')
        elif(mode==1):
            await ctx.send('創造模式')
        elif(mode==2):
            await ctx.send('冒險模式')
    
    @cog_ext.cog_slash(name="purge",
                description="清除訊息",
                options=[
                create_option(
                    name="amount",
                    description="amount to purge",
                    option_type=4,
                    required=True
                )
                ],
                guild_ids=GUILD_ID)
    async def _purge(self, ctx, amount:int):
        await ctx.send("Start purging.")
        await ctx.channel.purge(limit=amount+1)

def setup(bot):
    bot.add_cog(Slash(bot))