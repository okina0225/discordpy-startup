from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def mewtwo(ctx):
    await ctx.send('みゅー')
    
@bot.command()
async def sasakoi1(ctx):
    await ctx.send('https://amazon.co.jp/dp/B07T18R48L/')
    
@bot.command()
async def sasakoi2(ctx):
    await ctx.send('https://amazon.co.jp/dp/B083TF11SS/')
    
@bot.command()
async def sasakoi3(ctx):
    await ctx.send('https://amazon.co.jp/dp/B08CXH9K34/')
    
bot.run(token)
