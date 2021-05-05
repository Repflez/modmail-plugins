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
        
    @commands.command(aliases=["swms"])
    @checks.has_permissions(PermissionLevel.ADMIN)
    async def setjoinmessage(self, ctx, *, message):
        """Set a message to show a user after they join."""
        await self.db.find_one_and_update(
            {"_id": "mtp-join-config"},
            {"$set": {"mtp-join-message": {"message": message}}},
            upsert=True,
        )

        await ctx.send("Successfully set the message.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        config = await self.db.find_one({"_id": "mtp-join-config"})

        if config is None:
            logger.info("User joined, but no join message was set.")
            return

        try:
            message = config["mtp-join-message"]["message"]
            channel = self.bot.get_channel(328236301021347841)
            await channel.send(message.replace("{user}", str(member)))
        except:
            return

def setup(bot):
    bot.add_cog(JoinMessagePlugin(bot))
