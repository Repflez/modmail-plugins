import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class JoinMessagePlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(328236301021347841)
        await channel.send(f"{member.mention} is taking a rest at the Inn.\nWelcome! Please check out <#813243687983251476>, <#749651917587873903> and <#618548247367122954>!")

def setup(bot):
    bot.add_cog(JoinMessagePlugin(bot))
