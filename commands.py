import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD_PROD']


@bot.command()
async def ugabuga(ctx):
    await ctx.channel.send(f'Get ready to RRRRRRRRUMBLE!!!')


@bot.event
async def on_connect():
    print(f'Module {os.path.basename(__file__)} has connected to Discord and is currently operating on the following server(s):')
    for guild in bot.guilds:
        print(f'- Name: {guild.name} | ID: {guild.id}')


@bot.event
async def on_ready():
    print('Ready to go!')

bot.run(TOKEN)
