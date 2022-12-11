import random

#global variables
GREETING = ['Hallo', 'Hey', 'Goededag', 'Sup', 'Heyo']
COMMANDS = 'Commands, Decide on, Willo play, Willo skip, Willo pause, Willo continue, Willo queue, Willo leave'

async def decide(message):
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

async def greet(message):
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
    
async def willo(message):
    content = message.content.lower()
    if content == 'willo' or content == 'willo?' or content == 'willo ':
        await message.channel.send('Ja?')
    elif message.content.lower().startswith(('willo play', 'willo pause', 'willo continue', 'willo stop', 'willo leave', 'willo queue', 'willo skip')):
        pass
    elif 'matthias' in content:
        await message.channel.send("Matthias is my creator, I am forever thankfull! :D")
    elif 'nederlan' in content or 'engel' in content or 'dutch' in content or 'english' in content or 'taal' in content or 'language' in content:
        await message.channel.send('Ik ben tweetalig :D. Ik spreek Nederlands en Engels.')
    elif 'kan j' in content or 'doe j' in content or 'werk j' in content or 'do you' in content:
        if message.author.id == 254534396390932491:
            await message.channel.send('Ik kan: Commands, Decide on, Summon, Willo play, Willo skip, Willo pause, Willo continue, Willo queue, Willo leave')
        else:
            await message.channel.send('Ik kan alles.')
    elif 'introduce' in content:
        pass
    else:
        await message.channel.send('Stoor mij niet met zulke onnozele kwesties.')

async def introduce(message):
    if message.author.id == 254534396390932491:
            await message.channel.send(
                "@everyone **My name is willo!**\n"
                "I am a discord bot created by <@254534396390932491>. I have been designed to be a member of the Ludit server more than a bot.\n"
                "However I do have some bot like functions such as playing music! :D Therefore I have also been deployed in other servers.\n"
                "I do not work with a preset, just speak to me with my name and I will respond! (Maybe not always)\n"
                "As of right now I am only online when my maker has my script running. Not to worry tho, as a 24/7 uptime is in production.\n"
                "Anywway, I hope you will enjoy my presence. If you have any questions or suggestions, ask <@254534396390932491>!\n"
                "This is my first launch, I will keep you posted if I ever get updated!\n"
                "*V1.4*")

async def commands(message):
    if message.author.id == 254534396390932491:
        await message.channel.send(COMMANDS)
    else:
        await message.channel.send('Jij bent mijn baas niet. I am a strong and independant bot. Slay.')
    
async def help(message):
    if message.author.id == 254534396390932491:
        await message.channel.send(COMMANDS)
    else:
        await message.channel.send('Het is te laat om jou te helpen.')