import os  
import discord  
from discord.ext import commands 
from keepAlive import keep_alive

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="Pls",
                   strip_after_prefix=True,
                   help_command=None,
                   case_insensitive=True,
                   intents=intents
                   )

TOKEN = os.environ['token']

def record(author, message):
	hist = open('hist.text', 'a')
	hist.write(f'\n{author} : {message}')
	hist.close()

@bot.event
async def on_member_join(member):
	welcomeChannel = discord.utils.get(bot.get_all_channels(), name='welcome')
	welcomeEmbed = discord.Embed(
	    title=f"Welcome {member.name}",
	    description=f"{member.mention} Thanks for joining!",
	    color=0x00ff00)
	welcomeEmbed.set_thumbnail(url=member.avatar_url)
	await welcomeChannel.send(embed=welcomeEmbed)


@bot.event
async def on_message(message):

	if str(message.channel.type) == 'private':
		modChannel = discord.utils.get(bot.get_all_channels(),
		                               name='moderators')
		await modChannel.send(f'[{message.author.name}] : {message.content}')
		return

  record(message.author, message.content)

	if message.author == bot.user:
		return

	await bot.process_commands(message)


for file in os.listdir('./cogs'):
	if file.endswith('.py'):
		bot.load_extension(f'cogs.{file[:-3]}')
		print(f'The cog {file[:-3]} was loaded')

keep_alive()

# Run instance of the bot
bot.run(TOKEN)
