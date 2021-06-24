import discord
from discord.ext import commands

client = discord.Client()

comando = commands.Bot(command_prefix = '>', case_insensitivite = True)

@client.event
async def on_ready():
    print('Logamo nessa porra!')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
        
    if (msg.content.startswith('Alo')):
        await msg.channel.send('Alo eu')

    if (msg.content.startswith('help')):
        vc = msg.author
        await vc.move_to(None)

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'testando-o-bot':
            await client.send_message(channel, 'Message to send when member joins')

@comando.command()
async def ola(ctx):
    await ctx.send(f'Ola, {ctx.author}')

@comando.command()
async def dado(ctx, numero):
    await ctx.send(numero)


client.run('ODU3MzA1MjQ1MjI2MjM3OTUy.YNNpug._NdY6AEKnKW6qcfKAOrko6rJlUM')

