import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)
@bot.event
async def on_ready():
    print(f' We logged in as {bot.user}. ')

@bot.command()
async def merhaba(ctx):
    await ctx.send('Merhaba ben dünyada gerçekleşen herhangi bir gelişme hakkında bilgi veren bir discord botuyum.')

@bot.command()
async def konu(ctx):
    await ctx.send("Bilgi verdiğim konular çok fazla! Astronomi, doğa, bayramlar, yıl dönümleri ve çok daha fazlası... ")

@bot.command()
async def sicaklik_gunluk(ctx):
    await ctx.send("25 Mayıs Pazar: Sabah --> Parçalı bulutlu(25 derece) Akşam --> Yağmurlu(16-22 derece)")

@bot.command()
async def sicaklik_haftalik(ctx):
    await ctx.send("26 Mayıs - 1 Haziran(23 derece) --> 26 Mayıs(yağmurlu), 27 Mayıs(yağmurlu), 28 Mayıs(güneşli), 29 Mayıs(parçalı bulutlu), 30 Mayıs(yağmurlu), 31 Mayıs(yağmurlu), 1 Haziran(parçalı bulutlu)")

@bot.command()
async def havadurumu_aylik(ctx):
    await ctx.send("Mayıs(yağışlı ve parçalı bulutlu), Haziran(yağışlı ve güneşli), Temmuz(güneşli)")

@bot.command()
async def mayis_doğa(ctx):
    await ctx.send("Çiçek fırtınası ve güllerin açması ile karşılaşabilirsiniz.")

@bot.command()
async def haziran_doğa(ctx):
    await ctx.send("Ayın sonlarına doğru gündüzler yavaşça kısalmaya başlayacak.")

@bot.command()
async def temmuz_doğa(ctx):
    await ctx.send("Sıcaklıklar iyice yükselecek.")




bot.run("TOKEN")

