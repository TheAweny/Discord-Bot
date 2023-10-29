# This bot was created by Aweny developer.
# My GitHub - github.com/TheAweny
# Subscribe so as not to miss new updates, and also to support me.


import os
import disnake
from disnake.ext import commands





activity = disnake.Activity(
    name="github.com/TheAweny",
    type=disnake.ActivityType.watching,
)

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all(), activity=activity)




@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")






bot.run("YOUR_BOT_TOKEN")  # Replace the inscription "YOUR_BOT_TOKEN" with your bot token.