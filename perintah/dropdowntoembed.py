from typing import Any
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot anda berhasil di jalankan {0.user}".format(bot))
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands(0)")
    except Exception as e:
        print(f"kesalahan bot: {e}")




class DropSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="pertama", value="pertama", description="test"),
            discord.SelectOption(label="kedua", value="kedua", description="test"),
            
        ]
        
        super().__init__(placeholder="test drop down to embed", options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "pertama":
            embed = discord.Embed(
                title="title",
                description="description",
                color=0x3399ff
            )
            embed.add_field(name="test", value="test")

            await interaction.response.send_message(embed=embed)

        if self.values[0] == "kedua":
            await interaction.response.send_message("kedua")


class DropView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(DropSelect())



@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return

    if ctx.content.startswith("!hi"):
        await ctx.channel.send(f"hi juga <@{ctx.author.id}>")

    if ctx.content.startswith("!drop"):
        view = DropView()
        await ctx.channel.send("pilih salah satu", view=view)



try:
    bot.run("your token")
except Exception as e:
    print(f"terjadi kesalahan di bot anda: {e}")