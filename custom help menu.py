from logging import error
import discord
from discord import channel
from discord import activity
from discord.ext import commands
import json

# be sure to do pip install discord.py & have a bot ready including a token
# **REMOVE THESE HASHTAG MESSAGES ONCE DONE**

from discord.ext.commands.core import has_permissions

intents = discord.Intents.default()
intents.members - True

client = commands.Bot(command_prefix='=', intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    print("The bot is ready to be used! Code on.")
    print("------------------")


@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.orange()
    )

    embed.set_author(name='Help Menu!')
    embed.add_field(name='prefix & name of command',
                    value='description of command', inline=False)

# copy and paste the embed.add_field command & value!!

    await author.send(embed=embed)
    await ctx.send("I sent you a DM!")

# this command is for your bot to state they sent you a DM, you can delete this if you don't want it.

client.run('BOT TOKEN HERE IF YOU DONT ALREADY HAVE A BOT')
