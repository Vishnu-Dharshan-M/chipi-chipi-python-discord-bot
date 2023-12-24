#use pip install discord
#You can get FFmpegPCMAudio by downloading from the offical ffmpeg site
#download the ffmpeg, extract it and store it somewhere you remember
#afterwards copy the path and create a path variable for it
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

#This line determines the prefix of the bot, You can change the prefix as you want
client = commands.Bot(command_prefix="chipi.", intents = discord.Intents.all())

#This is not a command, rather an event that is triggered when the program is run. This is done in order to know that the program is online and active
@client.event
async def on_ready():
    print("chipi is chipi")

#This command is simply used to type out the dialouge to the text chat
@client.command()
async def talk(ctx):
    await ctx.send("chipi chipi chapa chapa dubi dubi daba daba")

#This command is used to send the chipi chipi meme gif to text chat
@client.command()
async def show(ctx):
    gif_url = "https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-10997735880837555564"
    await ctx.send(gif_url)

#This command displays all the possible commands
@client.command()
async def h(ctx):
    await ctx.send("Use these commands \n.talk --> chipi talk \n.show --> chipi dance \n.sing -->chipi sing")

#This command is used to join and play the chipi chipi audio
#If you want to change the name of the command itself, the place you have to make the change if in "async def sing(ctx)" change the sing to whatever command you want
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
        gif_url = "https://tenor.com/view/chipi-chapa-chipi-chipi-chipi-chipi-cat-chipi-chipi-dancing-cat-gif-1099773588083755556"
        await ctx.send(gif_url)

#please paste your bot's token in the quotes below
client.run("")
