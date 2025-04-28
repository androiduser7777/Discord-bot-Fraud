import discord
from discord.ext import commands
import random
import datetime

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot on valmis ja logis sisse kui {bot.user}')

@bot.command()
async def helpcommand(ctx):
    await ctx.send("Siin on sinu käsud: !nali, !coinflip, !ping, !dice, !mäng, !time")

@bot.command()
async def nali(ctx):
    await ctx.send("Miks tomat punaseks jäi? Sest ta nägi salatit!")

@bot.command()
async def coinflip(ctx):
    result = random.choice(['Heads', 'Tails'])
    await ctx.send(f'Tulemuseks on: {result}')

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  
    await ctx.send(f'Pong! Latentsus: {latency:.2f} ms')

@bot.command()
async def dice(ctx):
    result = random.randint(1, 6)
    await ctx.send(f'Täringuvise: {result}')

@bot.command()
async def mäng(ctx):
    games = ['Minecraft', 'Among Us', 'Valorant', 'Fortnite', 'Rocket League']
    game = random.choice(games)
    await ctx.send(f"Siin on üks mäng, mida proovida: {game}")

@bot.command()
async def time(ctx):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f'Praegune aeg: {current_time}')

bot.run('MTM2NjQxMzE3NDg5ODk1MDE4NQ.GfXIQ-.qoEZyM-iFlGbZm8P9ws7owWCnEGfJMwbHI9DFg')
