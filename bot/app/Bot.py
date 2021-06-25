import discord
import json
from discord.ext import commands

def ler_json(arq):
    with open(arq, 'r', encoding='utf8') as f:
        return json.load(f)

config = ler_json('config.json')

token = config['token']

client = discord.Client()

comando = commands.Bot(command_prefix = '>', case_insensitivite = True)

@client.event
async def on_ready():
    print('Logamo nessa porra!')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
        
    '''
        Enviando uma mensagem no canal -> channel.send(msg)
        Nesse caso, peguei o canal, pelo contexto da mensagem enviada
    '''
    if (msg.content.startswith('Alo')):
        await msg.channel.send('Alo eu')

    '''
        Para remover um usuario do canal de voz -> user.move_to(None)
        Nesse caso, peguei o user pelo autor da mensagem
    '''
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


client.run(token)

