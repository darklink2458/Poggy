import discord
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
from discord.ext import commands,tasks

disIntents = discord.Intents().all()
client = commands.Bot(command_prefix='.', intents=disIntents)

@client.event
async def on_ready():
  await client.change_presence(
     status=discord.Status.idle, activity=discord.Game('alive?'))
  print('Bot is ready')

@client.command(help = 'This command pings poggy and he will tell you how long it takes to get to him.')
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000, 2)}ms')


@client.command(help = "Rock Paper Scissors. Write one after your command to play.")
async def rps(ctx, player_move):
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


@client.command(help = 'insult')
async def fat(ctx):
    await ctx.send('<@271347480291966977>')#<@310230674483183630>


@client.command(help = 'Github Link')
async def github(ctx):
    await ctx.send('https://github.com/darklink2458/Poggy')


@client.command(help = 'Produces a quote that may inspire your entire server!')
async def inspire(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    await ctx.send(quote)


@client.command(help = 'Turns any serious input into the ramblings of child.')
async def uwu(ctx, *, string2):
    str = string2
    str = str.replace('r', 'w')
    str = str.replace('R', 'W')
    str = str.replace('l', 'w')
    str = str.replace('L', 'W')
    await ctx.send(str)


@client.command(aliases=['botguy'], help = "Pings poggy's father")
async def botGuy(ctx):
    await ctx.send('<@271347480291966977>')


@client.command(aliases=['randQuote'], help = 'Produces a random quote from the ones saved with the addQuote command')
async def randquote(ctx):
    lines = open('quotes.txt').read().splitlines()
    myline = random.choice(lines)
    #lines.close()
    await ctx.send(myline)


@client.command(aliases=['addquote'], help = 'Adds a quote to the quote list.')
async def addQuote(ctx, *, quote):
    f = open("quotes.txt", "a")
    f.write(quote + '\n')
    f.close()
    await ctx.send('Quote Saved!')


@client.command(help = 'Pings a random member of the server')
async def randem(ctx):
    #memList = ctx.message.guild.fetch_members()#ctx.message.guild.members
    member = random.choice(ctx.message.guild.members).mention
    while (member == '<@788553232380985364>'):
        member = random.choice(ctx.message.guild.members).mention
    await ctx.send(f'The Random person is: ' + member)


@client.command(help = 'ignore this one')
async def poger(ctx):
    await ctx.send(
        'https://www.twitch.tv/scrungo_tumbus/clip/HandsomeAmazonianPhoneKevinTurtle?filter=clips&range=all&sort=time'
    )


@client.command(aliases=['8ball'], help = "Ask Poggy a yes or no question and he will answer it for you. So far he has always been right.")
async def _8ball(ctx, *, question):
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


@client.command(aliases=['moonforhenry'], help = 'Gives the phase of the moon as would be seen from Washington at the current time.')
async def moon(ctx):
    mi = pylunar.MoonInfo((47, 62, 49), (-112, 52, 10))
    mi.update(datetime.now())
    await ctx.send('Moon Phase: ' + mi.phase_name().replace('_',' ') +
                   f'\nPercentage: {round(mi.fractional_phase()*100,2)}%')

@client.command(help = "Politics hahaha")
async def neeto(ctx):
  await ctx.send('A spectre is haunting Europe — the spectre of poopism.')

@client.command(help = 'Poggy will say his favorite word a few times.')
async def pog(ctx):
  for x in range(5):
    await ctx.send('pog')
    time.sleep(randrange(9))

#@client.command()
#async def commands(ctx):
#    await ctx.send('.ping\n.inspire\n.fat\n.uwu\n.botGuy\n.addquote\n.randquote\n.randem\n.poger\n.8ball\n.moonforhenry\n')

keep_alive()
client.run(os.getenv('TOKEN'))
