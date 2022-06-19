import discord
from discord.ext import commands

TOKEN = ""

client = commands.Bot(command_prefix='!')

mapas_save = ["Inferno", "Mirage", "Nuke", "Overpass", "Dust2", "Vertigo", "Ancient"]
mapas = []

@client.event
async def on_ready():
    print('Bot logado')


@client.command()
async def teste(ctx):
    await ctx.send(f"{ctx.author.mention}O bot foi testado")

@client.command()
async def veto(ctx):
    main.mapas = main.mapas_save.copy()
    await ctx.send('O map pool é: Inferno, Mirage, Nuke, Overpass, Dust2, Vertigo, Ancient')
    await ctx.send('Qual mapa remover(!ban + Nome do mapa): ')




@client.command() #problema: bot lê suas próprias msg
async def ban(ctx,arg):
    if ctx.author == client.user:
        return
        while len(mapas) > 1:
            mapas.remove(arg)
            await ctx.send(f"{ctx.author.mention} Removeu {arg}")
            await ctx.send("Os mapas restantes são: ")
            await ctx.send(mapas)
            if len(mapas) != 1:
                await ctx.send("Qual mapa remover:")
    if len(mapas) == 1:
            await ctx.send(f"O mapa jogado será:  {mapas}")










client.run(TOKEN)
