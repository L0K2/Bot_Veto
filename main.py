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
    mapas = mapas_save #problema: mapas n definido
    await ctx.send('O map pool é: Inferno, Mirage, Nuke, Overpass, Dust2, Vertigo, Ancient')
    await ctx.send('Qual mapa remover(!ban + Nome do mapa): ')




@client.command() #problema: bot lê suas próprias msg/ não termina o codigo
async def ban(ctx,arg):
    if ctx.author == client.user:
        return
    while len(mapas) > 1:
            mapas.remove(arg)
            await ctx.send("Os mapas restantes são: ")
            await ctx.send(mapas)
            await ctx.send("Qual mapa remover:")
            await ctx.send(len(mapas))
    if len(mapas) == 1:
            await ctx.send(f"O mapa jogado será:  {mapas}")










client.run(TOKEN)
