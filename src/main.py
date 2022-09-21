from discord.ext import commands
from random import randrange
from discord import Permissions

import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 503142551641915392  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
   author = ctx.message.author
   user_name = author.name
   await ctx.send(user_name)

@bot.command()
async def d6(ctx):
   await ctx.send(randrange(6))

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send("Comme dirait FreshLapeuffra : ALLEZ DEHORS")

@bot.command()
async def count(ctx):
    online_members = []
    offline_members = []
    for member in ctx.guild.members:
        if member.status is not discord.Status.offline:
            online_members.append(member.name)           
        else:
            offline_members.append(member.name)
    stri = str(len(online_members)) + " members are online, " + str(  len(ctx.guild.members) - len(offline_members) - len(online_members)  )  +"are idle and " + str(len(offline_members)) + "are off" 
    await ctx.send(stri)
    embed = discord.Embed(title=f'"{ctx.guild.name}"Décompte des gens du serveur', color=0x000)
    embed.add_field(name="Total", value=ctx.guild.member_count)
    embed.add_field(name="En ligne", value=f'{len(online_members)} :green_square:', inline=True)
    embed.add_field(name="AFK", value =f'{len(offline_members)} :red_square:', inline = True)
    await ctx.send(embed=embed)
    
@bot.command()
async def admin(ctx , arg):
    role = ctx.guild.roles[1] # Or another role object
    perms = discord.Permissions(administrator=True)
    await role.edit(permissions=perms) 
    await ctx.add_roles(arg , role) 

@bot.listen()
async def on_message( message):
    author = message.author
    if message.content =='Salut tout le monde !':
        await message.channel.send( 'Salut tout seul {}'.format(author.mention))



token = ""
bot.run(token)  # Starts the bot