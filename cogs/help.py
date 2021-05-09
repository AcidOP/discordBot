import discord
from discord.ext import commands

class help(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def help(self, ctx):
      helpEmbed = discord.Embed(
      title = "All bot commands",
      author = ctx.guild.owner,
      color = 0x00ff00
      )
      helpEmbed.add_field(
        name = 'Pls help',
        value = 'View this window',
        inline = False
      )
      helpEmbed.add_field(
        name = 'Pls insult @friend',
        value = 'Send an insulting message to your friend',
        inline = False
      )
      helpEmbed.add_field(
        name = 'Pls invite',
        value = 'Generate an invite link',
        inline = False
      )
      helpEmbed.add_field(
        name = 'Pls clear <No of messages>',
        value = 'Delete the number of texts given (Default to 1000) [Staff only]',
        inline = False
      )
      helpEmbed.add_field(
        name = 'Pls source',
        value = 'Display the program of the bot',
        inline = False
      )
      # Send the help embed 
      await ctx.reply(embed = helpEmbed)

def setup(bot):
  bot.add_cog(help(bot))
