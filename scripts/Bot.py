TOKEN = "" # Never push your token to GitHub!

# packages
import discord
from discord import app_commands
import asyncio

# local
import Music
import Responses

# set intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# make clients
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)
musicbot = Music.Player(bot)

# login
@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await tree.sync()
    print(f'We have logged in as {bot.user}, ready to terrorize the Luditserver.')

# application slash commands
@tree.command(name="test", description="Testing!")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("I'm working!")

@tree.command(name="help", description="Fine, I'll show you my commands!")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(Responses.COMMANDS)

@tree.command(name="clear", description="Clears a given amount of messages.")
@app_commands.checks.has_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, amount: int):
    await interaction.response.defer(ephemeral=True)
    await interaction.channel.purge(limit=amount)
    await interaction.followup.send("Cleared the chat!")

# command error
@tree.error
async def on_app_command_error(interaction, error):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message(error, ephemeral=True)
    else: raise error

@bot.event
async def on_message(message):
    # avoid responding to yourself
    if message.author == bot.user:
        return
    

    # music commands
    if message.content.lower().startswith('willo play'):
        await Music.play(message, bot, musicbot)
                
    if message.content.lower().startswith('willo leave'):
        await Music.leave(message, bot, musicbot)
    
    if message.content.lower().startswith('willo pause'):
        await Music.pause(message, bot)

    if message.content.lower().startswith('willo continue'):
        await Music.resume(message, bot)
    
    if message.content.lower().startswith('willo queue'):
        await Music.queue(message, musicbot)
    
    if message.content.lower().startswith('willo skip'):
        await Music.skip(message, bot, musicbot)


    # commands
    if message.content.lower().startswith(('commands', 'willo commands')):
        await Responses.commands(message)
    
    if message.content.lower().startswith(('help', 'willo help')):
        await Responses.help(message)
    
    if message.content.lower().startswith(('decide on', 'willo decide on')):
        await Responses.decide(message)
    
    if message.content.lower().startswith('willo introduce'):
        await Responses.introduce(message)
    
    if message.content.lower().startswith('willo update'):
        await Responses.update(message)
    
    if message.content.lower().startswith('willo cum'):
        await message.channel.send("https://tenor.com/view/cum-penis-cum-i-creamed-cumming-xd-gif-20404521")


    # message responses
    if message.content.lower().startswith(('hello ', 'hi ', 'hey ', 'hallo ', 'hoi ', 'jo ', 'yo ', 'willo hello ', 'willo hi ', 'willo hey ', 'willo hallo ', 'willo hoi ', 'willo jo ', 'willo yo ', 'sup ', 'willo sup ', 'wassup ')) or message.content.lower() == 'hello' or message.content.lower() == 'hi'or message.content.lower() == 'hey'or message.content.lower() == 'hallo' or message.content.lower() == 'hoi' or message.content.lower() == 'jo' or message.content.lower() == 'yo' or message.content.lower() == 'willo hello' or message.content.lower() == 'willo hi' or message.content.lower() == 'willo hey'or message.content.lower() == 'willo hallo'or message.content.lower() == 'willo hoi'or message.content.lower() == 'willo jo' or message.content.lower() == 'willo yo' or message.content.lower() == 'sup' or message.content.lower() == 'willo sup' or message.content.lower() == 'wassup':
        #await Responses.greet(message)
        pass
    
    if message.content.lower().startswith(('gn ', 'goodnight ', 'gngn ', 'night ')) or message.content.lower() == 'gn' or message.content.lower() == 'goodnight' or message.content.lower() == 'gngn' or message.content.lower() == 'night':
        #await Responses.goodnight(message)
        pass
    
    if message.content.lower().startswith(('gm ', 'goodmorning ', 'goedemorgen ', 'goeiemorgen ', 'goedemorge ')) or message.content.lower() == 'gm' or message.content.lower() == 'goodmorning' or message.content.lower() == 'goedemorgen' or message.content.lower() == 'goeiemorgen' or message.content.lower() == 'goeiemorge' or message.content.lower() == 'goedemorge':
        #await Responses.goodmorning(message)
        pass

    if message.content.lower().startswith('willo'):
        await Responses.willo(message)
    
    if message.content.lower().startswith('on god ') or message.content.lower() == 'on god':
        await message.channel.send("fr fr")
    
    
    # Gif/Image responses
    if message.content.lower().startswith(('kys', 'https://tenor.com/view/kys-saul-goodman-better-call-saul-gif-24336468', 'https://tenor.com/view/bill-nye-consider-the-following-kill-yourself-gif-24441260', 'kill yourself')):
        await message.channel.send("Please don't.")

    if message.content.startswith(('https://tenor.com/view/hop-on-valorant-gif-25789851', 'https://tenor.com/view/valorant-play-valorant-valorant-enjoyers-chips-wanna-play-valorant-gif-22258400', 'https://tenor.com/view/valorant-valo-gigachad-gif-23118627', 'https://tenor.com/view/valorant-play-valorant-hop-on-valorant-hop-on-anime-kissing-gif-23656387', 'https://tenor.com/view/hasbulla-gif-22466319', 'https://tenor.com/view/valorant-valorant-meme-play-valorant-hop-on-valorant-valorant-time-gif-26090808')) and message.author.id == 301046737764745216:
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
    
    if message.content.startswith(('https://tenor.com/view/get-real-yoru-valorant-yoru-valorant-get-gif-25282277', 'https://tenor.com/view/justfin-jefferson-j-jettas-jettas-jetta-nfl-gif-25986060', 'https://tenor.com/view/get-real-cat-skate-funny-meme-gif-18666878', 'https://tenor.com/view/get-real-gif-25364817', 'https://tenor.com/view/get-real-cats-cat-kittens-gif-22323194')):
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

    if message.content.startswith('https://tenor.com/view/aram-time-gif-22182013'):
        await message.channel.send("ARAM time!")
    
    if message.content.startswith('https://c.tenor.com/jQh7s68AGAgAAAAM/cock-cock-located.gif'):
        await message.channel.send(":detective: :mag: ")

    if message.content.startswith(('https://tenor.com/view/ok-ok-and-okay-buddy-dont-care-didnt-ask-gif-25239605', 'https://tenor.com/view/ok-and-ok-and-whole-sqaud-gif-22248092')):
        await message.channel.send("https://tenor.com/view/mrroasty-and-niklavs-niklavs-and-roasty-niklavs100and-mrroasty99-niklavs100-niklavs-gif-20207493")
    
    if message.content.startswith('https://tenor.com/view/british-dune-gif-24757881'):
        await message.channel.send("Oi oi!")
    
    if message.content.startswith('https://tenor.com/view/jetstream-sam-n-word-gif-25301615'):
        await message.channel.send("Brother no.")
    
    if message.content.startswith('https://tenor.com/view/griddy-griddy-dance-right-foot-creep-get-griddy-gif-25395586'):
        await message.channel.send("https://tenor.com/view/griddy-gif-25113845")

bot.run(TOKEN)