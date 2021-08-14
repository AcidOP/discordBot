# !/usr/bin/python3

import json
import discord
import requests
from random import choice
from discord.ext import commands


class api(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        memeChannel = discord.utils.get(self.bot.get_all_channels(), name="meme")
        links = ["https://memes.blademaker.tv/api/indianmemer",
                 "https://memes.blademaker.tv/api/Indiameme",
                 "https://memes.blademaker.tv/api/SamayRaina",
                 "https://memes.blademaker.tv/api/desimemes"
                 "https://memes.blademaker.tv/api"]

        r = requests.get(choice(links))
        resp = r.json()

        title = resp["title"]
        memeEmbed = discord.Embed(
            title=f"{title}",
            color=0x00ff00)
        memeEmbed.set_image(url=resp["image"])
        await memeChannel.send(embed=memeEmbed)

    @commands.command()
    async def short(self, ctx, url):

        url = "https://www." + url

        username = "bitly username"
        password = "bitly password"
        auth_res = requests.post(
            "https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
        access_token = auth_res.content.decode()
        headers = {"Authorization": f"Bearer {access_token}"}
        groups_res = requests.get(
            "https://api-ssl.bitly.com/v4/groups", headers=headers)
        guid = groups_res.json()['groups'][0]['guid']
        shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={
                                    "group_guid": guid, "long_url": url}, headers=headers)
        link = shorten_res.json().get("link")
        await ctx.send(link)


def setup(bot):
    bot.add_cog(api(bot))
