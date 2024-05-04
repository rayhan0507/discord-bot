from __future__ import annotations
import discord
from discord.ext import commands
import time
import random
import io
from discord import ui 
from contextlib import suppress
from jokeapi import Jokes
import datetime
from collections import defaultdict




bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())

user_message_count = defaultdict(int)
message_count = {}


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

# jabawan game matematika
greeting = ["hello", "hai"]
interaksi_salah = ["salah oy:x:", "yang bener aja:x:", "lu kelas berapa?:x:", "gak bisa ngitung ya:x:"]
interaksi_benar = [
    "anda sangat cerdas:white_check_mark:", "IQ 200:scream::white_check_mark:", "bener bang:white_check_mark:", "diatas rata-rata:white_check_mark:"
    "anda pintar:white_check_mark:", ":white_check_mark:", "ampun, bukan kaleng-kaleng:white_check_mark:", "jago banget:white_check_mark:", 
    "albert einstein:white_check_mark:"
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

class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(BlueButton(label="Tombol Biru", style=discord.ButtonStyle.primary, custom_id="button"))
        self.add_item(RedButton(label="Tombol Merah", custom_id="red_button"))
        self.add_item(GreenButton(label="Tombol Hijau", custom_id="green_button"))
        self.add_item(LinkButton(label="instagram", url="https://www.instagram.com/ryxadev/",))

    
#link button
class LinkButton(discord.ui.Button):
    def __init__(self, label: str, url: str):
        super().__init__(label=label, style = discord.ButtonStyle.link, url=url)
        
    async def callback(self, ctx: discord.ctx):
        await ctx.response.send_message("terima kasih telah mengfollow sosial media owner", ephemeral=True)
              
class SosmedView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(LinkButton(label="📱ryxagnrl", url="https://www.instagram.com/ryxagnrl/"))
        self.add_item(LinkButton(label="📱ryyxaaaa", url="https://www.instagram.com/ryyxaaaa/"))


#matematika -----------------------------------------------------------
class MathButton1(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle, custom_id: str):
        super().__init__(label=label, style=style, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):
        if self.label == "2":
            await interaction.response.send_message(random.choice(interaksi_benar))
        else: 
            await interaction.response.send_message(random.choice(interaksi_salah))


class MathButton1View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        buttons = [ 
           MathButton1(label="3", style=discord.ButtonStyle.blurple, custom_id="button1"),
           MathButton1(label="4", style=discord.ButtonStyle.blurple, custom_id="button2"),
           MathButton1(label="1", style=discord.ButtonStyle.blurple, custom_id="button3"),
           MathButton1(label="2", style=discord.ButtonStyle.blurple, custom_id="button4")
        ]
        random.shuffle(buttons)
        for button in buttons:
            self.add_item(button)
        

class MathButton2(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle, custom_id: str):
        super().__init__(label=label, style=style, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):
        if self.label == "6":
            await interaction.response.send_message(random.choice(interaksi_benar))
        else:
            await interaction.response.send_message(random.choice(interaksi_salah))
        
class MathButton2View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        buttons = [
            MathButton2(label="6", style=discord.ButtonStyle.blurple, custom_id="button5"),
            MathButton2(label="3", style=discord.ButtonStyle.blurple, custom_id="button6"),
            MathButton2(label="7", style=discord.ButtonStyle.blurple, custom_id="button7"),
            MathButton2(label="10", style=discord.ButtonStyle.blurple, custom_id="button8")
        ]
        random.shuffle(buttons)
        for button in buttons:
            self.add_item(button)

class MathButton3(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle, custom_id: str):
        super().__init__(label=label, style=style, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):

        if self.label == "-3":
            await interaction.response.send_message(random.choice(interaksi_benar))
        else:
            await interaction.response.send_message(random.choice(interaksi_salah))

class MathButton3View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        button = [
             MathButton3(label="-3", style=discord.ButtonStyle.blurple, custom_id="button9"),
            MathButton3(label="9", style=discord.ButtonStyle.blurple, custom_id="button10"),
            MathButton3(label="-6", style=discord.ButtonStyle.blurple, custom_id="button11"),
            MathButton3(label="3", style=discord.ButtonStyle.blurple, custom_id="button12")
        ]
        random.shuffle(button)
        for tombol in button:
            self.add_item(tombol)

class MathButton4(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle, custom_id: str):
        super().__init__(label=label, style=style, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):
        if self.label == "6":
            await interaction.response.send_message(random.choice(interaksi_benar))
        else:
            await interaction.response.send_message(random.choice(interaksi_salah))

class MathButton4View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        button = [
            MathButton4(label="8", style=discord.ButtonStyle.blurple, custom_id="button13"),
            MathButton4(label="4", style=discord.ButtonStyle.blurple, custom_id="button14"),
            MathButton4(label="-9", style=discord.ButtonStyle.blurple, custom_id="button15"),
            MathButton4(label="6", style=discord.ButtonStyle.blurple, custom_id="button16")
        ]
        random.shuffle(button)
        for tombol in button:
            self.add_item(tombol)

class MathButton5(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle, custom_id: str):
        super().__init__(label=label, style=style, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):
        if self.label == "12":
            await interaction.response.send_message(random.choice(interaksi_benar))
        else:
            await interaction.response.send_message(random.choice(interaksi_salah))

class MathButton5View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        buttons = [
            MathButton5(label="12", style=discord.ButtonStyle.blurple, custom_id="button17"),
            MathButton5(label="14", style=discord.ButtonStyle.blurple, custom_id="button18"),
            MathButton5(label="11", style=discord.ButtonStyle.blurple, custom_id="button19"),
            MathButton5(label="13", style=discord.ButtonStyle.blurple, custom_id="button20")
        ]
        random.shuffle(buttons)
        for tombol in buttons:
            self.add_item(tombol)

class MathButton6(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle, custom_id: str):
        super().__init__(label=label, style=style, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):
        if self.label == "13":
            await interaction.response.send_message(random.choice(interaksi_benar))
        else:
            await interaction.response.send_message(random.choice(interaksi_salah))

class MathButton6View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        buttons = [
            MathButton6(label="12", style=discord.ButtonStyle.blurple, custom_id="button21"),
            MathButton6(label="14", style=discord.ButtonStyle.blurple, custom_id="button22"),
            MathButton6(label="11", style=discord.ButtonStyle.blurple, custom_id="button23"),
            MathButton6(label="13", style=discord.ButtonStyle.blurple, custom_id="button24")
        ]
        random.shuffle(buttons)
        for tombol in buttons:
            self.add_item(tombol)
        
class MathButton7(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle, custom_id: str):
        super().__init__(label=label, style=style, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):
        if self.label == "48":
            await interaction.response.send_message(random.choice(interaksi_benar))
        else:
            await interaction.response.send_message(random.choice(interaksi_salah))

class MathButton7View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        buttons = [
            MathButton7(label="64", style=discord.ButtonStyle.blurple, custom_id="button25"),
            MathButton7(label="36", style=discord.ButtonStyle.blurple, custom_id="button26"),
            MathButton7(label="48", style=discord.ButtonStyle.blurple, custom_id="button27"),
            MathButton7(label="24", style=discord.ButtonStyle.blurple, custom_id="button28")
        ]
        random.shuffle(buttons)
        for tombol in buttons:
            self.add_item(tombol)

class MathButton8(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle, custom_id: str):
        super().__init__(label=label, style=style, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):
        if self.label == "-12":
            await interaction.response.send_message(random.choice(interaksi_benar))
        else:
            await interaction.response.send_message(random.choice(interaksi_salah))

class MathButton8View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        buttons = [
            MathButton8(label="9", style=discord.ButtonStyle.blurple, custom_id="button29"),
            MathButton8(label="-12", style=discord.ButtonStyle.blurple, custom_id="button30"),
            MathButton8(label="-11", style=discord.ButtonStyle.blurple, custom_id="button31"),
            MathButton8(label="-16", style=discord.ButtonStyle.blurple, custom_id="button32")
        ]
        random.shuffle(buttons)
        for tombol in buttons:
            self.add_item(tombol)



#drop down
class DropdownSelect1(discord.ui.Select):
    def __init__(self):      
            options=[
                discord.SelectOption(label="1", value="1", description="umur 1 tahun"),
                discord.SelectOption(label="2", value="2", description="umur 2 tahun"),
                discord.SelectOption(label="3", value="3", description="umur 3 tahun"),
            ]

            super().__init__(placeholder="what is your age?", options=options, min_values=1, max_values=1)
    
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"kamu memilih {self.values[0]} sebagai umur kamu dan {self.values[0]}")
        
        
class DropdownView1(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(DropdownSelect1())


class DropdownHelp(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="👋hi", value="!hi", description="menyapa anda"),
            discord.SelectOption(label="🌄selamatpagi", value="!selamatpagi", description="menyapa anda di pagi hari"),
            discord.SelectOption(label="🌃selamatmalam", value="!selamatmalam", description="menyapa anda di malam hari"),
            discord.SelectOption(label="🖩kalkulasi", value="!kalkulasi", description="membantu menghitung angka operasi"),
            discord.SelectOption(label="🎤join", value="!join", description="memasukan bot ke voice room"),
            discord.SelectOption(label="🔇leave", value="!leave", description="mengeluarkan bot dari voice room"),
            discord.SelectOption(label="📱sosmed", value="!sosmed", description="sosial media owner"),
            discord.SelectOption(label="😂canda", value="!canda", description="berbagai macam joke"),  
            discord.SelectOption(label="✏️other", value="/other", description="fitur lain"),
            
        ]
        super().__init__(placeholder="pilih perintah yang ingin kau bantu",options=options, min_values = 1, max_values = 1)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "!hi":
          await interaction.response.send_message(f"hi <@{interaction.user.id}>")
        elif self.values[0] == "!selamatpagi":
          await interaction.response.send_message(f"Selamat pagi juga <@{interaction.user.id}>!")
        elif self.values[0] == "!selamatmalam":
          await interaction.response.send_message("Selamat malam, waktunya untuk tidur :sleeping:")
        elif self.values[0] == "!kalkulasi":
          await interaction.response.send_message("Silakan ketik ekspresi matematika yang ingin Anda hitung setelah perintah `!kalkulasi`, misalnya `!kalkulasi 2 + 2`.")
        elif self.values[0] == "!join":
          await interaction.response.send_message("ketik !join untuk memasukan bot ke voice room")
        elif self.values[0] == "!leave":
          await interaction.response.send_message("ketik !leave untuk mengeluarkan bot dari voice room")
        elif self.values[0] == "!sosmed":
          view = SosmedView()
          embed = discord.Embed(title="ryxadev", 
                            url="https://www.instagram.com/ryxagrnl/", 
                            description="udah follow instagramnya owner server ini belum?, bisa juga mencari manual: @ryxagnrl", 
                            color=0x3399ff
                            )

          with open("C:\\Users\\USER\\Pictures\\Saved Pictures\\ryxaai.jpg", "rb") as file:
             image = file.read()

          embed.set_thumbnail(url="attachment://ryxaai.jpg") #thumbnail gambar
          embed.set_footer(text="ryxa general ai")
          embed.set_author(name="Social media owner")
      

          await interaction.response.send_message(embed=embed, view=view, file=discord.File(io.BytesIO(image), "ryxaai.jpg"))
          
        elif self.values[0] == "!canda":
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
            
          await interaction.response.send_message(ctx_content)        

        elif self.values[0] == "/other":
            embed = discord.Embed(title = "Fitur lain", color=0x3399ff)

            other_commands = {
               "/randomchat": "sebuah hal hal random dan unik",
               "/game": "beberapa game dengan bot",
               "/say": "tanyakan sesuatu kepada bot",
               "/botping": "menunjukan kecepatan ping dari bot anda",
               "/biner": "mengubah text atau angka ke dalam angka biner",
               "/copy_generator": "spam message generator"


            }

            for komentar, deskripsi in other_commands.items():
                if other_commands.items() == len(other_commands):
                   print("fitur other anda kurang")
                else:
                    embed.add_field(name=f"```{komentar}```", value=deskripsi, inline=True)
                    print(f"{interaction.user.mention} membuka fitur other embed")
    
            await interaction.response.send_message(embed=embed)   

class DropdownHelpView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(DropdownHelp())




    
@bot.event
async def on_message(ctx):
    ctx_content = ""

    if ctx.author == bot.user:
        return
    

    if ctx.content.startswith("!age"):
        await ctx.channel.send("Select your age:", view=DropdownView1())  
        


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
                            url="https://www.instagram.com/ryxagrnl/", 
                            description="udah follow instagramnya owner server ini belum?, bisa juga mencari manual: @ryxagnrl", 
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


    if ctx.content.startswith("!math"):
        print(f"{ctx.author.id} menggunakan command !math")
        await ctx.channel.send("jawablah dengan benar!")
        view_soal_1 = MathButton1View()
        view_soal_2 = MathButton2View()
        view_soal_3 = MathButton3View()
        view_soal_4 = MathButton4View()
        view_soal_5 = MathButton5View()
        view_soal_6 = MathButton6View()
        view_soal_7 = MathButton7View()
        view_soal_8 = MathButton8View()
        soal = [("1 + 1 = ?"), ("2 * 3 = ?"), ("3 - 6 = ?"), ("14 - 8 = ?"), 
                ("26 - 14"), ("39 / 3 = ?"), ("4 * 12 = ?"),("-3 * 4 = ?")]
        soal_jawaban = random.choice(soal)
        if soal_jawaban == soal[0]:
            await ctx.channel.send(f"Berapakah jawaban dari {soal_jawaban}", view=view_soal_1)
        elif soal_jawaban == soal[1]:
            await ctx.channel.send(f"Berapakah jawaban dari {soal_jawaban}", view=view_soal_2)
        elif soal_jawaban == soal[2]:
            await ctx.channel.send(f"Berapakah jawaban dari {soal_jawaban}", view=view_soal_3)
        elif soal_jawaban == soal[3]:
            await ctx.channel.send(f"Berapakah jawaban dari {soal_jawaban}", view=view_soal_4)
        elif soal_jawaban == soal[4]:
            await ctx.channel.send(f"Berapakah jawaban dari {soal_jawaban}", view=view_soal_5)
        elif soal_jawaban == soal[5]:
            await ctx.channel.send(f"Berapakah jawaban dari {soal_jawaban}", view=view_soal_6)
        elif soal_jawaban == soal[6]:
            await ctx.channel.send(f"Berapakah jawaban dari {soal_jawaban}", view=view_soal_7)
        elif soal_jawaban == soal[7]:
            await ctx.channel.send(f"Berapakah jawaban dari {soal_jawaban}", view=view_soal_8)
        else:
            None

    
    if ctx.author.bot:
        return  # abaikan pesan dari bot itu sendiri
    
    # Memeriksa jika pengguna sudah ada dalam dictionary
    if ctx.author.id in message_count:
        # Jika teks pesan sudah ada dalam dictionary, tambahkan jumlahnya
        if ctx.content in message_count[ctx.author.id]:
            message_count[ctx.author.id][ctx.content] += 1
        else:
            message_count[ctx.author.id][ctx.content] = 1
    else:
        message_count[ctx.author.id] = {ctx.content: 1}
    
    # Memeriksa jika pesan yang sama telah dikirim lebih dari 10 kali
    if message_count[ctx.author.id][ctx.content] > 10:
        await ctx.reply("jangan spam kocak :angry:")
    
    await bot.process_commands(ctx)

            

    


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
        "!leave": "mengeluarkan bot dari voice room",
        "!sosmed": "sosial media owner",
        "!canda": "berbagai macam joke",
        
        "/other": "fitur yang lain"

    }

    # Menambahkan bidang untuk setiap perintah
    for command, description in commands_info.items(): 
        if commands_info:
          embed.add_field(name=f"```{command}```", value=description, inline=True)
          print(f"{interaction.user.mention} menggunakan command help")

    await interaction.response.send_message(embed=embed, file=discord.File(io.BytesIO(image), "ryxaai.jpg"), view=DropdownHelpView())




#other
@bot.tree.command(name="other", description="berbagai macam fitur dari bot ini")
async def other(interaction = discord.Interaction):
    embed = discord.Embed(title = "Fitur lain", color=0x3399ff)

    other_commands = {
        "/randomchat": "sebuah hal hal random dan unik",
        "/game": "beberapa game dengan bot",
        "/say": "tanyakan sesuatu kepada bot",
        "/botping": "menunjukan kecepatan ping dari bot anda",
        "/biner": "mengubah text atau angka ke dalam angka biner",
        "/copy_generator": "spam message generator"


    }

    for komentar, deskripsi in other_commands.items():
        if other_commands.items() == len(other_commands):
           print("fitur other anda kurang")
        else:
           embed.add_field(name=f"```{komentar}```", value=deskripsi, inline=True)
           print(f"{interaction.user.mention} membuka fitur other embed")
    
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="game", description="berbagai macam game")
async def game(interaction: discord.Interaction):
    embed = discord.Embed(title="game", color=0x3399ff)
    games = {
        "/tebak angka": "menembak angka dari 1-10",
        "!math": "menjawab soal matematika mudah"
    }

    for isi, deskripsi in games.items():
        embed.add_field(name=f"```{isi}```", value=deskripsi, inline=True)
        print(f"{interaction.user.mention} menggunakan embed game")

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
        print(f"{interaction.user.mention} random_command")

    await interaction.response.send_message(embed=embed)




#hybrid command
@bot.hybrid_command(name="say", description="say something")
async def say(ctx: discord.ctx, text: str):
    response = ""
    if text == "hi":
        response = f"hi juga {ctx.author.mention}"
    elif text == "selamat pagi":
        response = f"selamat pagi juga {ctx.author.mention}"
    else:
        response = text

    await ctx.send(content=response)



@bot.hybrid_command(name="botping", description="menunjukan ping ms")
async def botping(ctx: discord.ctx, text: str):
    latency = round(bot.latency * 1000)
    view_ping = ""
    if text.lower() == "ping":
        view_ping = f"kecepatan bot kamu adalah {latency} ms"
        print(view_ping)
        await ctx.send(content=view_ping)
    else:
        await ctx.send("hanya bisa ketik ping")


@bot.hybrid_command(name="tebak_angka", description="Mainkan game menebak angka (1-10)")
async def tebak_angka(ctx: discord.ctx, angka: int):
    angka_random = random.randint(1, 10)  # Inisialisasi angka_random di luar loop
    while True:  # Gunakan while True untuk menjalankan loop tanpa kondisi yang spesifik
        if angka < angka_random:
            await ctx.send("Angka terlalu kecil. Coba lagi!")
        elif angka > angka_random:
            await ctx.send("Angka terlalu besar. Coba lagi!")
        else:
            await ctx.send(f"Selamat! Angka yang benar adalah {angka_random}. Anda menang!")
            break  
        return  

#text ke biner
@bot.hybrid_command(name="biner", description="mengkonversikan text ke biner")
async def biner(ctx: discord.ctx, text: str):
    if text.isdigit():
        angka_biner = format(int(text), "08b")
        await ctx.send(angka_biner)
        print("anda menggunakan teks to biner")
    elif text == "list":
        for i in range(11):
            biner2 = format(i, "08b")
            await ctx.send(f"angka {i} adalah {biner2}")
    else:
       biner = " ".join(format(ord(char), "08b") for char in text)
       await ctx.send(biner)
       print("anda menggunakan angka ke biner")


@bot.hybrid_command(name="copy_generator", description="membuat kata berulang")
async def copy(interaction: discord.Interaction, text:str, jumlah:int):
    if isinstance(text, (int, float, str) or isinstance(jumlah, (int,float))):
        copy_text = " ".join([text] * jumlah)
        await interaction.send(f"{copy_text} ", ephemeral = True)












try:
    bot.run("your token")
except Exception as e:
    print(f"terjadi kesalahan di bot anda: {e}")

 
