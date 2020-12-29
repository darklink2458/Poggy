import discord
import random
import json
from discord.ext import commands,tasks

class TestingCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('TestingCog Loaded!')


    #@commands.command(aliases=['randQuote'], help = 'Produces a random quote from the ones saved with the addQuote command')
    #async def randquote(self, ctx):
    #    lines = open('quotes.txt').read().splitlines()
    #    myline = random.choice(lines)
    #    #lines.close()
    #    await ctx.send(myline)


    @commands.command()
    async def ting(self, ctx):
      await ctx.send(ctx.message.guild.name)


    @commands.command(aliases=['addquote'], help = 'Adds a quote to the quote list.')
    async def addQuote(self, ctx, *, quote):
        #Opens the Json Quote Database
        file = open('quotes.json', 'r')
        ServerQuotes = json.load(file)
        server = ctx.message.guild.name

        if server not in ServerQuotes:
          ServerQuotes[server] = {'quoteNum':0,'quotes':{}}

        curQuoteNum = ServerQuotes[server]['quoteNum'] + 1
        ServerQuotes[server]['quoteNum'] = curQuoteNum
        ServerQuotes[server]['quotes'][curQuoteNum] = quote

        #Writes the Updated Database to the Json File
        file = open('quotes.json', 'w')
        json.dump(ServerQuotes, file)
        file.close()
        await ctx.send('Quote Saved!')

def setup(client):
    client.add_cog(TestingCog(client))
