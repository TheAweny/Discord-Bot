# This bot was created by Aweny developer.
# My GitHub - github.com/TheAweny
# Subscribe so as not to miss new updates, and also to support me.


import disnake
from disnake.ext import commands

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.author}, you don't have enough rights to execute this command!")  #{ ctx.author} is a reference to the author of the message, remove it if you don't need it.
        elif isinstance(error, commands.CommandNotFound):
            embed = disnake.Embed(
                title="The command was entered incorrectly!",
                color=0xff0000 # Red
            )

            await ctx.reply(embed=embed) # Sending an Embed message


def setup(bot):
    bot.add_cog(Errors(bot))