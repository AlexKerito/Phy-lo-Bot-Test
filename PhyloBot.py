import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def Saludo(ctx, Persona):
    await ctx.send("Hola "+Persona+", Algo de lo que quieras hablar?")

@bot.command()
async def Suma(ctx, Num1, Num2):
    await ctx.send(int(Num1)+int(Num2))

@bot.command()
async def Contraseña(ctx, num):
    await ctx.send(f"Tu contaseña Random es {gen_pass(int(num))}, q opinas?")

import random

@bot.command()
async def DatoRandom(ctx):
    Datos = [
        "Sabías que mi dueño está desarrollando Mental Disasters?",
        "Soy un bot muy eficaz, por no decir que apenas tengo 3 funciones, y esta. DJKFLADSJFAS",
        "Estoy full aburrido, suelo jugar roblox, y tu?"
    ]
    Seleccionado = Datos[random.randint(0, 2)]
    print(Seleccionado)
    await ctx.send(Seleccionado)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

import os

Images = os.listdir('Files/Images')

@bot.command()
async def mem(ctx):
    with open(f'Files/Images/{Images[random.randint(0, len(Images))-1]}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

import requests

def get_dog_image_url():    
    url = 'https://api.furry.ist/furry-img/?format=json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('furry')
async def furry(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run('TOKEN')
