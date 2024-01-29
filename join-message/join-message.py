import discord
from discord.ext import commands

class JoinMessagePlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1140088471420145674)
        await channel.send(f"{member.mention} is now resting in <#1140088471420145674>.")

async def setup(bot):
    await bot.add_cog(JoinMessagePlugin(bot))
