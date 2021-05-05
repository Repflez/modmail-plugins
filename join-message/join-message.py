import logging

import discord
from discord.ext import commands

logger = logging.getLogger("Modmail")

from core import checks
from core.models import PermissionLevel


class JoinMessagePlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        config = await self.db.find_one({"_id": "mtp-join-config"})

        if config is None:
            logger.info("User joined, but no join message was set.")
            return

        try:
            message = config["mtp-join-message"]["message"]
            channel = self.bot.get_channel(328236301021347841)
            await channel.send(f"{member.mention} is taking a rest at the Inn.")
        except:
            return

def setup(bot):
    bot.add_cog(JoinMessagePlugin(bot))
