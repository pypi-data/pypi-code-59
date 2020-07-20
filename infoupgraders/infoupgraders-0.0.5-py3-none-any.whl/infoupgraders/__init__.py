import discord
from discord.ext import commands

def embed(title=None, description=None, color=None):
    embed = discord.Embed(
        title=title,
        description=description,
        colour=color
    )
    return title, description, color, embed
