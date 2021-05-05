import os                               #Reading the token of the bot
import requests                         #API
import json                             #Reading the received data from requests module
import discord                          #Discord OwO
from discord.ext import commands        #Discord commands OwO
from time import sleep                  #Make the bot wait before a certain task

# Required for bot to welcome members
intents = discord.Intents.default()
intents.members = True

# Instance of the bot
bot = commands.Bot(
  command_prefix="Pls", 
  strip_after_prefix=True,
  help_command=None,
  intents = intents
)

TOKEN = os.environ['token']

# The channel and guild IDs
general = 826356833790722068
welcome = 839035255049945120

@bot.event
async def on_ready():
  generalChannel = bot.get_channel(general)
  allowed_mentions = discord.AllowedMentions(everyone = True)
  await generalChannel.send(content = "@everyone", allowed_mentions = allowed_mentions)
  await generalChannel.send(f'I am online. Type "Pls help" for the help menu')  
  print(f'Bot connected as {bot.user}')

#                                       THE INSULT METHOD
@bot.command()
async def insult(ctx, args=''):
  
  # Getting the insulting message 
  response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
  jsonData = json.loads(response.text)

  if args != '':
    botId = 837929231831793694 
    target = int(args[3:len(args)-1])

    # Checks if the argument is targeted to the bot itself
    if target == botId:
      await ctx.reply(f'{ctx.author.mention} You dare use my own spells against me Potter?!')
      return

    # Sending the message to the supplied person in the command
    await ctx.message.channel.send(f"{args} {jsonData['insult']}")
    return

  # If no argument supplied the bot will reply
  # to the member who sent the command. Else
  # the bot will tag the person supplied by the command
  # Replying to the member who sent the command
  await ctx.message.reply(f"{ctx.message.author.mention} {jsonData['insult']}")


#                                         THE HELP EMBED
@bot.command()
async def help(ctx):
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
    name = 'Pls insult',
    value = 'Send an insulting message to yourself',
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
    name = 'Pls clear',
    value = 'Delete recent 1000 texts from the channel',
    inline = False
  )
  # Send the help embed 
  await ctx.reply(embed = helpEmbed)

#                                           CLEAR THE CHANNEL
@bot.command()
async def clear(ctx):
  allowed_mentions = discord.AllowedMentions(everyone = True)
  await ctx.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
  await ctx.channel.send(f'All messages are going to be deleted from this channel')
  sleep(5)
  await ctx.channel.purge(limit= 1000)
  await ctx.channel.send(f'{ctx.message.author.mention} deleted the messages ')


#                                           WELCOMING NEW MEMBERS
@bot.event
async def on_member_join(member):
  # The channel the message is to be sent
  welcomeChannel = bot.get_channel(welcome)
  # Creating an embed
  welcomeEmbed = discord.Embed(
    title=f"Welcome {member.name}", 
    description=f"{member.mention} Thanks for joining!",
    # Neon green
    color = 0x00ff00
    )
  welcomeEmbed.set_thumbnail(url = member.avatar_url)
  await welcomeChannel.send(embed = welcomeEmbed)


#                                        PROVIDING THE INVITE LINKS
@bot.command()
async def invite(ctx):
  # creating the link
  link = await ctx.channel.create_invite(
    # Does not expire
    max_age = 0,
    # Expires after single use 
    max_uses = 0,
    # Same link will be provided
    unique = False,
    )
  # embed contains the invite link
  inviteEmbed = discord.Embed(
    title = "Here is your invite link",
    # The embed description contains the link
    description = link,
    # neon green
    color = 0x00ff00
    )
  await ctx.reply(embed = inviteEmbed)

@bot.event
async def on_message(message):

  print(f'{message.author.name} : {message.content}')

  # Bot does not reply to it's own messages
  if message.author == bot.user:
    return

  # Running the commands
  await bot.process_commands(message)

# Run instance of the bot
bot.run(TOKEN)
