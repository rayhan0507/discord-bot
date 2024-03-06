from __future__ import annotations
import discord
from discord.ext import commands
import time
import random
import io
from discord import ui 
from contextlib import suppress
from jokeapi import Jokes
import re


bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())


pertanyaan = [("satu kata untuk saya")]
jawaban = ["kamu ganteng :sunglasses:", "tampan", "jawir", "hitam legam :hot_face:", "raja ireng", 
           "niggas", "kamu orang dermawan :kissing_heart:", "negro","kamu tampan dan pemberani", "cina ireng", 
           "semok :yum:", "kamu sigma :sunglasses:"
           ]

kata_apresiasi = [("sip"), ("mantap"), ("keren"), ("siplah"), ("nah")]
kata_apresiasi_jawaban = ["keren bang", "keren nih", "keren ryxa", "siap"]

slash_selamat_pagi = ["selamat pagi @everyone semoga hari ini adalah hari yang indah", "selamat pagi waktunya sekolah", 
                      "bangun bangun udah pagi waktunya beraktivitas seperti biasa", "selamat pagi juga"
                      ]



@bot.event
async def on_ready():
    print("bot berhasil di aktifkan {0.user}".format(bot))
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

#tombol biru !tombol

class BlueButton(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle, custom_id: str):
        super().__init__(label=label, style=style, custom_id=custom_id)
        self.is_clicked = False

    async def callback(self, ctx: discord.ctx):
        if not self.is_clicked:
           await ctx.response.send_message("Tombol biru di tekan!", ephemeral=True)
           self.is_clicked = True
           self.disabled = True
           await ctx.response.send_message("Maaf, tombol hanya bisa diklik satu kali", ephemeral=True)
        

# tombol merah !tombol
class RedButton(discord.ui.Button):
    def __init__(self, label: str, custom_id: str):
        super().__init__(label=label, style=discord.ButtonStyle.red, custom_id=custom_id)

    async def callback(self, ctx: discord.ctx):
        await ctx.response.send_message("Tombol merah di tekan!", ephemeral=True)


# tombol hijau !tombol

class GreenButton(discord.ui.Button):
    def __init__(Self, label: str, custom_id: str):
        super().__init__(label=label, style = discord.ButtonStyle.green, custom_id=custom_id)

    async def callback(self, ctx: discord.ctx):
        await ctx.response.send_message("Tombol hijau di tekan", ephemeral=True)
#link button
class LinkButton(discord.ui.Button):
    def __init__(self, label: str, url: str):
        super().__init__(label=label, style = discord.ButtonStyle.link, url=url)
        
    async def callback(self, ctx: discord.ctx):
        await ctx.response.send_message("terima kasih telah mengfollow sosial media owner", ephemeral=True)
              



class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(BlueButton(label="Tombol Biru", style=discord.ButtonStyle.primary, custom_id="button"))
        self.add_item(RedButton(label="Tombol Merah", custom_id="red_button"))
        self.add_item(GreenButton(label="Tombol Hijau", custom_id="green_button"))
        self.add_item(LinkButton(label="instagram", url="https://www.instagram.com/ryxadev/",))

class SosmedView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(LinkButton(label="📱Sosial Media", url="https://www.instagram.com/ryxadev/"))


@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    
    ctx_content = ""

    if ctx.content.startswith("!tombol"):
        view = MyView()
        try:
           await ctx.channel.send("Ini adalah pesan dengan tombol!", view=view)
        except discord.errors.HTTPException as e:
            print(f"Terjadi kesalahan {e}")

    if ctx.content.startswith("!hi"):
        await ctx.channel.send(f"hi<@{ctx.author.id}>")

    if ctx.content.startswith("!selamat pagi"):
        await ctx.channel.send(f"selamat pagi juga <@{ctx.author.id}>!")

    if ctx.content.startswith("!selamat malam"):
        await ctx.channel.send("selamat malam waktunya untuk tidur :sleeping:")

    if any(pertanyaan1 in ctx.content.lower() for pertanyaan1 in pertanyaan):
       await ctx.channel.send(random.choice(jawaban))


    if any(apresiasi1 in ctx.content.lower() for apresiasi1 in kata_apresiasi):
        await ctx.channel.send(random.choice(kata_apresiasi_jawaban))

    
    if ctx.content.startswith("!sosmed"):
      view = SosmedView()
      embed = discord.Embed(title="ryxadev", 
                            url="https://www.instagram.com/ryxadev/", 
                            description="udah follow instagramnya owner server ini belum?, bisa juga mencari manual: @ryxadev", 
                            color=0x3399ff
                            )

      with open("C:\\Users\\USER\\Pictures\\Saved Pictures\\ryxaai.jpg", "rb") as file:
          image = file.read()

      embed.set_thumbnail(url="attachment://ryxaai.jpg") #thumbnail gambar
      embed.set_footer(text="ryxa general ai")
      embed.set_author(name="Social media owner")
      

      await ctx.channel.send(embed=embed, view=view, file=discord.File(io.BytesIO(image), "ryxaai.jpg"))
      
    
 

    # kalkulasi
    if ctx.content.startswith("!kalkulasi"):
        expression = ctx.content[len("!kalkulasi"):].strip()
        try:
            result = eval(expression)
            await ctx.channel.send(f"hasil: {result}")
        except Exception as e:
            await ctx.channel.send(f"ada kesalahan ketik: {e}")
            print(f"ada kesalahan {e}")


    


    if ctx.content.startswith("!canda"):
        try:
            j = await Jokes()
            blacklist = ["racist", "sexist"]  # Definisikan variabel blacklist
            joke = await j.get_joke(blacklist=blacklist)
        except Exception as e:
            print(f"Error while fetching joke: {e}")
            return

        ctx_content = ""
        if joke["type"] == "single":
            ctx_content = joke["joke"]
        else:
            ctx_content = joke["setup"]
            ctx_content += f" ||{joke['delivery']}||"
            
        await ctx.channel.send(ctx_content)

    if ctx.content.startswith("!join"): 
        channel = ctx.author.voice.channel if ctx.author.voice else None
        if channel:
            voice_channel = await channel.connect()
            await ctx.channel.send(f"Saya anda berhasil masuk {channel}")
            print("bot anda berhasil masuk ke voice room")
        else:
            await ctx.channel.send("anda tidak ada di voice room")
            print("anda tidak ada di voice room")

    if ctx.content.startswith("!leave"):
        channel = ctx.author.voice.channel if ctx.author.voice else None
        voice_channel = ctx.guild.voice_client
        if voice_channel:
            await voice_channel.disconnect()
            await ctx.channel.send('saya telah meninggalkan voice room')
            print("bot telah meninggalkan voice room")
        else:
            await ctx.channel.send("anda tidak ada di voice room")
            print("gagal")

    if ctx.content.startswith("!list"):
       list_jawaban = discord.Embed(title="List Jawaban")
       for kata in jawaban:
           list_jawaban.add_field(name="Jawaban", value=kata, inline=False)
       await ctx.channel.send(embed=list_jawaban)


    


# bot tree command
@bot.tree.command(name="hello", description="menyapa")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"hi {interaction.user.mention}, ini adalah slash komen semoga dengan fitur ini dapat membantu anda")

@bot.tree.command(name="selamatpagi", description="menyapa di pagi hari")
async def selamatpagi(interaction: discord.Interaction):
    await interaction.response.send_message(f"selamat pagi {interaction.user.mention}")

@bot.tree.command(name="selamatmalam", description="menyapa di malam hari")
async def selamatpagi(interaction: discord.Interaction):
    await interaction.response.send_message(f"selamat malam {interaction.user.mention}")

# /help
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
        "!sosmed": "menunjukan sosial media owner",
        "!joke": "berbagai macam joke",
        
        "/other": "fitur yang lain"

    }

    # Menambahkan bidang untuk setiap perintah
    for command, description in commands_info.items(): 
        if commands_info:
          embed.add_field(name=f"```{command}```", value=description, inline=True)

    await interaction.response.send_message(embed=embed, file=discord.File(io.BytesIO(image), "ryxaai.jpg"))





#other
@bot.tree.command(name="other", description="berbagai macam fitur dari bot ini")
async def other(interaction = discord.Interaction):
    embed = discord.Embed(title = "Fitur lain help", color=0x3399ff)

    other_commands = {
        "/randomchat": "sebuah hal hal random dan unik",
        "/game": "beberapa game dengan bot",
        "/say": "tanyakan sesuatu kepada bot",
        "/botping": "menunjukan kecepatan ping dari bot anda",
        "/biner": "mengubah text atau angka ke dalam angka biner"


    }

    for komentar, deskripsi in other_commands.items():
        if other_commands.items() == len(other_commands):
           print("fitur other anda kurang")
        else:
           embed.add_field(name=f"```{komentar}```", value=deskripsi, inline=True)
           print("anda membuka fitur other embed")
    
    await interaction.response.send_message(embed=embed)




#randomchat
@bot.tree.command(name = "randomchat", description = "hal hal random dan unik")
async def random1(interaction = discord.Interaction):
    embed = discord.Embed(title="pesan random", color=0x3399ff)

    random_command = {
        "satu kata untuk saya": "bot akan memanggil anda dengan panggilan yang menarik"
    }

    for komen, description1 in random_command.items():
        embed.add_field(name=f"```{komen}```", value=description1, inline=True)
        embed.set_author(name="cobalah pesan random di bawah ini!")
        print("anda menggunakan random_command")

    await interaction.response.send_message(embed=embed)






#hybrid command
@bot.hybrid_command(name="say", description="say something")
async def say(interaction: discord.cinteraction, text: str):
    response = ""
    if text == "hi":
        response = f"hi juga {interaction.author.mention}"
    elif text == "selamat pagi":
        response = f"selamat pagi juga {interaction.author.mention}"
    else:
        response = text

    await interaction.send(content=response)



@bot.hybrid_command(name="botping", description="menunjukan ping ms")
async def botping(interaction: discord.interaction, text: str):
    latency = round(bot.latency * 1000)
    view_ping = ""
    if text.lower() == "ping":
        view_ping = f"kecepatan bot kamu adalah {latency} ms"
        print(view_ping)
        await interaction.send(content=view_ping)
    else:
        await interaction.send("hanya bisa ketik ping")


@bot.hybrid_command(name="tebak_angka", description="Mainkan game menebak angka (1-10)")
async def tebak_angka(interaction: discord.interaction, angka: int):
    angka_random = random.randint(1, 10)  # Inisialisasi angka_random di luar loop
    while True:  # Gunakan while True untuk menjalankan loop tanpa kondisi yang spesifik
        if angka < angka_random:
            await interaction.send("Angka terlalu kecil. Coba lagi!")
        elif angka > angka_random:
            await interaction.send("Angka terlalu besar. Coba lagi!")
        else:
            await interaction.send(f"Selamat! Angka yang benar adalah {angka_random}. Anda menang!")
            break  # Keluar dari loop setelah pemain menebak dengan benar
        return  # Keluar dari perintah dan menunggu interaksi berikutnya  

#text ke biner
@bot.hybrid_command(name="biner", description="mengkonversikan text ke biner")
async def biner(interaction: discord.interaction, text: str):
    if text.isdigit():
        angka_biner = format(int(text), "08b")
        await interaction.send(angka_biner)
        print("anda menggunakan teks to biner")
    elif text == "list":
        for i in range(11):
            biner2 = format(i, "08b")
            await interaction.send(f"angka {i} adalah {biner2}")
    else:
       biner = " ".join(format(ord(char), "08b") for char in text)
       await interaction.send(biner)
       print("anda menggunakan angka ke biner")


@bot.hybrid_command(name="pencariemail", description="mencari sebuah email tersembunyi disuatu teks ataupun paragraf")
async def Email(interaction: discord.Interaction, text: str):
    if text:
         pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
         matches = re.findall(pattern, text)
         if len(matches) > 0:
             for nomor_urut, email in enumerate(matches, start=1):
                 await interaction.send("Email yang ditemukan:", ephemeral=True)
                 await interaction.send(f"{nomor_urut}. {email}", ephemeral=True)
         else:
             await interaction.send("Tidak ditemukan email dalam teks yang diberikan.")
    else:
        await interaction.send("Mohon berikan teks untuk mencari email.")









try:
    bot.run("YOUR BOT TOKER")
except Exception as e:
    print(f"terjadi kesalahan di bot anda: {e}")
