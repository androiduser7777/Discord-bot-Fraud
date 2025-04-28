import discord
from discord.ext import commands
import random
import datetime

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

user_money = {}

@bot.event
async def on_ready():
    print(f'Bot on valmis {bot.user}')

@bot.command()
async def helpcommand(ctx):
    await ctx.send("Käsud: !nali, !coinflip, !ping, !dice, !mäng, !time, !roulette")

naljad = [
    "Miks tomat punaseks jäi? Sest ta nägi salatit!",
    "Miks matemaatik ei suutnud oma päeva alustada? Ta oli ikka veel hommikuses 'sümbioosis'!",
    "Kuidas programmeerija mõtleb? 'Tõrge? Mis tõrge? Kõik on 'debug'.",
    "Mis on programmeerija lemmik toiduaine? 'Byte'!",
    "Kuidas saab teadlane teaduslikult lõbutsema? 'Aine ja 'beebipüree' kombinatsiooniga!",
    "Miks õpetaja armastab matemaatikat? Sest see on alati 'lahendatav'.",
    "Kuidas läheb filosoofide kohtumine? Üks ütleb: 'Kuidas see sind huvitab?' ja teine vastab: 'Miks mitte?!'",
    "Miks piraadid armastavad interneti sirvimist? Sest neil on alati 'URL-ide' peal!",
    "Kuidas suudab ajaloohuviline kiiresti sõpru leida? Lihtsalt 'pöörates'!",
    "Kuidas öelda, et teadlane on tõesti väsinud? Ta lihtsalt ütles: 'Ma ei suuda enam mõõta!'",
    "Miks oli sotsioloogil raskusi kaalu kaotamisega? Ta ei saanud oma 'süsteemi' kokku!",
    "Kuidas jääb bioloogiline test täiesti igavaks? Kui on ainult 'südametunnistus'.",
    "Miks teadlane ei räägi kunagi oma saladustest? Ta ei taha, et kõik tema 'geneetilised' asjad oleksid teada!",
    "Miks ei tohi kunagi masinaga magama minna? Sest see võib sul 'bugi' külge jääda!",
    "Mis on kohtumine ilma naljata? Tundmatu ja igav!"
]

@bot.command()
async def nali(ctx):
    valitud_nali = random.choice(naljad)
    await ctx.send(valitud_nali)

@bot.command()
async def coinflip(ctx):
    result = random.choice(['Kull', 'Kiri'])
    await ctx.send(f'Tulemus: {result}')

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  
    await ctx.send(f'Ping!  {latency:.2f} ms')

@bot.command()
async def dice(ctx):
    result = random.randint(1, 6)
    await ctx.send(f'Täringuvise: {result}')

@bot.command()
async def mäng(ctx):
    games = ['Minecraft', 'CS2', 'GTA', 'Fortnite', 'Rocket League']
    game = random.choice(games)
    await ctx.send(f"Siin on üks mäng, mida proovida: {game}")

@bot.command()
async def time(ctx):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f'Praegune aeg: {current_time}')

@bot.command()
async def roulette(ctx, bet: str, amount: int):
    """Kasutaja saab mängida ruletti, panustades kas punasele, mustale või rohelisele"""
    
    user = ctx.author
    
    if user.id not in user_money:
        user_money[user.id] = 1000  

    if bet not in ['red', 'black', 'green']:
        await ctx.send("Palun vali kehtiv panus! Kas valid punase, musta või rohelise.")
        return

    if user_money.get(user.id, 0) < amount:
        await ctx.send(f"Sul ei ole piisavalt raha, et teha panust {amount} münti!")
        return

    roulette_wheel = ['red'] * 18 + ['black'] * 18 + ['green']
    result = random.choice(roulette_wheel)  

    await ctx.send(f"Ruletti keerati ja tuli: **{result}**!")

    if bet == result:
        user_money[user.id] = user_money.get(user.id, 0) + amount  
        await ctx.send(f"Palju õnne, sa võitsid {amount} münti! Sul on nüüd {user_money[user.id]} münti.")
    else:
        user_money[user.id] = user_money.get(user.id, 0) - amount  
        await ctx.send(f"Kahjuks sa kaotasid {amount} münti! Sul on nüüd {user_money[user.id]} münti.")

    if user_money[user.id] <= 0:
        await ctx.send(f"Sul on raha otsas, kuid saad ikka mängida! Raha võib minna miinusesse, kui jätkad mängimist.")

bot.run('Token')  

