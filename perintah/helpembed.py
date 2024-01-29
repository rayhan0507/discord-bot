import discord
from discord.ext import commands
import time
import random
import io

bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())

#memakai slash
#cara 1 
@bot.tree.command(name="help", description="membantu anda untuk mengetahui fitur dari bot ini")
async def helping(interaction: discord.Interaction):
    embed = discord.Embed(title="Ryxa General AI help", description="help", color=0x3399ff)
    with open("C:\\Users\\USER\\Pictures\\Saved Pictures\\ryxaai.jpg", "rb") as file:
          image = file.read()


    embed.set_thumbnail(url="attachment://ryxaai.jpg")
    embed.add_field(name="!hi", value="menyapa anda",inline=True) 
    embed.add_field(name="!selamat pagi", value="menyapa anda di pagi hari", inline=True)
    embed.add_field(name="!kalkulasi", value="membantu menghitung angka operasi", inline=True)
    embed.add_field(name="!join", value="memasukan bot ke voice room")
    embed.add_field(name="!leave", value="membantu mengeluarkan bot dari voice room", inline=True)
    embed.add_field(name="!embed", value="menunjukan embed", inline=True)
    embed.insert_field_at(2, name="!selamat malam", value="menyapa anda di malam hari", inline=True)
    # Anda dapat menambahkan lebih banyak bidang sesuai dengan kebutuhan

    await interaction.response.send_message(embed=embed, file=discord.File(io.BytesIO(image), "ryxaai.jpg"))

#cara 2
@bot.tree.command(name="help", description="membantu anda untuk mengetahui fitur dari bot ini")
async def helping(interaction: discord.Interaction):
    embed = discord.Embed(title="Ryxa General AI help", color=0x3399ff)
    with open("C:\\Users\\USER\\Pictures\\Saved Pictures\\ryxaai.jpg", "rb") as file:
        image = file.read()

    embed.set_thumbnail(url="attachment://ryxaai.jpg")

    # Dictionary untuk menyimpan informasi perintah
    commands_info = {
        "!hi": "menyapa anda",
        "!selamat pagi": "menyapa anda di pagi hari",
        "!selamat malam": "menyapa anda di malam hari",
        "!kalkulasi": "membantu menghitung angka operasi",
        "!join": "memasukan bot ke voice room",
        "!leave": "membantu mengeluarkan bot dari voice room",
        "!embed": "menunjukan embed"
    }

    # Menambahkan bidang untuk setiap perintah
    for command, description in commands_info.items():
        if commands_info:
          embed.add_field(name=f"```{command}```", value=description, inline=True)

    await interaction.response.send_message(embed=embed, file=discord.File(io.BytesIO(image), "ryxaai.jpg"))