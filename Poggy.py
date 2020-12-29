import discord
import os
from keep_alive import keep_alive
from discord.ext import commands,tasks

disIntents = discord.Intents().all()
client = commands.Bot(command_prefix='.', intents=disIntents)

@client.event
async def on_ready():
  await client.change_presence(
     status=discord.Status.idle, activity=discord.Game('alive?'))
  print('Bot is ready')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

keep_alive()
client.load_extension('cogs.main')
client.run(os.getenv('TOKEN'))
