import os
import datetime
import discord
from discord import Game,Embed
from cogs import brp
from discord.ext import commands
from datetime import time
from dotenv import load_dotenv
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="kino",
)

kino = db.cursor()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#client = discord.Client()
bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print(f'{bot.user} is here.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.bot:
        return

    if message.content.startswith('!') or message.content.startswith('!!')  or message.content.startswith('.'):
        return
    
    if message.content.startswith('??'):
        x = kino.execute(f"SELECT title FROM Movie where title = x")

        for x in kino:
            print(x)

bot.run(TOKEN)