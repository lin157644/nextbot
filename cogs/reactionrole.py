from datetime import datetime
from os import getenv, name
from core.database import Database
from discord.ext import commands
from core.classes import Cog_Extension
from dotenv import load_dotenv
from discord import Embed
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option, create_choice
load_dotenv()
db_user = getenv('DB_USER')
db_passwd = getenv('DB_PASSWORD')

class ReactionRole(Cog_Extension):
    GUILD_ID=[int(getenv('GUILD_ID'))]

    def __init__(self, bot):
        super().__init__(bot)
        self.db = Database(db_user, db_passwd)
        self.db.cur.execute("USE nextbot;")
    
    @cog_ext.cog_slash(name="addrole",
                description="Add new reaciton role.",
                options=[
                create_option(
                    name="channel",
                    description="Target channel",
                    option_type=7,
                    required=True
                ),
                create_option(
                    name="message",
                    description="Target message ID",
                    option_type=3,
                    required=True
                ),
                create_option(
                    name="reaction",
                    description="Target reaction",
                    option_type=3,
                    required=True
                ),
                create_option(
                    name="role",
                    description="Target role",
                    option_type=8,
                    required=True
                )
                ],
                guild_ids=GUILD_ID)
    async def _addrole(self, ctx, channel, message, reaction, role):
        UID = hash(str([message, reaction, role]))
        # todo: 要是moderator init reaction Check duplicate
        # print(f'INSERT INTO reactionrole (unique_id, channel_id, message_id, reaction, role_id) VALUE ({UID}, {channel.id}, {message}, {reaction}, {role.id});')
        if ctx.author == ctx.guild.owner:
            self.db.cur.execute(
                "INSERT INTO reactionrole (unique_id, channel_id, message_id, reaction, role_id) VALUE (?, ?, ?, ?, ?);", 
                (UID, channel.id, message, reaction, role.id))
            theMessage= await channel.fetch_message(message)
            await theMessage.add_reaction(reaction)
            embed=Embed(title=f"Reaction Role Created:", color=0x34CB78, timestamp=datetime.now())
            embed.add_field(name="Unique ID:", value=UID, inline=False)
            embed.add_field(name="頻道:", value=channel.name, inline=False)
            embed.add_field(name="訊息ID:", value=channel.id, inline=False)
            embed.add_field(name="Emoji:", value=reaction, inline=False)
            embed.add_field(name="身分組:", value=role.name, inline=False)
            embed.set_footer(text="lin157644#1337")
            await ctx.send("", embed=embed)
        else:
            embed=Embed(title=f"Permission Denied, you are not the server owner.", color=0x34CB78, timestamp=datetime.now())
            await ctx.send("", embed=embed)
    
    @cog_ext.cog_subcommand(base="removerole",
                            name="byuid",
                            description="Remove existing reaction roleby unique id.",
                            options=[
                                create_option(name="uid", description="Unique ID", option_type=3, required=True)
                            ],
                            guild_ids=GUILD_ID)
    async def _removerole_byid(self, ctx, uid: str):
        if ctx.author == ctx.guild.owner:
            try:
                self.db.cur.execute("DELETE FROM reactionrole WHERE unique_id=?;", (uid,)) # 必須是Tuple
                embed=Embed(title=f"Reaction Role Removd:", color=0x34CB78, timestamp=datetime.now())
                embed.add_field(name="Removed reaction role ID:", value=uid, inline=False)
                embed.set_footer(text="lin157644#1337")
                await ctx.send(content=uid)
                await ctx.send("", embed=embed)
            except Exception as e:
                print(e)
                await ctx.send("Query Fail")
        else:
            embed=Embed(title=f"Permission Denied, you are not the server owner.", color=0x34CB78, timestamp=datetime.now())
            await ctx.send("", embed=embed)
        
    
    @cog_ext.cog_subcommand(base="removerole",
                            name="bymessage",
                            description="by message id.",
                            options=[
                                create_option(name="id", description="message ID", option_type=3, required=True)
                            ],
                            guild_ids=GUILD_ID)
    async def _removerole_bymessage(self, ctx, id: str):
        if ctx.author == ctx.guild.owner:
            try:
                print(int(id))
                self.db.cur.execute("DELETE FROM reactionrole WHERE message_id=?;", (id,))
                embed=Embed(title=f"Reaction Role Removd:", color=0x34CB78, timestamp=datetime.now())
                embed.add_field(name="Removed reaction role Message ID:", value=id, inline=False)
                embed.set_footer(text="lin157644#1337")
                await ctx.send("", embed=embed)
            except Exception as e:
                print(e)
                await ctx.send("Query Fail")
        else:
            embed=Embed(title=f"Permission Denied, you are not the server owner.", color=0x34CB78, timestamp=datetime.now())
            await ctx.send("", embed=embed)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.user_id != self.bot.user.id:
            self.db.cur.execute(
                "SELECT role_id FROM reactionrole WHERE message_id=? AND reaction=?;", 
                (payload.message_id, str(payload.emoji)))
            for role_id in self.db.cur:
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(int(role_id[0]))
                # print(int(role_id[0]))
                await payload.member.add_roles(role)
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.user_id != self.bot.user.id:
            self.db.cur.execute(
                "SELECT role_id FROM reactionrole WHERE message_id=? AND reaction=?;", 
                (payload.message_id, str(payload.emoji)))
            for role_id in self.db.cur:
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(int(role_id[0]))
                member = guild.get_member(payload.user_id)
                # print(int(role_id[0]))
                await member.remove_roles(role)

def setup(bot):
    bot.add_cog(ReactionRole(bot))