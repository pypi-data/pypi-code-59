import discord
from discord.ext import commands

def embed(title=None, description=None, colour=None):
    embed = discord.Embed(
        title=title,
        description=description,
        color=colour
    )
    return embed
