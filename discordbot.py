from discord.ext import commands
import os
import traceback
import random
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()


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
    
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    
bot.run(token)
