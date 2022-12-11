import discord
import youtube_dl
import pafy

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


async def play(message, bot, musicbot):
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

async def leave(message, bot, musicbot):
    voice = discord.utils.get(bot.voice_clients, guild=message.author.guild)
    musicbot.queue = []
    musicbot.names = []
    try:
        await message.channel.send("Disconnecting, give me a second to clean up my record player!")
        return await voice.disconnect()
    except:
        return await message.channel.send("I'm not even connected. Damn.")
    
async def pause(message, bot):
        voice = discord.utils.get(bot.voice_clients, guild=message.author.guild)
        try:
            return await voice.pause()
        except:
            if voice == None:
                await message.channel.send("I wasn't even speaking. What is it with you people? ...")
    
async def resume(message, bot):
        voice = discord.utils.get(bot.voice_clients, guild=message.author.guild)
        try:
            return await voice.resume()
        except:
            if voice == None:
                await message.channel.send("I'm not even there!")
    
async def queue(message, musicbot):
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
    
async def skip(message, bot, musicbot):
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