from core.classes import Cog_Extension

class Osu(Cog_Extension):
    pass


def setup(bot):
    bot.add_cog(Osu(bot))
