import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord.utils import get

token = "no no"

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print("Math200 bot is locked and loaded. Activation Succesful!")
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity = discord.Game("What's up peeps! @bg"))
    botChannel = bot.get_channel(735777596452634624)
    await botChannel.send("Bot is Online!")

@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')



@bot.command()
async def na(ctx, num, dueDate, link):
    assignmentsLabsChannel = bot.get_channel(735753445260132353)
    embedVar = discord.Embed(title=":warning: New Written Assignment Alert! :warning:", description="Chad has posted a new written assignemnt!", color=0x00ff00)
    embedVar.add_field(name="Written Assignment #" + num + " can be viewed at the link below!", value=link, inline=False)
    embedVar.add_field(name="Due Date: ", value=dueDate, inline=False)
    await assignmentsLabsChannel.send(embed=embedVar)
    await assignmentsLabsChannel.send('@here')


@bot.command()
async def nl(ctx, num, dueDate, link):
    assignmentsLabsChannel = bot.get_channel(735753445260132353)
    embedVar = discord.Embed(title=":warning: New Lab Assignment Alert! :warning:", description="Chad has posted a new lab assignemnt!", color=0x00ff00)
    embedVar.add_field(name="Lab Assignment #" + num + " can be viewed at the link below!", value=link, inline=False)
    embedVar.add_field(name="Due Date: ", value=dueDate, inline=False)
    await assignmentsLabsChannel.send(embed=embedVar)
    await assignmentsLabsChannel.send('@here')

@bot.command()
async def dd(ctx, name, dueDate, link):
    dueDateChannel = bot.get_channel(735971528843460618)
    embedVar = discord.Embed(title=":calendar_spiral: Due Date Alert! :calendar_spiral:", description="There is an assignment due today!", color=0x00ff00)
    embedVar.add_field(name=name, value=link, inline=False)
    embedVar.add_field(name="Due Date: ", value=dueDate, inline=False)
    await dueDateChannel.send(embed=embedVar)
    await dueDateChannel.send('@here')

@bot.command()
async def an(ctx, desc, blurbTitle, blurb):
    announcementsChannel = bot.get_channel(736001127518306315)
    embedVar = discord.Embed(title=":mega: New Announcement! :mega:", description=desc, color=0x00ff00)
    embedVar.add_field(name=blurbTitle, value=blurb, inline=False)
    await assignmentsLabsChannel.send(embed=embedVar)
    await assignmentsLabsChannel.send('@here')


bot.run(token)
