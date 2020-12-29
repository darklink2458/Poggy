import discord
import random
from discord.ext import commands,tasks

class TestingCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('TestingCog Loaded!')

    @commands.command(aliases=['randQuote'], help = 'Produces a random quote from the ones saved with the addQuote command')
    async def randquote(self, ctx):
        lines = open('quotes.txt').read().splitlines()
        myline = random.choice(lines)
        #lines.close()
        await ctx.send(myline)


    @commands.command(aliases=['addquote'], help = 'Adds a quote to the quote list.')
    async def addQuote(self, ctx, *, quote):
        f = open("quotes.txt", "a")
        f.write(quote + '\n')
        f.close()
        await ctx.send('Quote Saved!')

def setup(client):
    client.add_cog(TestingCog(client))
