import discord    
from discord.ext import commands
    
class allevents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        welcomeChannel = discord.utils.get(self.bot.get_all_channels(), name="welcome")    
        embed = discord.Embed(title="Welcome to the server!", color=0x00ff00)
        embed.add_field(name=member.display_name, value="hopped into the server", inline=False)
        embed.add_field(name=member.display_name, value="hopped into the server", inline=True)
        embed.set_thumbnail(url=member.avatar_url)
        await welcomeChannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("```Invalid command. Try using `Pls help` to figure out commands!```")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```Please pass in all requirements.\ncheck `Pls help <command>` for all requirements```')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You dont have all the requirements or permissions for using this command ```")

def setup(bot):
    bot.add_cog(allevents(bot))
