# This bot was created by Aweny developer.
# My GitHub - github.com/TheAweny
# Subscribe so as not to miss new updates, and also to support me.


import disnake
from disnake.ext import commands
import time

class ClearChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="clear", description="Clearing the chat.")
    @commands.has_permissions(administrator=True)   # Available only to people with administrator rights
    async def clear(self, ctx):
        await ctx.send("The chat will be cleared in 5 seconds.")  # Cleaning Announcement
        time.sleep(5)  # Delay of 5 seconds
        await ctx.channel.purge()


def setup(bot):
    bot.add_cog(ClearChat(bot))