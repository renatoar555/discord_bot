import discord
import json
from discord.ext import commands

def ler_json(arq):
    with open(arq, 'r', encoding='utf8') as f:
        return json.load(f)

config = ler_json('config.json')

token = config['token']

bot = commands.Bot(command_prefix = '/', case_insensitivite = True)

@bot.event
async def on_ready():
    print('Logamo nessa porra!')

@bot.event
async def on_message(msg):
    if (msg.author == bot.user):
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

    await bot.process_commands(msg)

@bot.command()
async def ola(ctx):
    return await ctx.send(f'Ola, {ctx.author}')

@bot.command()
async def dado(ctx, numero):
    return await ctx.send(numero)

@bot.command()
async def sorteio(ctx, um, dois):
    param_num_pessoas = '*'
    param_num_grupos = '_'
    num_pessoas = 0
    num_grupos = 0
    if (um != None and um.startswith(param_num_pessoas)):
        num_pessoas = int(um[1:])
    elif (um != None and um.startswith(param_num_grupos)):
        num_grupos = int(um[1:])
    
    if (dois != None and dois.startswith(param_num_pessoas)):
        num_pessoas = int(dois[1:])
    elif (dois != None and dois.startswith(param_num_grupos)):
        num_grupos = int(dois[1:])

    return await ctx.send(f'Número de pessoas: {num_pessoas}, e número de grupos {num_grupos}')

bot.run(token)