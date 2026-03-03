import discord
from discord.ext import commands

class JoinMessagePlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.join_messages = [
            "{member} has been added!",
            "You received a Mii! It's {member}!",
            "{member} has entered the apartment.",
            "{member} arrived at the plaza!",
            "{member} skydived onto Wuhu Island.",
            "{member} has joined the Sports Club!" ,
            "Streetpassed with {member}!",
            "Added {member} to the player list",
            "{member} joins the fight!",
            "{member} has visited Hayley's Ranch!",
            "{member} is trotting the globe.",
            "{member} is planting flowers!",
            "{member} has joined the Party Walk!",
            "{member} would like a new hat.",
            "{member} is vacationing on Kawawii Island.",
            "{member}'s QR Code has been scanned.",
            "Transferred {member} from the Wii.",
            "{member} is playing a Worldwide VS Race!",
            "{member} is using tilt controls!"
        ]

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1140088471420145674)

        if channel is None:
            return  # Avoid crash if channel not found

        message_template = random.choice(self.messages)
        message = message_template.format(member=member.mention)

        await channel.send(message)

async def setup(bot):
    await bot.add_cog(JoinMessagePlugin(bot))
