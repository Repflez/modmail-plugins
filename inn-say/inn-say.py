import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

class MTPSayPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    @commands.command()
    async def mtpsay(self, ctx, *, message: str):
        """I'll have two number 9s, a number 9 large, a number 6 with extra dip, a number 7, two number 45s, one with cheese, and a large soda."""
        channel = self.bot.get_channel(328236301021347841)
        await channel.send(f"{message}")

def setup(bot):
    bot.add_cog(MTPSayPlugin(bot))
