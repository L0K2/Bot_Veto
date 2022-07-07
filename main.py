import discord
from discord.ext import commands

import main

TOKEN = ""

client = commands.Bot(command_prefix='!')

md1 = 0

veto_count = 0

mapas_save = ["Inferno", "Mirage", "Nuke", "Overpass", "Dust2", "Vertigo", "Ancient"]
mapas = []
team1_pick = []
team2_pick = []

def restart():
    main.md1 = 0
    main.veto_count = 0
    main.mapas = main.mapas_save.copy()

@client.event
async def on_ready():
    print('Bot logado')
    print(f"Eu estou em {len(client.guilds)} servidores")

@client.command()
async def reset(ctx):
    restart()
    await ctx.send("Bot Reiniciado!")

@client.command()
async def teste(ctx):
    await ctx.send(f"{ctx.author.mention}O bot foi testado")

@client.command()
async def veto(ctx):
    restart()
    await ctx.send('!md1 ou !md3')

@client.command()
async def md1(ctx):
    main.md1 = 1
    await ctx.send('O map pool é: Inferno, Mirage, Nuke, Overpass, Dust2, Vertigo, Ancient')
    await ctx.send('Qual mapa remover(!ban + Nome do mapa): ')

@client.command()
async def md3(ctx):
    main.md1 = 3
    await ctx.send('O map pool é: Inferno, Mirage, Nuke, Overpass, Dust2, Vertigo, Ancient')
    await ctx.send('Qual mapa remover(!ban + Nome do mapa): ')

@client.command()
async def pick(ctx,arg):
    if ctx.author == client.user:
        return
    if veto_count == 2:
        index = mapas.index(arg)
        main.team1_pick = main.mapas.pop(index)
        await ctx.send(f"O time de {ctx.author.mention} Escolheu: ")
        await ctx.send(main.team1_pick)
        main.veto_count = main.veto_count + 1
        await ctx.send(f"Time 2 Escolha um mapa: {main.mapas}")
    if veto_count == 3:
        index = mapas.index(arg)
        main.team2_pick = main.mapas.pop(index)
        await ctx.send(f"O time de {ctx.author.mention} Escolheu: ")
        await ctx.send(main.team2_pick)
        main.veto_count = main.veto_count + 1
        await ctx.send(f"Time 1 continue os vetos: {main.mapas}")
    else:
        await ctx.send(f"{ctx.author.mention} Você precisa banir um mapa antes!")


@client.command()
async def ban(ctx,arg):
    if ctx.author == client.user:
        return
    if md1 == 3:
        if veto_count == 2:
                await ctx.send(f"{ctx.author.mention} Você precisa escolher um mapa agora!")
                print(".")
        else:
            print(".")
        if veto_count == 3:
                await ctx.send(f"{ctx.author.mention} Você precisa escolher um mapa agora!")
                print(".")
        else:
            while len(mapas) > 1:
                mapas.remove(arg)
                main.veto_count = main.veto_count + 1
                await ctx.send(f"{ctx.author.mention} Removeu {arg}")
                await ctx.send("Os mapas restantes são: ")
                await ctx.send(mapas)
                if len(mapas) != 1:
                    if veto_count == 1:
                        await ctx.send("Qual mapa remover:")
                    if veto_count == 2:
                        await ctx.send("Escolha Um mapa:")
                    if veto_count == 3:
                        await ctx.send("Escolha Um mapa:")
                    if veto_count > 3:
                        await ctx.send("Qual mapa remover:")
            if len(mapas) == 1:
                await ctx.send(f"O primeiro mapa de escolha do time 1 será: {main.team1_pick}")
                await ctx.send(f"O Segundo mapa de escolha do time 2 será: {main.team2_pick}")
                await ctx.send(f"O terceiro mapa, caso necessário será: {main.mapas}")
                restart()
    else:
            while len(mapas) > md1:
                    mapas.remove(arg)
                    main.veto_count = main.veto_count + 1
                    await ctx.send(f"{ctx.author.mention} Removeu {arg}")
                    await ctx.send("Os mapas restantes são: ")
                    await ctx.send(mapas)
                    if len(mapas) != md1:
                        await ctx.send("Qual mapa remover:")
            if len(mapas) == md1:
                        await ctx.send(f"O mapa jogado será:  {mapas}")
                        restart()



client.run(TOKEN)
