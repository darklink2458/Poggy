import discord
import random
import json
from discord.ext import commands,tasks

class Quotes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('quotes Loaded!')


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

    @commands.command(aliases=['randQuote'], help = 'Produces a random quote from the ones saved with the addQuote command')
    async def randquote(self, ctx):
        file = open('quotes.json', 'r')
        ServerQuotes = json.load(file)
        file.close()
        server = ctx.message.guild.name
        quotenum = ServerQuotes[server]['quoteNum']

        myline = ServerQuotes[server]['quotes'][f'{random.randint(1, quotenum)}']
        await ctx.send(myline)


    @commands.command(aliases=['getQuote'], help = 'Grabs a random quote from the server quote list')
    async def getquote(self, ctx, input):
        file = open('quotes.json', 'r')
        ServerQuotes = json.load(file)
        file.close()
        server = ctx.message.guild.name
        quotenum = ServerQuotes[server]['quoteNum']

        if input not in ServerQuotes[server]['quotes']:
            await ctx.send(f'You entered {input}, this is not a valid quote number.\nThere are {quotenum} quotes saved for this server.')
        else:
            myline = ServerQuotes[server]['quotes'][input]
            await ctx.send(f'Quote {input}: {myline}')

def setup(client):
    client.add_cog(Quotes(client))
