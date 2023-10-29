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
        print(f" _______              _")
        print(f" |_   _| |__   ___   / \__      _____ _ __  _   _ ")
        print(f"   | | | '_ \ / _ \ / _ \ \ /\ / / _ \ '_ \| | | |")
        print(f"   | | | | | |  __// ___ \ V  V /  __/ | | | |_| |")
        print(f"   |_| |_| |_|\___/_/   \_\_/\_/ \___|_| |_|\__, |")
        print(f"                                            |___/ ")


def setup(bot):
    bot.add_cog(ConsoleStartLog(bot))