import random

#global variables
GREETING = ['Hallo', 'Hey', 'Goededag', 'Sup', 'Heyo', 'Yo']
GN = ['Goodnight', 'Sleep tight', 'Rest well', 'Night Night', 'Sleep well']
COMMANDS = 'Commands, Help, Decide on, Cum, Play, Skip, Pause, Continue, Queue, Leave'

async def decide(message):
    if message.content.startswith('willo'):
        content = message.content[15:]
    else:
        content = message.content[9:]
    choices = []
    items = content.split(',')
    for item in items:
        if item != '' and item != ' ':
            choices += [item]
    await message.channel.send(random.choice(choices))

async def get_name(message):
    if message.author.id == 256865001757736960:
        return "Daniël"
    elif message.author.id == 254534396390932491:
        return "Matthias"
    elif message.author.id == 146629406398480384:
        return "Leonie"
    elif message.author.id == 146682730321543169:
        return "Koen"
    elif message.author.id == 328930345800171520:
        return "Sacha"
    elif message.author.id == 265805417765011456:
        return "Asllan"
    elif message.author.id == 295508105322561536:
        return "Bas"
    elif message.author.id == 147397202753486850:
        return "Jim"
    elif message.author.id == 687024689922703381:
        return "Femke"
    elif message.author.id == 273586584937562113:
        return "Jolan"
    elif message.author.id == 256858825171140609:
        return ", holy shit het is Joran"
    elif message.author.id == 237134274929754112:
        return "Pepijn"
    elif message.author.id == 540914374131580928:
        return "Tommie"
    elif message.author.id == 301046737764745216:
        return "Jarno"
    elif message.author.id == 357153700139237378:
        return "Sem"
    elif message.author.id == 293300046093484043:
        return "Mees"
    elif message.author.id == 357153700139237378:
        return "Jamie"
    else:
        return None

async def greet(message):
    greet = random.choice(GREETING)
    naam = await get_name(message)
    
    if naam == None:
        await message.channel.send(f'{greet}!')
    elif naam == "Daniël":
        await message.channel.send('Hallo mensen van de wifi smasher, welkom bij een nieuwe video en vandaag gaan we gdfherhwbhjdsf...fdsfsdf..')
    else:
        await message.channel.send(f"{greet} {naam}!")
    
async def goodnight(message):
    gn = random.choice(GN)
    naam = await get_name(message)

    if naam == None:
        await message.channel.send(f'{gn}!')
    else:
        await message.channel.send(f"{gn} {naam}!")

async def willo(message):
    content = message.content.lower()
    if message.content.lower().startswith(('willo play', 'willo pause', 'willo continue', 'willo stop', 'willo leave', 'willo queue', 'willo skip', 'willo introduce', 'willo update', 'willo commands', 'willo help', 'willo decide on', 'willo cum')):
        pass
    elif content == 'willo' or content == 'willo?' or content == 'willo ':
        await message.channel.send('Yes?')
    elif 'matthias' in content:
        await message.channel.send("Matthias is my creator, I am forever thankfull! :D")
    elif 'nederlan' in content or 'engel' in content or 'dutch' in content or 'english' in content or 'taal' in content or 'language' in content:
        await message.channel.send("I speak English, however I do understand Dutch!")
    elif 'kan j' in content or 'doe j' in content or 'werk j' in content or 'do you' in content:
        if message.author.id == 254534396390932491:
            await message.channel.send("I'm capable of: " + COMMANDS)
        else:
            await message.channel.send('I can do anything.')
    else:
        await message.channel.send("Do not distrub me with such silly matters.")

async def introduce(message):
    if message.author.id == 254534396390932491:
        await message.channel.send(
        "@everyone **My name is willo!**\n"
        "I am a discord bot created by <@254534396390932491>. I have been designed to be a member of the Ludit server more than a bot.\n"
        "However I do have some bot like functions such as playing music! :D Therefore I have also been deployed in other servers.\n"
        "I do not work with a preset, just speak to me with my name and I will respond! (Maybe not always)\n"
        "As of right now I am only online when my maker has my script running. Not to worry tho, as a 24/7 uptime is in production.\n"
        "Anyway, I hope you will enjoy my presence. If you have any questions or suggestions, ask <@254534396390932491>!\n"
        "This is my first launch, I will keep you posted if I ever get updated!\n"
        "*V2.1*")
        await message.delete()

async def update(message):
    if message.author.id == 254534396390932491:
        await message.channel.send(
            "@everyone **Patch notes v2.0**\n"
            "Yes! My second update! I am now in version 2.0!\n"
            "I now run 24/7 on a RasberryPI, a mini-server in <@254534396390932491>'s house!\n\n"
            "*V2.0*")
        await message.delete()

async def commands(message):
    if message.author.id == 254534396390932491:
        await message.channel.send(COMMANDS)
    else:
        await message.channel.send("You aren't my boss. I am a strong and independant bot. Slay.")
    
async def help(message):
    if message.author.id == 254534396390932491:
        await message.channel.send(COMMANDS)
    else:
        await message.channel.send("It's too late to help you.")