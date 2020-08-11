from discord.ext import commands
import os
import traceback
import random
import asyncio

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
    await ctx.send('https://amazon.co.jp/gp/product/4758079501/')
    
@bot.command()
async def sasakoi2(ctx):
    await ctx.send('https://amazon.co.jp/gp/product/4758020744/')
    
@bot.command()
async def sasakoi3(ctx):
    await ctx.send('https://amazon.co.jp/gp/product/475802135X/')

@bot.command()
async def dedennne(ctx):
    i = random.random():
        if i<=0.1:
        await ctx.send('https://app-date.net/dendedendendendedenne/')
        elif i<=0.2:
        await ctx.send('https://app-date.net/cannededenne/')
        elif i<=0.3:
        await ctx.send('https://app-date.net/7thdedenne/')
        elif i<=0.4:
        await ctx.send('https://zalwa.net/LetsGoDedenne')
        elif i<=0.5:
        await ctx.send('https://app-date.net/dedenne_oranne/')
        elif i<=0.6:
        await ctx.send('https://app-date.net/ennedednednednededned/')
        elif i<=0.7:
        await ctx.send('https://app-date.net/ultra_dedeltal/')
        elif i<=0.8:
        await ctx.send('http://camptothecin.blog.jp/archives/1064126950.html')
        elif i<=0.9:
        await ctx.send('http://camptothecin.blog.jp/archives/1067492467.html')
        else:
        await ctx.send('https://zalwa.net/radishnne')
    
bot.run(token)
