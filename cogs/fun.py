import discord
from discord.ext import commands
import requests
import json

class fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def insult(self, ctx, target: discord.Member):
    
    if target == self.bot.user:
      await ctx.reply('You dare use my own spells against me Potter ??!!')
      return

    response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    jsonData = json.loads(response.text)

    await ctx.send(f'{target.mention} {jsonData["insult"]}')


  @commands.command()
  async def source(self, ctx):
    link = 'https://github.com/acidOP/discordBot/'
    sourceEmbed = discord.Embed(
      name = "Here's my source code",
      description = link,
      color = 0x00ff00
      )
    await ctx.reply(embed = sourceEmbed)

  @commands.command()
  async def invite(self, ctx):
    link = await ctx.channel.create_invite(
      max_age = 0,
      max_uses = 0,
      unique = False,
      )
    inviteEmbed = discord.Embed(
      title = "Here is your invite link",
      description = link,
      color = 0x00ff00
      )
    await ctx.reply(embed = inviteEmbed)


def setup(bot):
  bot.add_cog(fun(bot))

