from nextcord import Intents
from nextcord.ext import commands
from datetime import date

import json
import datetime
import asyncio
import os

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('I love wife!')


@bot.command(name="nomi")
async def SendMessage(nomi):
    await nomi.send('bees knees')

mesaj = ' days left for Christmass!!! <@&973708149234229288>'


async def daily_message():
    this_year = date.today().year
    christmas = date(this_year, 12, 25)
    day_to_new_year = christmas - date.today()
    now = datetime.datetime.now()
    then = now.replace(hour=1, minute=00)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)
    channel = bot.get_channel(973708460648718376)
    await channel.send(str(day_to_new_year.days)+mesaj)


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}')
    await daily_message()

if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])
