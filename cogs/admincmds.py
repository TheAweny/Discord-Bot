# This bot was created by Aweny developer.
# My GitHub - github.com/TheAweny
# Subscribe so as not to miss new updates, and also to support me.


import disnake
from disnake.ext import commands

class AdminCMDs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    @commands.has_permissions(kick_members=True, administrator=True)  # Available only to administrators And people who have access to the user kick
    async def kick(self, ctx, member: disnake.Member, *, reason="Not specified."):
        await ctx.send(f"The administrator {ctx.author.mention} kicked out the user {member.mention}")
        await member.kick(reason=reason)


    @commands.command()
    @commands.has_permissions(ban_members=True, administrator=True)  # Available only to administrators and people who have access to the user ban
    async def ban(self, ctx, member: disnake.Member, *, reason="Not specified.", ):
        await ctx.send(f"The administrator {ctx.author.mention} banned the user {member.mention}")
        await member.ban(reason=reason)


def setup(bot):
    bot.add_cog(AdminCMDs(bot))