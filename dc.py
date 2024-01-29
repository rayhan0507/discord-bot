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
async def on_message(message):
  if message.author == bot.user:
    

  if any(permintaan in message.content.lower() for permintaan in permintaan_word):
    await message.channel.send(random.choice(permintaan_answer))
    
  
  if any(sedih in message.content.lower() for sedih in sad):
    await message.channel.send(random.choice(sad_word))
    

  if any(negatif in message.content.lower() for negatif in negatif_word):
    await message.channel.send(random.choice(kata_negatif))
    

  if any(good in message.content.lower() for good in good_word):
    await message.channel.send(random.choice(answer_good_word))

  if any(bad in message.content.lower() for bad in bad_word):
    await message.channel.send(f'mohon untuk tidak berkata kasar, katakanlah kata yang sopan <@{message.author.id}>')

  if message.content.startswith('!hi ryxa'):
    await message.channel.send(f'hi juga <@{message.author.id}>')

  if message.content.startswith('!selamat pagi'):
    await message.channel.send('selamat pagi!')

  if message.content.startswith('!calculate'):
    expression = message.content[len('!calculate'):].strip()
    try:
      result = eval(expression)
      await message.channel.send(f'Hasil: {result}')
    except Exception as e:
      await message.channel.send(f'ada kesalahan ketik: {e}')

  if message.content.startswith('!search'):
    query = message.content[len('!search'):].strip()
    await message.channel.send(f'Searching for: {query}')



# daftar manakan  ----------------------------------------------------------------
  if message.content.startswith('!food'):
    await message.channel.send(
        'kami menyediakan banyak menu ketik !daftarmenumakanan untuk melihat menu'
    )

  if message.content.startswith('!daftarmenumakanan'):
    formatted_text = "```css\nDaftar Menu:\n"
    for menu in menu_list:
      formatted_text += f"- {menu}\n"
    formatted_text += "```"

    await message.channel.send(formatted_text)
    await message.channel.send('pilih sesuka anda :blush:')

  if message.content.startswith('!pesan'):
    choice = message.content[len('!pesan'):].strip()
    if choice in menu_list:
      await message.channel.send(f'{choice} di pesan')
    else:
      await message.channel.send(f'menu {choice} tidak tersedia')


# help ----------------------------------------------------------------

  if message.content.startswith('!help'):
    await message.channel.send('bisa saya bantu? :blush:')
    formatted_text = "```css\nPerintah:\n"
    for help in help_list:
      formatted_text += f'{help}\n'
    formatted_text += "```"

    await message.channel.send(formatted_text)

# join / leave
  if message.content.startswith('!join'):
    channel = message.author.voice.channel if message.author.voice else None
    if channel:
      voice_channel = await channel.connect()
      await message.channel.send(f"Berhasil masuk ke voice channel {channel}")
    else:
      await message.channel.send("Kamu tidak ada di voice channel")

  if message.content.startswith('!leave'):
    channel = message.author.voice.channel if message.author.voice else None
    voice_channel = message.guild.voice_bot
    if voice_channel:
      await voice_channel.disconnect()
      await message.channel.send(
          f"Berhasil keluar dari voice channel {channel}")
    else:
      await message.channel.send("kamu tidak ada di voice channel")


# play music
  if message.content.startswith('!play'):
    try:
      url = message.content.split()[1]
      if not message.guild.voice_bot:
        voice_channel = await message.author.voice.channel.connect()
        message.guild.voice_bot = voice_channel

      voice_channel = message.guild.voice_bot

      loop = asyncio.get_event_loop()
      data = await loop.run_in_executor(
          None, lambda: ytdl.extract_info(url, download=False))

      song = data["url"]
      player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

      voice_channel.play(player) 

    except Exception as err:
      print(err)
# joke 

  if message.content.startswith("!joke"):
    try:
        j = await Jokes()
        blacklist = ["racist", "sexist"]  # Definisikan variabel blacklist
        joke = await j.get_joke(blacklist=blacklist)
    except Exception as e:
        print(f"Error while fetching joke: {e}")
        return

    message_content = ""
    if joke["type"] == "single":
        message_content = joke["joke"]
    else:
        message_content = joke["setup"]
        message_content += f" ||{joke['delivery']}||"

    await message.channel.send(message_content)

  if any(sedih in message.content.lower() for sedih in sad):
    await message.channel.send(random.choice(sad_word))

  if any(negatif in message.content.lower() for negatif in negatif_word):
    await message.channel.send(random.choice(kata_negatif))


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
        "!embed": "menunjukan embed"
    }

    # Menambahkan bidang untuk setiap perintah
    for command, description in commands_info.items():
        if commands_info:
          embed.add_field(name=f"```{command}```", value=description, inline=True)

    await interaction.response.send_message(embed=embed, file=discord.File(io.BytesIO(image), "ryxaai.jpg"))



@bot.hybrid_command(name="say", description="say something")
async def say(interaction: discord.Interaction, text: str):
    await interaction.send(content=text)




try:
  bot.run("your TOKEN")
except Exception as e:
  print(f'Error: {e}')
