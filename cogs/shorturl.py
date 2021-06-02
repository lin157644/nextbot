from typing import Pattern
import bitlyshortener
import re, json
from os import getenv
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option
from core.classes import Cog_Extension
from dotenv import load_dotenv

class ShourURL(Cog_Extension):
    with open('setting.json', 'r', encoding='utf8') as jfile:
        jdata = json.load(jfile)
    GUILD_ID=jdata['guild_id']
    tokens_pool = ['1182b14ca4b313491d3643c897a868e7877d87ca']
    shortener = bitlyshortener.Shortener(tokens=tokens_pool, max_cache_size=256)

    @cog_ext.cog_slash(name="shorturl",
    description="Generate short url through bitlyapi.",
    options=[create_option(name="url", description="LongURL", option_type=3, required=True)],
    guild_ids=GUILD_ID)
    async def _shorturl(self, ctx, url: str):
        long_urls=[url]
        try:
            await ctx.send(self.shortener.shorten_urls(long_urls)[0])
        except:
            await ctx.send("Fail")
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author != self.bot.user:
            pattern = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
            longurl = re.match(pattern, msg.content)
            if longurl != None and self.shortener.usage() < 0.7:
                try:
                    # await msg.channel.send(longurl.group())
                    if len(longurl.group()) > 150 and len(msg.content)==len(longurl.group()) :
                        await msg.channel.send(self.shortener.shorten_urls([longurl.group()])[0])
                        await msg.delete()
                except Exception  as e:
                    print(e)

def setup(bot):
    bot.add_cog(ShourURL(bot))