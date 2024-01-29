import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

class MTPSayPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    @commands.command()
    async def innsay(self, ctx, *, message: str):
        """I'll have two number 9s, a number 9 large, a number 6 with extra dip, a number 7, two number 45s, one with cheese, and a large soda."""
        channel = self.bot.get_channel(1140088471420145674)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass
        await channel.send(f"{message}")

    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    @commands.command()
    async def cafesay(self, ctx, *, message: str):
        """I'll have know. I know my bread very well."""
        channel = self.bot.get_channel(1140091635577913378)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass
        await channel.send(f"{message}")

async def setup(bot):
    await bot.add_cog(MTPSayPlugin(bot))
