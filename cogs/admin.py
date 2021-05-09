from discord.ext import commands

class admin(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount: int= 1000):
    await ctx.channel.purge(limit= amount+1)

def setup(bot):
  bot.add_cog(admin(bot))
