import discord
import random,requests
from discord.ext import commands
from generador import get_duck_image_url
import os
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def meme(ctx):
  try:
    images = os.listdir('c:/python-course/memes/images')
    if images:
      img_name = random.choice(images)
      with open(f'c:/python-course/memes/images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    else:
      await ctx.send("¡No se encontraron memes en la carpeta 'imagenes'!")
  except FileNotFoundError:
    await ctx.send("¡No se encontraron memes en la carpeta 'imagenes'!")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command("duck")
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


bot.run('MTI0MDExMDQ4MDk2NjgxNTg2NQ.GhhuTR.-Yh8Lmv7f9dJ9tbC9rs5emSBc-GrgiVak6lFEY')


        













