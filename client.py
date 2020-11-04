import os
import discord

TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD_PROD']
CH_W = os.environ['CHANNEL_WELCOME']


class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        try:
            print(f'Detected message from {message.author}')
            if message.content.lower().startswith('hello'):
                if 'world' in message.content.lower():
                    await message.channel.send("Fuck off, that's my line!")
                else:
                    await message.channel.send(f'Hello {message.author}! :wink:')
        except Exception as e:
            print(e)

    async def on_member_join(self, member):
        try:
            print(f'Detected {member.name} joining server {member.guild}')
            await self.get_channel(int(CH_W)).send(f'{member.name} has joined the server. Pretend to care...')
        except Exception as e:
            print(e)


client = MyClient(intents=discord.Intents.all())


@client.event
async def on_connect():
    print(f'Module {os.path.basename(__file__)} has connected to Discord and is currently operating on the following server(s):')
    for guild in client.guilds:
        print(f'- Name: {guild.name} | ID: {guild.id}')


@client.event
async def on_ready():
    print('Ready to go!')


client.run(TOKEN)
