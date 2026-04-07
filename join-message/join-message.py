import discord
from discord.ext import commands
import random

class JoinMessagePlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.join_messages = {
            "{member} has been added!":                                         None,
            "You received a Mii! It's {member}!":                               None,
            "{member} has entered the apartment.":                              None,
            "{member} arrived at the plaza!":                                   None,
            "{member} skydived onto Wuhu Island.":                              None,
            "{member} has joined the Sports Club!" :                            None,
            "Streetpassed with {member}!":                                      None,
            "Added {member} to the player list":                                None,
            "{member} joins the fight!":                                        None,
            "{member} has visited Hayley's Ranch!":                             "<:HayleyHey:1490867198619815967>",
            "{member} is trotting the globe.":                                  None,
            "{member} is planting flowers!":                                    "🌸",
            "{member} has joined the Party Walk!":                              None,
            "{member} would like a new hat.":                                   None,
            "{member} is vacationing on Kawawii Island.":                       None,
            "{member}'s QR Code has been scanned.":                             None,
            "Transferred {member} from the Wii.":                               None,
            "{member} is playing a Worldwide VS Race!":                         None,
            "{member} is using tilt controls!":                                 None,
            "{member} has Yeah'd this message.":                                "<:yeah:1490264399238139944>",
            "{member} has bought HP Bananas.":                                  "<:HPbanana:1490264139598401576>",

            # Server specific join messages
            "The Bread Council has decided that {member} is welcome!":          "🍞",
            "{member} wants to share their bread with the server.":             "🍞",
            "Hey! {member} has bread!":                                         "🍞",
        }

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1473099778844917790)

        if channel is None:
            return  # Avoid crash if channel not found

        message_template, emoji = random.choice(list(self.join_messages.items()))
        sent = await channel.send(message_template.format(member=member.mention))

        if emoji:
            try:
                await sent.add_reaction(emoji)
            except discord.HTTPException:
                pass

async def setup(bot):
    await bot.add_cog(JoinMessagePlugin(bot))
