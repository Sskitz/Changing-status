import discord
from itertools import cycle
from discord.ext import commands, tasks

status = cycle(['Add ur text here','ur text here','ur text here','ur text here'])  # you can add as much as you want EX: 'Stiizzy cat is hot','Name'

bot = commands.Bot(command_prefix="!") # prefix will not be used for changng status

@bot.event
async def on_ready():
    print("Changing Status started")
    change_status.start()

@tasks.loop(seconds=5) # change to how many secs you want - 5 is best
async def change_status(): 

 await bot.change_presence(activity=discord.Game(next(status)))

bot.run("Your Token here", bot=False)


#made by stiizzy cat 
# not my fault if you get disabled
