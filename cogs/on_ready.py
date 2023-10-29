# This bot was created by Aweny developer.
# My GitHub - github.com/TheAweny
# Subscribe so as not to miss new updates, and also to support me.


import disnake
from disnake.ext import commands

class ConsoleStartLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot {self.bot.user} is ready to work!")  # A message in the console about the bot's readiness


def setup(bot):
    bot.add_cog(ConsoleStartLog(bot))