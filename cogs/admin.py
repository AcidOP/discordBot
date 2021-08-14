from discord.ext import commands

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 10):
        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def reload(self, ctx, extension):
        extension = "cogs." + extension
        try:
            self.bot.unload_extension(extension)
            self.bot.load_extension(extension)
            await ctx.send(f'The extension "{extension}" was reloaded')
        except:
            await ctx.send(f'The extension "{extension}" could not be reloaded')

def setup(bot):
    bot.add_cog(admin(bot))
