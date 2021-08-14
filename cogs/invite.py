import discord
from discord.ext import commands


class invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        generalChannel = discord.utils.get(
            self.bot.get_all_channels(), name="general")
        invite_link = await generalChannel.create_invite()
        await ctx.reply(f"Here's your invite link:\n{invite_link}")


def setup(bot):
    bot.add_cog(invite(bot))
