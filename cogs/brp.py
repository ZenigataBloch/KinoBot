import random
import discord
from discord.ext import commands,tasks

class BotRichPresence(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.change_status.start()

    def cog_unload(self):
        self.change_status.cancel()

    @tasks.loop(seconds=60.0)
    async def change_status(self):
        file =  open('src/Movies.txt', 'r') 
        f = file.readlines()
        for line in f:
            rd = line.strip().split("/--/")    
            for i in rd:
                richpresencekino = [str(rd[0])]
                game = random.choice(richpresencekino)
                await self.bot.change_presence(status=discord.Status.do_not_disturb,activity=discord.Activity(type=discord.ActivityType.watching,name=str(game)))

    @change_status.before_loop
    async def before_change_status(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(BotRichPresence(bot))