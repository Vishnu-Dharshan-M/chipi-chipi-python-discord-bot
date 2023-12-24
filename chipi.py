import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

client = commands.Bot(command_prefix="chipi.", intents = discord.Intents.all())

@client.event
async def on_ready():
    print("chipi is chipi")

@client.command()
async def talk(ctx):
    await ctx.send("chipi chipi chapa chapa dubi dubi daba daba")

@client.command()
async def show(ctx):
    gif_url = "https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564"
    await ctx.send(gif_url)

@client.command()
async def h(ctx):
    await ctx.send("Use these commands \n.talk --> chipi talk \n.show --> chipi dance \n.sing -->chipi sing")

@client.command()
async def sing(ctx):
    if not ctx.author.voice:
        sad_url = "https://tenor.com/view/sad-cat-gif-26527456"
        await ctx.send(sad_url)
        await ctx.send("why you bully chipi, you no in channel!!!")
    else:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        source = FFmpegPCMAudio('chipi_audio.wav')
        player = vc.play(source)
        gif_url = "https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564"
        await ctx.send(gif_url)


client.run("MTE4ODEzMTI3MDAwNjQyNzc2OA.GQgZOs.1I1or5ZEimFSfCVkdpXkrT-wzq3zaaslK_3sX8")

#sad_url = "https://tenor.com/view/sad-cat-gif-26527456"
#await ctx.send(sad_url)