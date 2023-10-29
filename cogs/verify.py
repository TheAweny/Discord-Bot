# This bot was created by Aweny developer.
# My GitHub - github.com/TheAweny
# Subscribe so as not to miss new updates, and also to support me.


import disnake
from disnake.ext import commands

class VerifyModal(disnake.ui.Modal):
    def __init__(self, code):
        self.code = code
        components = [
            disnake.ui.TextInput(label="Enter the code (which is specified in the input field)", placeholder=self.code, custom_id="code")
        ]
        super().__init__(title="Verification", components=components, custom_id="verify_modal")

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        if self.code == int(interaction.text_values["code"]):
            role = interaction.guild.get_role(1158016393892089876) # Роль неверифицированного
            await interaction.author.add_roles(role)
            await interaction.response.send_message("✔ You have successfully passed verification!", ephemeral=True)
        else:
            await interaction.response.send_message("❌ Invalid code!", ephemeral=True)


class ButtonView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Verification", style=disnake.ButtonStyle.green, emoji="✅", custom_id="button1")
    async def button1(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        import random
        code = random.randint(1000, 9999)
        await interaction.response.send_modal(VerifyModal(code))


class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistents_views_added = False

    @commands.command()
    async def goverify(self, ctx):

        server_name = ctx.guild.name


        # Embed-Message
        embed = disnake.Embed(title="Verification on the server",
                              description="Please go through verification to get access to the main channels.\nYou can do this by clicking on the button below and entering the code.\n\nIf you have an error, contact the developers of the bot.",
                              colour=0xf56e00)

        embed.set_author(name=f"{server_name}")

        embed.set_footer(text="Verification",
                         icon_url="https://cdn1.iconfinder.com/data/icons/business-700/48/Approved-1024.png")
        await ctx.send(embed=embed, view=ButtonView())

    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_views_added:
            return
        verify_message_id = 0
        self.bot.add_view(ButtonView(), message_id=Message ID) # ID of the message with the button (So that after restarting, the button does not break)


def setup(bot):
    bot.add_cog(Verify(bot))
