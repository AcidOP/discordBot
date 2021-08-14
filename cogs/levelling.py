import json
import discord
from discord.ext import commands


class levelling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('users.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users, member)

        with open('users.json', 'w') as f:
            json.dump(users, f)


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == False:
            with open('users.json', 'r') as f:
                users = json.load(f)

            await self.update_data(users, message.author)
            await self.add_experience(users, message.author, 5)
            await self.level_up(users, message.author, message)

            with open('users.json', 'w') as f:
                json.dump(users, f)


    async def update_data(self, users, user: discord.Member):
        if not f'{user.id}' in users:
            users[f'{user.id}'] = {}
            users[f'{user.id}']['name'] = user.display_name
            users[f'{user.id}']['experience'] = 0
            users[f'{user.id}']['level'] = 1


    async def add_experience(self, users, user, exp):
        users[f'{user.id}']['name'] = user.display_name
        users[f'{user.id}']['experience'] += exp


    async def level_up(self, users, user, message):
        levelChannel = discord.utils.get(self.bot.get_all_channels(), name="level")    
        experience = users[f'{user.id}']['experience']
        lvl_start = users[f'{user.id}']['level']
        lvl_end = int(experience ** (1 / 4))
        if lvl_start < lvl_end:
            await levelChannel.send(f'{user.mention} has leveled up to level {lvl_end}')
            users[f'{user.id}']['level'] = lvl_end


    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        if not member:
            id = ctx.message.author.id
            with open('users.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            await ctx.send(f'You are at level {lvl}!')
        else:
            id = member.id
            with open('users.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            await ctx.send(f'{member.display_name} is at level {lvl}!')


def setup(bot):
    bot.add_cog(levelling(bot))
