import discord
from discord.ext import commands,tasks
import pylunar
import os
import datetime
from datetime import date, datetime, time
import time
import random
from random import randrange
import requests
import json
from keep_alive import keep_alive

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('MainCog Loaded!')

    #--------- Commands List -------------------------------
    #The Following List is in Alphabetical Order and should remain so
    #-------------------------------------------------------
    @commands.command(aliases=['8ball'], help = "Ask Poggy a yes or no question and he will answer it for you. So far he has always been right.")
    async def _8ball(self, ctx, *, question):
        responses = [
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.",
            "Better not tell you now.", "Cannot predict now.",
            "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
            "My sources say no.", "Outlook not so good.", "Very doubtful."
        ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(aliases=['botguy'], help = "Pings poggy's father")
    async def botGuy(self, ctx):
        await ctx.send('<@271347480291966977>')

    @commands.command(help = "makes a new face")
    async def face(self, ctx):
      response = requests.get("https://thispersondoesnotexist.com/image")
      file = open("face.jpeg", 'wb')
      file.write(response.content)
      file.close()
      await ctx.send(file = discord.File("face.jpeg"))

    @commands.command(help = 'insult')
    async def fat(self, ctx):
        await ctx.send('<@271347480291966977>')#<@310230674483183630>

    @commands.command(help = 'Github Link')
    async def github(self, ctx):
        await ctx.send('https://github.com/darklink2458/Poggy')

    @commands.command(help = 'Produces a quote that may inspire your entire server!')
    async def inspire(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + ' -' + json_data[0]['a']
        await ctx.send(quote)

    @commands.command(aliases=['moonforhenry'], help = 'Gives the phase of the moon as would be seen from Washington at the current time.')
    async def moon(self, ctx):
        mi = pylunar.MoonInfo((47, 62, 49), (-112, 52, 10))
        mi.update(datetime.now())
        await ctx.send('Moon Phase: ' + mi.phase_name().replace('_',' ') +
                       f'\nPercentage: {round(mi.fractional_phase()*100,2)}%')

    @commands.command(help = "Politics hahaha")
    async def neeto(self, ctx):
      await ctx.send('A spectre is haunting Europe — the spectre of poopism.')

    @commands.command(help = 'This command pings poggy and he will tell you how long it takes to get to him.')
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000, 2)}ms')

    @commands.command(help = 'Poggy will say his favorite word a few times.')
    async def pog(self, ctx):
      for x in range(5):
        await ctx.send('pog')
        time.sleep(randrange(9))

    @commands.command(help = 'ignore this one')
    async def poger(self, ctx):
        await ctx.send(
            'https://www.twitch.tv/scrungo_tumbus/clip/HandsomeAmazonianPhoneKevinTurtle?filter=clips&range=all&sort=time'
        )

    @commands.command(help = 'Pings a random member of the server')
    async def randem(self, ctx):
        #memList = ctx.message.guild.fetch_members()#ctx.message.guild.members
        member = random.choice(ctx.message.guild.members).mention
        while (member == '<@788553232380985364>'):
            member = random.choice(ctx.message.guild.members).mention
        await ctx.send(f'The Random person is: ' + member)

    @commands.command(help = "Rock Paper Scissors. Write one after your command to play.")
    async def rps(self, ctx, player_move):
          selection = player_move.lower()
          choices = ['rock', 'paper', 'scissors']
          if selection in choices:
              comp = random.choice(choices)
              if comp == selection:
                  result = 'Tie! You both chose ' + selection + '.'
              else:
                  if selection == 'rock':
                      if comp == 'paper':
                          result = 'You Lost! Poggy chose ' + comp + '.'
                      elif comp == 'scissors':
                          result = 'You Won! Poggy chose ' + comp + '.'
                  elif selection == 'paper':
                      if comp == 'scissors':
                          result = 'You Lost! Poggy chose ' + comp + '.'
                      elif comp == 'rock':
                          result = 'You Won! Poggy chose ' + comp + '.'
                  elif selection == 'scissors':
                      if comp == 'rock':
                          result = 'You Lost! Poggy chose ' + comp + '.'
                      elif comp == 'paper':
                          result = 'You Won! Poggy chose ' + comp + '.'
          else:
              result = 'Please choose Rock, Paper, or Scissors'
          await ctx.send(result)

    @commands.command(help = 'Turns any serious input into the ramblings of child.')
    async def uwu(self, ctx, *, string2):
        str = string2
        str = str.replace('r', 'w')
        str = str.replace('R', 'W')
        str = str.replace('l', 'w')
        str = str.replace('L', 'W')
        await ctx.send(str)

    #--------- Commands List End-------------------------------
def setup(client):
    client.add_cog(Main(client))
