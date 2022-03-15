import discord
from discord.ext import commands

TOKEN = ""

client = commands.Bot(command_prefix='!')

mapas_save = ["Inferno", "Mirage", "Nuke", "Overpass", "Dust2", "Vertigo", "Ancient"]
mapas = ["Inferno", "Mirage", "Nuke", "Overpass", "Dust2", "Vertigo", "Ancient"]

@client.event
async def on_ready():
    print('Bot logado')


@client.command()
async def teste(ctx):
    await ctx.send('O bot foi testado')

@client.command()
async def veto(ctx):
    mapas = mapas_save
    await ctx.send('O map pool é: Inferno, Mirage, Nuke, Overpass, Dust2, Vertigo, Ancient')
    await ctx.send('Qual mapa remover(!ban + Nome do mapa): ')



@client.command()
async def ban(ctx,arg):
        ban1 = []
        num_de_ban = 0
        if num_de_ban == 0:
            mapas.remove(arg)
            ban1 = mapas
            num_de_ban = num_de_ban + 1
            await ctx.send("Os mapas restantes são: ")
            await ctx.send(ban1)
            await ctx.send("Qual mapa remover:")
        if len(mapas) == 1:
            num_de_ban = 2
            await ctx.send("O mapa jogado será: ", mapas)








client.run(TOKEN)
