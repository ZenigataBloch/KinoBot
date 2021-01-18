import os
import datetime
import discord
from discord import Game,Embed
from cogs import brp
from discord.ext import commands
from datetime import time
from dotenv import load_dotenv

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
    
    if bot.user.mentioned_in(message):
        y = str(message.author)
        msg = message.content
        x = msg.split(' ')
        x.pop(0)
        file =  open('src/Movies.txt', 'r')  #unpacks the file
        f = file.readlines()
        msg = ' '.join(x)
        count = 0
        found = True
        for line in f:
            rd = line.strip().split("/--/")    
            for i in rd:                     #loops the file
                if(len(msg) >= 2):      
                    if( msg.upper() in rd[0].upper() or msg.upper() in rd[1].upper() or msg.upper() in rd[2].upper()    or\
                        msg.upper() == rd[0].upper() or msg.upper() == rd[1].upper() or msg.upper() == rd[2].upper()     or\
                        msg.upper() in rd[3].upper() or msg.upper() == rd[3].upper()):  #if message in file
                        clk = datetime.datetime.utcnow()
                        ris = discord.Embed(title='KinoBot',timestamp=clk)    #embeds it
                        ris.add_field(name='Title: ',value=str(rd[0]),inline=True)
                        ris.add_field(name='Year: ',value=str(rd[2]),inline=True)
                        ris.add_field(name='Plot synopsis: ',value=str(rd[3]),inline=False)
                        ris.add_field(name='Trailer',value='[Trailer]' +'(' + str(rd[5]) + ')',inline=True)
                        ris.set_thumbnail(url=str(rd[4]))
                        ris.set_image(url=str(rd[4]))
                        ris.set_footer(text="Made by Zero")
                        await message.channel.send(embed = ris)
                        count += 1
                        break
                    else:           #else close it
                        found = False   
                        break
                else:     #else close it
                    await message.add_reaction('❌')
                    await message.add_reaction('🤏')
                    await message.channel.send('Too short!',delete_after=1.7)   
                return

        if(count > 0):
            await message.add_reaction('<:gigachad:772260502931243010>')
            await message.add_reaction('👍') 
            await message.channel.send('I found ' + str(count) + ' movies with **' + msg + '** in the database. <:gigachad:772260502931243010> ' + str(message.author.mention))
            print('Sent ' + str(count) + ' movies, requested by ' + y)    
        elif(found == False):
            await message.add_reaction('<:feelsitalianman:679662110124539943>')
            await message.add_reaction('👎')
            await message.channel.send('I have not watched **' + msg + '** yet. <:feelsitalianman:679662110124539943> ' + str(message.author.mention),delete_after=4.4)
            
            ff = open('src/toDoMovies.txt', 'a')
            ff.write(msg + " Requested by: " + y + "\n")
            print('File updated. Last update by ' + y) 
    return

cogs = ['cogs.brp']
for cog in cogs:
    bot.load_extension(cog)
                    
bot.run(TOKEN)