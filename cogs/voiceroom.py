from discord.errors import Forbidden, HTTPException, InvalidArgument
import os, json
from datetime import datetime, timedelta
from discord.ext import commands, tasks
from core.classes import Cog_Extension
from dotenv import load_dotenv
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
BOT_ID=os.getenv('PUBLIC_KEY')
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

GUILD_ID=jdata['guild_id']

class RoomLimitReached(commands.CommandError):
    pass

class Room():
    def __init__(self, voiceChannel, create_time, creator):
        self.voiceChannel = voiceChannel
        self.creator = creator
        self.create_time = create_time
        print(GUILD_ID)

class VoiceRoom(Cog_Extension):

    def __init__(self, bot):
        super().__init__(bot)
        self.rooms = []
        self.expireChecker.start()

    
    @cog_ext.cog_slash(name="voiceroomtest", description="This is just a test command, nothing more.", guild_ids=GUILD_ID)
    async def _ping(self, ctx):
        await ctx.send(f"測試!123")

    @cog_ext.cog_slash(name='createroom', description="建立私人語音頻道", guild_ids=GUILD_ID)
    async def _createroom(self, ctx):
        if len(self.rooms)>0: raise RoomLimitReached()
        try:
            vc = await ctx.guild.create_voice_channel(name=f'{ctx.author.name}@{datetime.strftime(datetime.now(), "%H%M%S")}', position=len(ctx.guild.channels))
            # print(len(self.bot.get_guild(GUILD_ID[0]).channels))
            await vc.set_permissions(ctx.author, manage_channels=True)
        except Forbidden:
            await ctx.send('Forbidden')
        except HTTPException:
            await ctx.send('HTTPException')
        except InvalidArgument:
            await ctx.send('InvalidArgument')
        self.rooms.append(Room(vc, datetime.now(), ctx.author))
        await ctx.send("Room Created")
    
    @tasks.loop(minutes=1.0)
    async def expireChecker(self):
        print('Cheaking Rooms')
        for index in reversed(range(len(self.rooms))):
            room = self.rooms[index]
            if room.create_time + timedelta(minutes=1) < datetime.now():
                print(f'Channel {room.voiceChannel.name} Deleted')
                await room.voiceChannel.delete()
                self.rooms.pop(index)

    @expireChecker.before_loop
    async def before_expireChecker(self):
        await self.bot.wait_until_ready()

    def cog_unload(self):
        self.expireChecker.cancel()

def setup(bot):
    bot.add_cog(VoiceRoom(bot))