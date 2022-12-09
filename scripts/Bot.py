TOKEN = "" # Never push your token to GitHub!

import discord
from discord import app_commands
import asyncio
import random
import youtube_dl
import pafy

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

GREETING = ['Hallo', 'Hey', 'Goededag', 'Sup', 'Heyo']
COMMANDS = 'Commands, Decide on, Willo play, Willo skip, Willo pause, Willo continue, Willo queue, Willo leave'

class Player():
    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        self.names = []
    
    def play(self, voice, url):
        voice.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)), after= lambda error: self.bot.loop.create_task(self.next(voice)))

    async def next(self, voice):
        if len(self.queue) > 0:
            voice.stop()
            self.play(voice, self.queue[0])
            self.queue.pop(0)
            self.names.pop(0)

musicbot = Player(bot)

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await tree.sync()
    print(f'We have logged in as {bot.user}, ready to terrorize the Luditserver.')

@tree.command(name="test", description="Testing!")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("I'm working!")

@tree.command(name="help", description="Fine, I'll show you my commands!")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(COMMANDS)

@tree.command(name="clear", description="Clears a given amount of messages.")
@app_commands.checks.has_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, amount: int):
    await interaction.response.defer(ephemeral=True)
    await interaction.channel.purge(limit=amount)
    await interaction.followup.send("Cleared the chat!")

@tree.error
async def on_app_command_error(interaction, error):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message(error, ephemeral =True)
    else: raise error

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # commands
    if message.content.lower().startswith('commands'):
        if message.author.id == 254534396390932491:
            await message.channel.send(COMMANDS)
        else:
            await message.channel.send('Jij bent mijn baas niet. I am a strong and independant bot. Slay.')
    
    if message.content.lower().startswith('decide on'):
        content = message.content[9:]
        choices = []
        while ',' in content:
            idx = content.index(',')
            arg = content[:idx]
            content = content[idx+2:]
            choices += [arg]
        arg = content
        choices += [arg]
        await message.channel.send(random.choice(choices))
    
    if message.content.lower().startswith('willo play'):
        content = message.content[11:]
        try:
            voiceChannel = discord.utils.get(message.author.guild.voice_channels, name=message.author.voice.channel.name)
            await voiceChannel.connect()
            voice = discord.utils.get(bot.voice_clients, guild=message.author.guild)

        except:
            voice = discord.utils.get(bot.voice_clients, guild=message.author.guild)
            if voice == None:
                await message.channel.send('Something went wrong. Are you even in a channel?')
                return
            else:
                pass
        
        if message.content == ('willo play') or message.content == ('willo play '):
            return
        elif voice.is_playing():
            try:
                if not ("youtube.com/watch?" in content or "https://youtu.be/" in content):
                    info = await bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet": True}).extract_info(f"ytsearch1:{content}", download=False, ie_key="YoutubeSearch"))
                    yturl = [entry["webpage_url"] for entry in info["entries"]]    
                else:
                    yturl = [content]
                    
                url = pafy.new(yturl[0]).getbestaudio().url
                await message.channel.send(f"Added {yturl[0]} to queue!")
                musicbot.queue += [url]
                musicbot.names += [yturl]
            except:
                return await message.channel.send("Not so fast!")
                
        else:
            try:
                if not ("youtube.com/watch?" in content or "https://youtu.be/" in content):
                    info = await bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet": True}).extract_info(f"ytsearch1:{content}", download=False, ie_key="YoutubeSearch"))
                    yturl = [entry["webpage_url"] for entry in info["entries"]]            
                else:
                    yturl = [content]
                    
                url = pafy.new(yturl[0]).getbestaudio().url
                await message.channel.send(f"Now playing: {yturl[0]}")
                musicbot.play(voice, url)
            except:
                return await message.channel.send("Not so fast!")
                
    if message.content.lower().startswith('willo leave'):
        voice = discord.utils.get(bot.voice_clients, guild=message.author.guild)
        musicbot.queue = []
        musicbot.names = []
        try:
            await message.channel.send("Disconnecting, give me a second to clean up my record player!")
            return await voice.disconnect()
        except:
            return await message.channel.send("I'm not even connected. Damn.")
    
    if message.content.lower().startswith('willo pause'):
        voice = discord.utils.get(bot.voice_clients, guild=message.author.guild)
        try:
            return await voice.pause()
        except:
            if voice == None:
                await message.channel.send("I wasn't even speaking. What is it with you people? ...")
    
    if message.content.lower().startswith('willo continue'):
        voice = discord.utils.get(bot.voice_clients, guild=message.author.guild)
        try:
            return await voice.resume()
        except:
            if voice == None:
                await message.channel.send("I'm not even there!")
    
    if message.content.lower().startswith('willo queue'):
        if len(musicbot.queue) == 0:
            await message.channel.send("There is no queue.")
        else:
            embed = discord.Embed(title="The Queue", description="", colour=discord.Colour.blurple())
            i = 1
            for name in musicbot.names:
                embed.description += f"{i} - {name[0]}\n"
                i += 1
            embed.set_footer(text="The queue can be cleared with 'Willo leave'")
            await message.channel.send(embed=embed)
    
    if message.content.lower().startswith('willo skip'):
        voiceChannel = discord.utils.get(message.author.guild.voice_channels, name=message.author.voice.channel.name)
        voice = discord.utils.get(bot.voice_clients, guild=message.author.guild)
        if voice == None:
            return await message.channel.send("I am not playing a song right now")
        if voiceChannel == None:
            return await message.channel.send("You are not in a channel")
        if voiceChannel.id != voice.channel.id:
            return await message.channel.send("You and me, we are not in the same channel.")
        else:
            voice.stop()
            await message.channel.send("Skipping!")
            await musicbot.next(voice)

    # message responses
    if message.content.lower().startswith(('hello', 'hi', 'hey', 'hallo', 'hoi')):
        greet = random.choice(GREETING)
        if message.author.id == 256865001757736960:
            naam = "Daniël"
        elif message.author.id == 254534396390932491:
            naam = "Matthias"
        elif message.author.id == 146629406398480384:
            naam = "Leonie"
        elif message.author.id == 146682730321543169:
            naam = "Koen"
        elif message.author.id == 328930345800171520:
            naam = "Sacha"
        elif message.author.id == 265805417765011456:
            naam = "Asllan"
        elif message.author.id == 295508105322561536:
            naam = "Bas"
        elif message.author.id == 147397202753486850:
            naam = "Jim"
        elif message.author.id == 687024689922703381:
            naam = "Femke"
        elif message.author.id == 273586584937562113:
            naam = "Jolan"
        elif message.author.id == 256858825171140609:
            naam = ", holy shit het is Joran"
        elif message.author.id == 237134274929754112:
            naam = "Pepijn"
        elif message.author.id == 540914374131580928:
            naam = "Tommie"
        elif message.author.id == 301046737764745216:
            naam = "Jarno"
        elif message.author.id == 357153700139237378:
            naam = "Sem"
        else:
            naam = None
        
        if naam == None:
            await message.channel.send(f'{greet}!')
        elif naam == "Daniël":
            await message.channel.send('Hallo mensen van de wifi smasher, welkom bij een nieuwe video en vandaag gaan we gdfherhwbhjdsf...fdsfsdf..')
        else:
            await message.channel.send(f"{greet} {naam}!")

    if message.content.lower().startswith('willo'):
        c = message.content.lower()
        if c == 'willo' or c == 'willo?' or c == 'willo ':
            await message.channel.send('Ja?')
        elif message.content.lower().startswith(('willo play', 'willo pause', 'willo continue', 'willo stop', 'willo leave', 'willo queue', 'willo skip')):
            pass
        elif 'matthias' in c:
            await message.channel.send("Matthias is my creator, I am forever thankfull! :D")
        elif 'nederlan' in c or 'engel' in c or 'dutch' in c or 'english' in c or 'taal' in c or 'language' in c:
            await message.channel.send('Ik ben tweetalig :D. Ik spreek Nederlands en Engels.')
        elif 'kan j' in c or 'doe j' in c or 'werk j' in c or 'do you' in c:
            if message.author.id == 254534396390932491:
                await message.channel.send('Ik kan:' + COMMANDS)
            else:
                await message.channel.send('Ik kan alles.')
        elif 'introduce' in c:
            pass
        else:
            await message.channel.send('Stoor mij niet met zulke onnozele kwesties.')
    
    if message.content.lower().startswith('help'):
        if message.author.id == 254534396390932491:
            await message.channel.send(COMMANDS)
        else:
            await message.channel.send('Het is te laat om jou te helpen.')

    if message.content.lower().startswith('cleared the chat!'):
        if message.author.id == 968827105016164372: #Willo
            message.delete()
    
    if message.content.lower().startswith('willo introduce'):
        if message.author.id == 254534396390932491:
                await message.channel.send("@everyone **My name is willo!**\nI am a discord bot created by <@254534396390932491>. I have been designed to be a member of the Ludit server more than a bot.\nHowever I do have some bot like functions such as playing music! :D Therefore I have also been deployed in other servers.\nI do not work with a preset, just speak to me with my name and I will respond! (Maybe not always)\nAs of right now I am only online when my maker has my script running. Not to worry tho, as a 24/7 uptime is in production.\nAnywway, I hope you will enjoy my presence. If you have any questions or suggestions, ask <@254534396390932491>!\nThis is my first launch, I will keep you posted if I ever get updated!\n*V1.0*")

        

    # Gif/Image responses
    if message.content.lower().startswith(('kys', 'https://tenor.com/view/kys-saul-goodman-better-call-saul-gif-24336468', 'https://tenor.com/view/bill-nye-consider-the-following-kill-yourself-gif-24441260')):
        await message.channel.send("Please don't.")

    if message.content.startswith(('https://tenor.com/view/hop-on-valorant-gif-25789851', 'https://tenor.com/view/valorant-play-valorant-valorant-enjoyers-chips-wanna-play-valorant-gif-22258400', 'https://tenor.com/view/valorant-valo-gigachad-gif-23118627', 'https://tenor.com/view/valorant-play-valorant-hop-on-valorant-hop-on-anime-kissing-gif-23656387', 'https://tenor.com/view/hasbulla-gif-22466319')) and message.author.id == 301046737764745216:
        await message.channel.send('Addiction moment')
    
    if message.content.startswith('https://tenor.com/view/so-no-head-animal-crossing-break-phone-tom-nook-no-head-gif-24545244'):
        await message.channel.send('https://tenor.com/view/anger-angry-break-gif-19098093')

    if message.content.startswith('https://tenor.com/view/shaco-league-of-legends-clone-gif-20083502'):
        await message.channel.send('Owhwhwwww')
    
    if message.content.startswith('https://tenor.com/view/love-you-heart-ily-asdfpoki-pokimane-gif-13823656'):
        await message.channel.send('I love you too!')

    if message.content.startswith('https://tenor.com/view/white-dog-shaking-scared-nervous-dog-scared-and-shaking-gif-22874221'):
        await message.channel.send('Shiver me timbers!')
    
    if message.content.startswith('https://tenor.com/view/crying-meme-black-guy-cries-sad-man-thank-god-for-my-reefer-hood-news-gif-24902056'):
        await message.channel.send("It's okay bro <3")
    
    if message.content.startswith('https://tenor.com/view/sigma-rule-744-gif-25127400'):
        await message.channel.send("@everyone Rule 744 has been called!")
    
    if message.content.startswith('https://tenor.com/view/60fps-morshu-gif-19945976'):
        await message.channel.send("True")
    
    if message.content.startswith('https://tenor.com/view/troll-pilled-gif-19289988'):
        await message.channel.send("https://tenor.com/view/troll-pilled-gif-19289988")
    
    if message.content.startswith('https://tenor.com/view/dono-wall-talking-wall-bricks-gif-17741481'):
        await message.channel.send("I'm here, you can talk to me!")
        await asyncio.sleep(12)
        await message.channel.send(":)")

    if message.content.startswith('https://tenor.com/view/skander-dinostan-eu4-gif-22448415'):
        await message.channel.send("https://tenor.com/view/skander-dinostan-eu4-gif-22448415")

    if message.content.startswith('https://cdn.discordapp.com/attachments/613729945830555648/1047623673206550598/unknown.png'):
        await message.channel.send("https://cdn.discordapp.com/attachments/326424296933163018/1042195337063960636/unknown.png")

    if message.content.startswith('https://cdn.discordapp.com/attachments/326424296933163018/1042195337063960636/unknown.png'):
        await message.channel.send("https://cdn.discordapp.com/attachments/613729945830555648/1047623673206550598/unknown.png")
    
    if message.content.startswith(('https://tenor.com/view/get-real-yoru-valorant-yoru-valorant-get-gif-25282277', 'https://tenor.com/view/justfin-jefferson-j-jettas-jettas-jetta-nfl-gif-25986060', 'https://tenor.com/view/get-real-cat-skate-funny-meme-gif-18666878', 'https://tenor.com/view/get-real-gif-25364817')):
        await message.channel.send("Getting real!") 
        await message.channel.send("https://tenor.com/view/load-loading-april-fools-gif-5435835")
    
    if message.content.startswith('https://tenor.com/view/american-psycho-patrick-bateman-gif-25746875'):
        await message.channel.send("smh :fist::pensive:")

    if message.content.startswith('https://tenor.com/view/joker-joker-card-evil-laughs-gif-15221160'):
            await message.channel.send("Is the J for Joker, or for Jim?")
            await asyncio.sleep(1)
            await message.channel.send("Hmmm...")
    
    if message.content.startswith('https://tenor.com/view/shut-up-cat-monch-cat-monch-spinfal-gif-19376414'):
        await message.channel.send("https://tenor.com/view/reverse-card-uno-uno-cards-gif-13032597")

bot.run(TOKEN)