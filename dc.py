import os
import discord
import random
from discord.ext import commands
import youtube_dl
import asyncio
import time
from jokeapi import Jokes

bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())

sad = [('sedih aku mh'), ('nangis aku mh'), ('sedih aku'), ('aku sedih')]
sad_word = ['cengeng', 'jangan sedih :sad:', 'cengeng sekali', ':sad:', "jangan bersedih bang aku setia bersamamu"]
negatif_word = [('oceh'), ('cukup tau'), ('ckp tw'), ('cukup tw'),
                ('oceh bud')]
kata_negatif = ['baper', 'baperan']
menu_list = [
    'nasi goreng', 'bakso', 'ayam goreng', 'indomie', 'sup ayam', 'sayur',
    'nasi ayam', 'sop sayur', 'soto', 'salad', 'buah buahan'
]
help_list = [
    "!help", "!calculate", "!daftarmenumakanan", "!food", "!pesan", "!joke"
]
good_word = [('mantap'), ('riksa keren'), ('riksa keren sekali'),
             ('riksa pinter'), ('pinter bgt'), ('cerdas')]
answer_good_word = [
    'iya dong', ('gweh banget'), ('menggambarkan saya'), (':smirk:')
]

permintaan_word = [("beri 1 kata untuk saya")]
permintaan_answer = ["hitam","kamu tampan dan sigma:sunglasses:"]

bad_word = ["kontol", "anjing", "tolol"]

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


voice_bot = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': '-vn'}


@bot.event
async def on_ready():
  print('bot berhasil di nyalakan {0.user}'.format(bot))


@bot.event
async def on_member_join(member):
  channel = bot.get_channel(1174587014323109888)
  await channel.send(
      f'<@{member.id}> halo member baru selamat datang di server rexa')


@bot.event
async def on_ctx(ctx):
  if ctx.author == bot.user:
    

  if any(permintaan in ctx.content.lower() for permintaan in permintaan_word):
    await ctx.channel.send(random.choice(permintaan_answer))
    
  
  if any(sedih in ctx.content.lower() for sedih in sad):
    await ctx.channel.send(random.choice(sad_word))
    

  if any(negatif in ctx.content.lower() for negatif in negatif_word):
    await ctx.channel.send(random.choice(kata_negatif))
    

  if any(good in ctx.content.lower() for good in good_word):
    await ctx.channel.send(random.choice(answer_good_word))

  if any(bad in ctx.content.lower() for bad in bad_word):
    await ctx.channel.send(f'mohon untuk tidak berkata kasar, katakanlah kata yang sopan <@{ctx.author.id}>')

  if ctx.content.startswith('!hi ryxa'):
    await ctx.channel.send(f'hi juga <@{ctx.author.id}>')

  if ctx.content.startswith('!selamat pagi'):
    await ctx.channel.send('selamat pagi!')

  if ctx.content.startswith('!calculate'):
    expression = ctx.content[len('!calculate'):].strip()
    try:
      result = eval(expression)
      await ctx.channel.send(f'Hasil: {result}')
    except Exception as e:
      await ctx.channel.send(f'ada kesalahan ketik: {e}')

  if ctx.content.startswith('!search'):
    query = ctx.content[len('!search'):].strip()
    await ctx.channel.send(f'Searching for: {query}')



# daftar manakan  ----------------------------------------------------------------
  if ctx.content.startswith('!food'):
    await ctx.channel.send(
        'kami menyediakan banyak menu ketik !daftarmenumakanan untuk melihat menu'
    )

  if ctx.content.startswith('!daftarmenumakanan'):
    formatted_text = "```css\nDaftar Menu:\n"
    for menu in menu_list:
      formatted_text += f"- {menu}\n"
    formatted_text += "```"

    await ctx.channel.send(formatted_text)
    await ctx.channel.send('pilih sesuka anda :blush:')

  if ctx.content.startswith('!pesan'):
    choice = ctx.content[len('!pesan'):].strip()
    if choice in menu_list:
      await ctx.channel.send(f'{choice} di pesan')
    else:
      await ctx.channel.send(f'menu {choice} tidak tersedia')


# help ----------------------------------------------------------------

  if ctx.content.startswith('!help'):
    await ctx.channel.send('bisa saya bantu? :blush:')
    formatted_text = "```css\nPerintah:\n"
    for help in help_list:
      formatted_text += f'{help}\n'
    formatted_text += "```"

    await ctx.channel.send(formatted_text)

# join / leave
  if ctx.content.startswith('!join'):
    channel = ctx.author.voice.channel if ctx.author.voice else None
    if channel:
      voice_channel = await channel.connect()
      await ctx.channel.send(f"Berhasil masuk ke voice channel {channel}")
    else:
      await ctx.channel.send("Kamu tidak ada di voice channel")

  if ctx.content.startswith('!leave'):
    channel = ctx.author.voice.channel if ctx.author.voice else None
    voice_channel = ctx.guild.voice_bot
    if voice_channel:
      await voice_channel.disconnect()
      await ctx.channel.send(
          f"Berhasil keluar dari voice channel {channel}")
    else:
      await ctx.channel.send("kamu tidak ada di voice channel")


# play music
  if ctx.content.startswith('!play'):
    try:
      url = ctx.content.split()[1]
      if not ctx.guild.voice_bot:
        voice_channel = await ctx.author.voice.channel.connect()
        ctx.guild.voice_bot = voice_channel

      voice_channel = ctx.guild.voice_bot

      loop = asyncio.get_event_loop()
      data = await loop.run_in_executor(
          None, lambda: ytdl.extract_info(url, download=False))

      song = data["url"]
      player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

      voice_channel.play(player) 

    except Exception as err:
      print(err)
# joke 

  if ctx.content.startswith("!joke"):
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

  if any(sedih in ctx.content.lower() for sedih in sad):
    await ctx.channel.send(random.choice(sad_word))

  if any(negatif in ctx.content.lower() for negatif in negatif_word):
    await ctx.channel.send(random.choice(kata_negatif))


@bot.tree.command(name="hello", description="menyapa")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_ctx(f"hi {interaction.user.mention}, ini adalah slash komen semoga dengan fitur ini dapat membantu anda")

@bot.tree.command(name="selamatpagi", description="menyapa di pagi hari")
async def selamatpagi(interaction: discord.Interaction):
    await interaction.response.send_ctx(f"selamat pagi {interaction.user.mention}")

@bot.tree.command(name="selamatmalam", description="menyapa di malam hari")
async def selamatpagi(interaction: discord.Interaction):
    await interaction.response.send_ctx(f"selamat malam {interaction.user.mention}")

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
        "!embed": "menunjukan embed"
    }

    # Menambahkan bidang untuk setiap perintah
    for command, description in commands_info.items():
        if commands_info:
          embed.add_field(name=f"```{command}```", value=description, inline=True)

    await interaction.response.send_ctx(embed=embed, file=discord.File(io.BytesIO(image), "ryxaai.jpg"))



@bot.hybrid_command(name="say", description="say something")
async def say(interaction: discord.Interaction, text: str):
    await interaction.send(content=text)




try:
  bot.run("your TOKEN")
except Exception as e:
  print(f'Error: {e}')
