import discord
import os
import json
from discord.ext import commands,tasks

class TestingCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('TestingCog Loaded!')

    @commands.command()
    async def poop(self, ctx):
      await ctx.send('ctx.message.server')


def setup(client):
    client.add_cog(TestingCog(client))
