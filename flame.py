import json
import random
import asyncio
import discord
import requests
from discord.ext import commands

Client = discord.Client()
bot_prefix = "p!"
client = commands.Bot(command_prefix=bot_prefix)
server = client.get_guild(398527995167637524)

'''
EVENTS
'''


# TELLS YOU WHEN THE BOT IS READY
@client.event
async def on_ready():
    print("====================")
    print("Connected!")
    print("====================")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("====================")
    print('Logged in as ' + client.user.name + ' (ID:' + str(client.user.id) + ') | ' + str(
        len(client.guilds)) + ' servers')
    await client.change_presence(game=discord.Game(name='Use p!help'))


# CLEVER BOT
CBuser = 'hTitan8XcqVKE5qt'
CBkey = 'jrUn80fYMmc1P6MTqqDwjCCoRo7yt5P5'


@client.event
async def on_message(message):
    if not message.author.bot and (message.guild == None or client.user in message.mentions):
        # await client.send_typing(message.channel)
        txt = message.content.replace(message.guild.me.mention, '') if message.guild else message.content
        r = json.loads(requests.post('https://cleverbot.io/1.0/ask',
                                     json={'user': CBuser, 'key': CBkey, 'nick': 'Paradise', 'text': txt}).text)
        if r['status'] == 'success':
            await message.channel.send(r['response'])
    else:
        await client.process_commands(message)


@client.event
async def on_guild_join(guild):
    embed = discord.Embed(title=":star: Hello! **thanks for addine me** :) :star: ",
                          description="Here is the Paradise info.\n - My prefix here is p!\n - You can see a list of commands by typing `p!help`\n - Join Paradise Server https://discord.gg/Hfac9uu")
    if guild.system_channel is not None:
        await guild.system_channel.send(embed=embed)
    else:
        for c in guild.text_channels:
            if not c.permissions_for(guild.me).says:
                continue
            f_channel = c
            break
        if f_channel is not None:
            await f_channel.send(embed=embed)


'''
COMMANDS
'''
# HELP COMMAND
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    footer_text = "Paradise ☁"
    embed1 = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="To join paradise server use this command `p!server` for bot invite `p!invite`")
    embed1.set_author(name=str(author.name), icon_url=author.avatar_url)
    embed1.title = "COMMANDS FOR EVERYONE"
    embed1.add_field(name="p!help", value="Shows you this!", inline=True)
    embed1.add_field(name="p!info", value="shows you the bot informations!", inline=True)
    embed1.add_field(name="p!invite", value="invites the bot", inline=True)
    embed1.add_field(name="p!server", value="invites to the paradise server!", inline=True)
    embed1.add_field(name="p!ping", value="Pings the bot!", inline=True)
    embed1.add_field(name="p!serverinfo", value="Gives you information about the server!", inline=True)
    embed1.add_field(name="p!quote", value="Gives you a random quote!", inline=True)
    embed1.add_field(name="p!eightball (question)", value="Ask the magic eightball a question!", inline=True)
    embed1.add_field(name="p!suicide", value="Gives you suicide fact!", inline=True)
    embed1.add_field(name="p!heaven", value="Gives you Heaven fact!", inline=True)
    embed1.add_field(name="p!say (text)", value="Forces the bot to say something!", inline=True)
    embed1.add_field(name="p!profile (user)", value="Shows you information about the mentioned user!", inline=True)
    embed1.set_footer(text=footer_text)

    author = ctx.message.author
    footer_text = "Paradise ☁"
    embed2 = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    embed2.set_author(name=str(author.name), icon_url=author.avatar_url)
    embed2.title = "FUN COMMANDS"
    embed2.add_field(name="p!retard", value="Turns the mentioned user into a retard!", inline=True)
    embed2.add_field(name="p!kill (user)", value="Kills someone!", inline=True)
    embed2.add_field(name="p!hug (user)", value="hugs someone!", inline=True)
    embed2.add_field(name="p!kiss (user)", value="kiss someone!", inline=True)
    embed2.add_field(name="p!esketit (user)", value="esketit someone!", inline=True)
    embed2.add_field(name="p!cookie (user)", value="give someone cookie!", inline=True)
    embed2.add_field(name="p!poison (user)", value="give someone poison!", inline=True)
    embed2.add_field(name="p!poop (user)", value="give a shit to someone!", inline=True)
    embed2.add_field(name="p!candy (user)", value="give someone candy!", inline=True)
    embed2.add_field(name="p!slap (user)", value="slaps someone!", inline=True)
    embed2.add_field(name="p!insult (user)", value="insult someone!", inline=True)
    embed2.add_field(name="p!roast (user)", value="Roasts someone!", inline=True)
    embed2.set_footer(text=footer_text)

    author = ctx.message.author
    footer_text = "Paradise ☁"
    embed3 = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    embed3.set_author(name=str(author.name), icon_url=author.avatar_url)
    embed3.title = "MODERATION COMMANDS"
    embed3.add_field(name="p!ban (user)", value="Bans the mentioned user!", inline=True)
    embed3.add_field(name="p!kick (user)", value="Kicks the mentioned user!", inline=True)
    embed3.add_field(name="p!prune (number)", value="Deletes a number of messages!", inline=True)
    embed3.add_field(name="p!unban (id)", value="Unbans the user with the matching ID!", inline=True)
    embed3.add_field(name="p!giverole (user) (role)", value="Gives the mentioned user a specified role!", inline=True)
    embed3.add_field(name="p!takerole (user) (role)", value="Removes a specified role from the mentioned user!", inline=True)
    embed3.add_field(name="p!rawsay (text)", value="Forces the bot the say something without any formatting!", inline=True)
    embed3.set_footer(text=footer_text)

    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = ""
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name=":incoming_envelope: ", value="A list of commands is coming your way!\nCheck your DMs, {}!".format(author))
    msg.set_footer(text=footer_text)
    await ctx.send(embed=msg)
    await ctx.message.author.send(author, embed=embed1)
    await ctx.message.author.send(author, embed=embed2)
    await ctx.message.author.send(author, embed=embed3)
    print("============================================================")
    print("HELP COMMAND")
    print("{}".format(author))
    print("============================================================")


# PING COMMAND
@client.command(pass_context=True)
async def ping(ctx):
    pingmsg = ["I'm here!", "Yes, I am here. You don't have to ping me!", "Hello?", "Oh, hi!", "Hey, how are you?",
               "Hello!", "Pong!"]
    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = ""
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name=":satellite: Pinging...", value="{}".format(random.choice(pingmsg)))
    msg.set_footer(text=footer_text)
    await ctx.send(embed=msg)
    print("============================================================")
    print("PING COMMAND")
    print("{}".format(author))
    print("============================================================")


# SERVER INFO COMMAND
@client.command(pass_context=True)
async def serverinfo(ctx):
    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = ":page_with_curl: SERVER INFORMATION"
    msg.add_field(name="MEMBERS", value=str(len(ctx.message.guild.members)), inline=True)
    msg.add_field(name="CHANNELS", value=str(len(ctx.message.guild.channels)), inline=True)
    msg.add_field(name="EMOJIS", value=str(len(ctx.message.guild.emojis)), inline=True)
    msg.add_field(name="ID", value=str(ctx.message.guild.id), inline=True)
    msg.add_field(name="REGION", value=str(ctx.message.guild.region), inline=True)
    msg.add_field(name="ROLES", value=str(len(ctx.message.guild.roles)), inline=True)
    msg.add_field(name="OWNER", value=str(ctx.message.guild.owner), inline=True)
    msg.add_field(name="CREATED AT", value=str(ctx.message.guild.created_at), inline=True)
    msg.set_footer(text=footer_text)
    await ctx.send(embed=msg)
    print("============================================================")
    print("SERVERINFO COMMAND")
    print("{}".format(author))
    print("============================================================")

# p!report (user) (reason) - REPORT SUM1
@client.command(pass_context=True)
async def report(ctx, *, args):
    author = ctx.message.author
    await ctx.send(":ticket:  Report sent!")

    msg2 = discord.Embed(colour=0xFF0000, description="", title="Report:")
    msg2.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg2.add_field(name= ":clipboard: Report", value= "`{} has issued a report!`\n`Reason: {}`".format(ctx.message.author, args))
    msg2.set_footer(text="Paradise ☁")

    await client.get_channel(405502159292203009).send(embed=msg2)

    print("============================================================")
    print("REPORT COMMAND")
    print("{}".format(author))
    print("============================================================") 

# p!retard (user) - TURNS PPL INTO RETARDS
@client.command(pass_context=True)
async def retard(context, userName: discord.User):
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = ""
    msg.add_field(name=":rofl: Retard Maker 3000",
                  value="`{} is now officially a retard!`\n`Research shows that most retards are good people!`".format(
                      userName.display_name))
    msg.set_footer(text=footer_text)
    await context.send(embed=msg)
    print("============================================================")
    print("RETARD COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")

# kiss GIF COMMAND
@client.command(pass_context=True)
async def kiss(context, userName: discord.User):
    kiss = ["https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif?itemid=6155657",
            "https://media.giphy.com/media/FmB6UTdCj3G12/giphy.gif",
            "https://media.giphy.com/media/12VXIxKaIEarL2/giphy.gif",
            "https://data.whicdn.com/images/64318304/original.gif",
            "https://media.giphy.com/media/bm2O3nXTcKJeU/giphy.gif",
            "https://media1.giphy.com/media/bGm9FuBCGg4SY/giphy.gif",
            "https://thumbs.gfycat.com/AgedWhisperedBarnacle-max-1mb.gif",
            "http://i.myniceprofile.com/1401/140141.gif",
            "https://38.media.tumblr.com/28be9398582acc543016b4233ff12d77/tumblr_inline_nmblyt3AJf1sjmrlk.gif",
            "https://s-media-cache-ak0.pinimg.com/originals/ef/cc/cb/efcccb410c47e35559e71c8435505dbc.gif",
            "https://media1.tenor.com/images/7fd98defeb5fd901afe6ace0dffce96e/tenor.gif?itemid=9670722",
            "https://78.media.tumblr.com/3a416d5c991dbef68b6eaf8a06682d3d/tumblr_inline_ol29wgtBjL1u0103a_500.gif",
            "https://orig00.deviantart.net/690c/f/2015/251/8/3/kiss_gif_animation_by_psyclopathe-d96tmbk.gif",
            "https://lh5.googleusercontent.com/-hL5QiBPsjqM/VMZt6cMVZgI/AAAAAAAACQ0/hUmVPyWcJcA/w498-h281/3.gif",
            "https://78.media.tumblr.com/befc3f8aa8e0de74004d314397799fac/tumblr_og2ac38IqO1u7esouo1_500.gif",]
 
    footer_text = "Paradise ☁"
    msg = discord.Embed(title="KISS! :kissing_closed_eyes:  ", colour=random.randint(0, 0xFFFFFF),
    description="{} :couplekiss:  Fancy Kiss :couplekiss:   {}".format(
    context.message.author, context.message.mentions[0]))
    print(random.choice(kiss))
    msg.set_image(url=str(random.choice(kiss)))
    msg.set_footer(text=" Romantic kiss! ")
    await context.send(embed=msg)
    print("============================================================")
    print("KISS COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")

@kiss.error
async def kiss_error(ctx, error):
    msg = discord.Embed(title=" :x: Error You forgot something ;) ", colour=random.randint(0, 0xFFFFFF), description="try again with p!kiss and mention the user ;) ")
    msg.set_footer(text=" example!! p!kiss @Flame.Exe#0001 ")
    await ctx.send(embed=msg)
    

# slap GIF COMMAND
@client.command(pass_context=True)
async def slap(context, userName: discord.User):
    slap = ["https://thumbs.gfycat.com/DeadRequiredElver-max-1mb.gif",
            "https://thumbs.gfycat.com/WhisperedPoisedEelelephant-max-1mb.gif",
            "https://thumbs.gfycat.com/FondTepidIberiannase-max-1mb.gif",
            "https://thumbs.gfycat.com/EmbarrassedAliveCutworm-max-1mb.gif",
            "https://thumbs.gfycat.com/FreeAgreeableBushbaby-max-1mb.gif",
            "https://thumbs.gfycat.com/SphericalSlushyGavial-max-1mb.gif",
            "https://thumbs.gfycat.com/AllSharpChick-max-1mb.gif",
            "https://thumbs.gfycat.com/EnlightenedBountifulAnchovy-max-1mb.gif",
            "https://thumbs.gfycat.com/OpulentArtisticIbizanhound-max-1mb.gif",
            "https://thumbs.gfycat.com/CaringFloweryKentrosaurus-max-1mb.gif",
            "https://thumbs.gfycat.com/CalmAccurateHartebeest-max-1mb.gif",
            "https://thumbs.gfycat.com/FrankHorribleCaecilian-max-1mb.gif",
            "https://thumbs.gfycat.com/ZanyAcademicBear-max-1mb.gif",
            "https://thumbs.gfycat.com/JealousSophisticatedDuckbillcat-max-1mb.gif",
            "https://thumbs.gfycat.com/WealthyFortunateAllosaurus-max-1mb.gif",]
 
    footer_text = "Paradise ☁"
    msg = discord.Embed(title="SLAP! :raised_hand: ", colour=random.randint(0, 0xFFFFFF),
    description="{} :boxing_glove: SLAPPED :boxing_glove:   {}".format(
    context.message.author, context.message.mentions[0]))
    print(random.choice(slap))
    msg.set_image(url=str(random.choice(slap)))
    msg.set_footer(text=" OUCH! ")
    await context.send(embed=msg)
    print("============================================================")
    print("SLAP COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")

@slap.error
async def slap_error(ctx, error):
    msg = discord.Embed(title=" :x: Error You forgot something ;) ", colour=random.randint(0, 0xFFFFFF), description="try again with p!slap and mention the user ;) ")
    msg.set_footer(text=" example!! p!slap @Flame.Exe#0001 ")
    await ctx.send(embed=msg)
    


#INFO COMMAND
@client.command(pass_context=True)
async def info(ctx):
    author = ctx.message.author
    footer_text = "Paradise ☁"
    server_count = client.guilds
    member_count = 0
    channel_count = 0
    for server in server_count:
        member_count = member_count + int(server.member_count)
        channel_count = channel_count + len(server.channels)
    msg = discord.Embed(title="Paradise Information :newspaper: ", description="Bot Made By Flame.Exe#0001",colour=random.randint(0, 0xFFFFFF))
    msg.add_field(name="API:", value="DIscord.py ({})".format(discord.__version__), inline=True)
    msg.add_field(name="Onwer ID:", value="398409207793319936", inline=True)
    msg.add_field(name="Server count", value=str(len(server_count)), inline=True)
    msg.add_field(name="User count", value=str(member_count), inline=True)
    msg.add_field(name="Invite link bot", value="[Click here](https://discordapp.com/oauth2/authorize?client_id=401419300096704525&scope=bot&permissions=2146958591)", inline=True)
    msg.add_field(name="Join Paradise server", value="[Click here](https://discord.gg/Q2yUkP3)")
    msg.add_field(name="Donate paradise with special rewards", value="[Click here](https://patreon.com/paradisebot)")
    await ctx.send(embed=msg)
    print("============================================================")
    print("INFO COMMAND")
    print("{}".format(author))
    print("============================================================")    

# HUG GIF COMMAND
@client.command(pass_context=True)
async def hug(context, userName: discord.User):
    hug = ["https://media1.giphy.com/media/3M4NpbLCTxBqU/giphy.gif",
           "https://media1.giphy.com/media/EvYHHSntaIl5m/giphy.gif",
           "https://media2.giphy.com/media/lXiRKBj0SAA0EWvbG/giphy.gif",
           "https://media2.giphy.com/media/HjlKKc14d5tBK/giphy.gif",
           "https://media2.giphy.com/media/diAhf8bYer76E/giphy.gif",
           "https://media1.giphy.com/media/xT39CXg70nNS0MFNLy/giphy.gif",
           "https://media0.giphy.com/media/42YlR8u9gV5Cw/giphy.gif",
           "https://media0.giphy.com/media/3oEhmDMA4r9GxhwEqA/giphy.gif",
           "https://media1.giphy.com/media/8KKRIP5ZHUo2k/giphy.gif",
           "https://media0.giphy.com/media/llmZp6fCVb4ju/giphy.gif",
           "https://media1.giphy.com/media/l378uBCYt1vfaj2aA/giphy.gif",
           "https://media1.giphy.com/media/QbkL9WuorOlgI/giphy.gif",
           "https://media2.giphy.com/media/MsKuuQKrMvoPu/giphy.gif",
           "https://media0.giphy.com/media/jMGxhWR7rtTNu/giphy.gif",
           "https://media3.giphy.com/media/f6y4qvdxwEDx6/giphy.gif",
           "https://media3.giphy.com/media/l4FGpP4lxGGgK5CBW/giphy.gif",
           "https://media1.giphy.com/media/26FeTvBUZErLbTonS/giphy.gif",
           "https://media0.giphy.com/media/3oEjI72YdcYarva98I/giphy.gif",
           "https://media3.giphy.com/media/7eQ8Ky3dAsRYA/giphy.gif",
           "https://media0.giphy.com/media/fyx8vjZc2ZvoY/giphy.gif",
           "https://media3.giphy.com/media/8tpiC1JAYVMFq/giphy.gif",
           "https://media2.giphy.com/media/3o6Zth3OnNv6qDGQ9y/giphy.gif"
           "https://media2.giphy.com/media/gnXG2hODaCOru/giphy.gif",
           "https://media3.giphy.com/media/3oEdv4hwWTzBhWvaU0/giphy.gif",
           "https://media2.giphy.com/media/bAmQn1R4V3owE/giphy.gif",
           "https://media0.giphy.com/media/3oz8xt8ebVWCWujyZG/giphy.gif",
           "https://media1.giphy.com/media/Bj9k1U69GZ8Iw/giphy.gif",
           "https://media0.giphy.com/media/Qwi6fEcn2JJeg/giphy.gif",
           "https://media2.giphy.com/media/JzsG0EmHY9eKc/giphy.gif",
           "https://media3.giphy.com/media/3oEhnaf39dUjrk2Ag0/giphy.gif",
           "https://media1.giphy.com/media/X4pI9XchDNsu4/giphy.gif",
           "https://media3.giphy.com/media/l0HlOvJ7yaacpuSas/giphy.gif",
           "https://media3.giphy.com/media/l4FGy5UyZ1KnVZ7BC/giphy.gif",
           "https://media0.giphy.com/media/yidUzriaAGJbsxt58k/giphy.gif",
           "https://media2.giphy.com/media/RPyUPymjO4YJa/giphy.gif",
           "https://media0.giphy.com/media/26gs6VrnuqjOwXb0I/giphy.gif",
           "https://media1.giphy.com/media/INUsrrxQW4et2/giphy.gif",
           "https://media1.giphy.com/media/oaQgdY6DCGKre/giphy.gif",
           "https://media2.giphy.com/media/2GnS81AihShS8/giphy.gif",
           "https://media2.giphy.com/media/rvzbOcYmR7GZW/giphy.gif",
           "https://media1.giphy.com/media/bbxTrFmeoM7aU/giphy.gif",
           "https://media1.giphy.com/media/3o75271l90QWINQSbe/giphy.gif",
           "https://media0.giphy.com/media/6uEE79cXjssla/giphy.gif",
           "https://media0.giphy.com/media/l41YzyKroVv69cTmw/giphy.gif",
           "https://media0.giphy.com/media/us8FXd0EtOXXa/giphy.gif",
           "https://media2.giphy.com/media/IuCSOHcDlooPm/giphy.gif",
           "https://media0.giphy.com/media/OiKAQbQEQItxK/giphy.gif",
           "https://media3.giphy.com/media/3oEjI5FOhdKTwzZqPS/giphy.gif",
           "https://media1.giphy.com/media/146hjDyVeRhhXG/giphy.gif",
           "https://media0.giphy.com/media/13YrHUvPzUUmkM/giphy.gif",
           "https://media1.giphy.com/media/DjoWze0Patl1m/giphy.gif",
           "https://media1.giphy.com/media/l4FGnPMWYC3JWhFWo/giphy.gif",
           "https://media1.giphy.com/media/1GJRIgTY4sS6k/giphy.gif",
           "https://media2.giphy.com/media/3ov9jJaDBM5jmETiXC/giphy.gif",
           "https://media2.giphy.com/media/kooPUWvhaGe7C/giphy.gif",
           "https://media2.giphy.com/media/l0MYLJKRmFCZbJyo0/giphy.gif",
           "https://media1.giphy.com/media/C6gNbjL0bb2Te/giphy.gif",
           "https://media1.giphy.com/media/heS7mNS0PisVy/giphy.gif",
           "https://media1.giphy.com/media/SKjrGSWO9WTxC/giphy.gif",
           "https://media3.giphy.com/media/l2JhzZkCGF9tBWatO/giphy.gif",
           "https://media2.giphy.com/media/l2JeafQqkjbkaqeC4/giphy.gif",
           "https://media1.giphy.com/media/xT0xemCvkpWyJlOG2Y/giphy.gif",
           "https://media1.giphy.com/media/xUOxfb8r3BhgPpfyKs/giphy.gif",
           "https://media2.giphy.com/media/3oz8xLz5gnSla2STE4/giphy.gif",
           "https://media0.giphy.com/media/3orif2vpZbXi8P0fPW/giphy.gif",
           "https://media2.giphy.com/media/Xz5yiymhR5qta/giphy.gif",
           "https://media0.giphy.com/media/vL1meInBzYCgo/giphy.gif",
           "https://media2.giphy.com/media/3otPozEs14AOGrdcOI/giphy.gif",
           "https://media0.giphy.com/media/xT1XGNlkcBDSqkCRqg/giphy.gif",
           "https://media3.giphy.com/media/l2JJOsEYzQbtvV0A0/giphy.gif",
           "https://media2.giphy.com/media/l3vRgg34T0F3lYRws/giphy.gif",
           "https://media1.giphy.com/media/l0HlKDJgw54pm4hgY/giphy.gif",
           "https://media1.giphy.com/media/qLEDGdMoyTT9e/giphy.gif",
           "https://media3.giphy.com/media/h9dm2hKcLCXsc/giphy.gif",
           "https://media0.giphy.com/media/oVr48mIz8l5XG/giphy.gif",
           "https://media3.giphy.com/media/ArYs7UTBnXvnW/giphy.gif",
           "https://media2.giphy.com/media/13fQ3RrUjteykw/giphy.gif",
           "https://media3.giphy.com/media/3o6Zt6tWmgtTBXaoM0/giphy.gif",
           "https://media1.giphy.com/media/NouqV2z3RkdUI/giphy.gif",
           "https://media0.giphy.com/media/l46Cot6SYZsicMsp2/giphy.gif",
           "https://media3.giphy.com/media/xT0Gqne4C3IxaBcOdy/giphy.gif",
           "https://media2.giphy.com/media/l2SpNKVG9ZPZA7dpm/giphy.gif",
           "https://media2.giphy.com/media/3o6Mb7KaEIURtCKAbS/giphy.gif",
           "https://media1.giphy.com/media/3o6ozthpyPfmo0B5S0/giphy.gif",
           "https://media3.giphy.com/media/3o6ZsU3d4WZ4wX5oQ0/giphy.gif",
           "https://media3.giphy.com/media/3oEjHG6BNeKNohrZiU/giphy.gif",
           "https://media3.giphy.com/media/VGACXbkf0AeGs/giphy.gif",
           "https://media2.giphy.com/media/3oKIP9Mkgy0ninvQ0U/giphy.gif",
           "https://media3.giphy.com/media/xUA7aVwuBDwtKhspos/giphy.gif",
           "https://media2.giphy.com/media/l3vRbbOSjx4JvY48g/giphy.gif",
           "https://media1.giphy.com/media/3EJsCqoEiq6n6/giphy.gif",
           "https://media2.giphy.com/media/117o9BJASzmLNC/giphy.gif",
           "https://media2.giphy.com/media/LuSeshH6YcgZq/giphy.gif",
           "https://media1.giphy.com/media/3o7WTDVMidWRDzP9ss/giphy.gif",
           "https://media0.giphy.com/media/PBYXorv5BZze8/giphy.gif",
           "https://media0.giphy.com/media/26tn9sw1iph9DzBuM/giphy.gif",
           "https://media0.giphy.com/media/wsSssszJkPBYs/giphy.gif"]
    footer_text = "Paradise ☁"
    msg = discord.Embed(title="Hugs :two_hearts: ", colour=random.randint(0, 0xFFFFFF),
    description="{} :cherry_blossom: Romantic Hugs :cherry_blossom:  {}".format(
    context.message.author, context.message.mentions[0]))
    print(random.choice(hug))
    msg.set_image(url=str(random.choice(hug)))
    msg.set_footer(text=" Hugs for ever ")
    await context.send(embed=msg)
    print("============================================================")
    print("HUG COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")


# ESKETIT GIF COMMAND
@client.command(pass_context=True)
async def esketit(context, userName: discord.User):
    esketit = ["https://media1.tenor.com/images/a1e52f4f5406ec6a68972558c48ecfa1/tenor.gif?itemid=9637556"
               "https://media3.giphy.com/media/l41JTEIQ4B222YZxe/giphy.gif"
               "https://pa1.narvii.com/6560/2db7772999a93333f20550b1e8ed77e4f65244e7_hq.gif"
               "https://tenor.com/view/bigsean-lil-bitch-lilbitch-gif-5055316"
               "https://tenor.com/view/lil-pump-gif-9116965"
               "https://tenor.com/view/lil-pump-gif-9637525"]
    footer_text = "Paradise ☁"
    msg = discord.Embed(title="ESKTEETIT :fire: ", colour=random.randint(0, 0xFFFFFF),
    description="{} :fire: Skirt :fire:  {}".format(
    context.message.author, context.message.mentions[0]))
    print(random.choice(esketit))
    msg.set_image(url=str(random.choice(esketit)))
    msg.set_footer(text=" esketit for ever ")
    await context.send(embed=msg)
    print("============================================================")
    print("esketit COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")

@hug.error
async def hug_error(ctx, error):
    msg = discord.Embed(title=" :x: Error You forgot something ;) ", colour=random.randint(0, 0xFFFFFF), description="try again with p!hug and mention the user ;) ")
    msg.set_footer(text=" example!! p!hug @Flame.Exe#0001 ")
    await ctx.send(embed=msg)


@client.command(pass_context=True)
async def poison(ctx, to_user: discord.Member):
    await ctx.send(" :skull_crossbones:  | {} has given {} a Poison :syringe: .".format(
                   ctx.author.name, to_user.mention))

@esketit.error
async def esketit_error(ctx, error):
    msg = discord.Embed(title=" :x: Error You forgot something ;) ", colour=random.randint(0, 0xFFFFFF), description="try again with p!esketit and mention the user ;) ")
    msg.set_footer(text=" example!! p!esketit @Flame.Exe#0001 ")
    await ctx.send(embed=msg)

@poison.error
async def poison_error(ctx, error):
    msg = discord.Embed(title=" :x: Error You forgot something ;) ", colour=random.randint(0, 0xFFFFFF), description="try again with p!poison and mention the user ;) ")
    msg.set_footer(text=" example!! p!poison @Flame.Exe#0001 ")
    await ctx.send(embed=msg)


@client.command(pass_context=True)
async def cookie(ctx, to_user: discord.Member):
    await ctx.send(" :cookie: | {} has given {} a Cookie.".format(
                   ctx.author.name, to_user.mention))

@cookie.error
async def cookie_error(ctx, error):
    msg = discord.Embed(title=" :x: Error You forgot something ;) ", colour=random.randint(0, 0xFFFFFF), description="try again with p!cookie and mention the user ;) ")
    msg.set_footer(text=" example!! p!cookie @Flame.Exe#0001 ")
    await ctx.send(embed=msg)


@client.command(pass_context=True)
async def candy(ctx, to_user: discord.Member):
    await ctx.send(" :candy: | {} has given {} a Candy.".format(
                   ctx.author.name, to_user.mention))

@candy.error
async def candy_error(ctx, error):
    msg = discord.Embed(title=" :x: Error You forgot something ;) ", colour=random.randint(0, 0xFFFFFF), description="try again with p!candy and mention the user ;) ")
    msg.set_footer(text=" example!! p!candy @Flame.Exe#0001 ")
    await ctx.send(embed=msg)

    

@client.command(pass_context=True)
async def poop(ctx, to_user: discord.Member):
    await ctx.send(" :poop: | {} has given {} a shit.".format(
                   ctx.author.name, to_user.mention))

@poop.error
async def poop_error(ctx, error):
    msg = discord.Embed(title=" :x: Error You forgot something ;) ", colour=random.randint(0, 0xFFFFFF), description="try again with p!poop and mention the user ;) ")
    msg.set_footer(text=" example!! p!poop @Flame.Exe#0001 ")
    await ctx.send(embed=msg)
    

# INSULT COMMAND
@client.command(pass_context=True)
async def insult(context, userName: discord.User):
    insult = ["My middle finger get's a boner when I think of you ;)",
                "I would call you a cunt, but you don't have the depth or the warmth.",
                "No, no, I'm not insulting you I'm describing you.",
                "You're a fail. So was your dad's condom.",
                "I'd like to see things from your point of view but I can't seem to get my head that far up my ass.",
                "Shut up, you'll never be the man your mother is.",
                "You're just mad 'cause your mom has a bigger dick than you.",
                "You should wear a condom on your head because if you're gonna act like a dick you might as well dress like one!",
                "You must have been born on a highway because that's where most accidents happen.",
                "I'd slap you, but that would be animal abuse.",
                "Have you been shopping lately? They are selling lives at the mall - you should get one.",
                "Pardon me, but you've obviously mistaken me for someone who gives a damn.",
                "Shock me, say something intelligent.",
                "Your birth certificate is an apology from the condom factory.",
                "I don't know what makes you so stupid, but it really works!",
                "YOU SUCK! AND YOU SWALLOW!"
                "You Failed! Yeah, so did your mom's abortion. :)",
                "At least when I do a handstand my stomach doesn't hit me in the face.",
                "Man, I bet you were up all night, working on that one.",
                "Twinkle twinkle little star,I want to hit you with my car,Throw you off a cliff so high,I hope you break your neck and die.",
                "Roses are red, violets are blue, I have 5 fingers, the 3rd ones for you.",
                "Yo momma's so fat, she downloads cheats for Wii Fit.",
                "Why don't you slip into something more comfortable... like a coma.",
                "Yo momma's so ugly when she joined an ugly contest, they said 'Sorry, no professionals.",
                "Yo momma's so ugly she looked out the window and got arrested for mooning."
                "Yo momma's so ugly just after she was born, her mother said What a treasure! and her father said Yes, let's go bury it.",
                "your mom is so fat she ordered a double room for a singles weekend!",
                "Yo' momma's so fat, when she hauls *ss, she has to make two trips!"
                "You’re so ugly that when you cry, the tears roll down the back of your head…just to avoid your face.",]

    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = ""
    msg.add_field(name="INSULT :boom: ", value="{} :bomb:  {}".format(userName.display_name, random.choice(insult)))
    msg.set_footer(text=footer_text)
    await context.send(embed=msg)
    print("============================================================")
    print("INSULT COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")

@insult.error
async def insult_error(ctx, error):
    msg = discord.Embed(title=" :x: Error You forgot something ;) ", colour=random.randint(0, 0xFFFFFF), description="try again with p!insult and mention the user ;) ")
    msg.set_footer(text=" example!! p!insult @Flame.Exe#0001 ")
    await ctx.send(embed=msg)


# QUOTE COMMAND
@client.command(pass_context=True)
async def quote(ctx):
    quotes = ["If you want to achieve greatness stop asking for permission.",
              "Things work out best for those who make the best of how things work out.",
              "To live a creative life, we must lose our fear of being wrong.",
              "What hurts you, but doesn't kill you, makes you stronger.",
              " If you are not willing to risk the usual you will have to settle for the ordinary.",
              "Trust because you are willing to accept the risk, not because it’s safe or certain.",
              "Once you choose hope, anything is possible.",
              "A positive attitude gives you power over your circumstances instead of your circumstances having power over you.",
              "Character cannot be developed in ease and quiet. Only through experience of trial and suffering can the soul be strengthened, ambition inspired, and success achieved.",
              "Keep yourself busy if you want to avoid depression. For me, inactivity is the enemy.",
              "Sometimes, you gotta pretend everything is okay.",
              "It’s always worse than it seems.",
              "I get lost inside my mind”.",
              "All alone! Whether you like it or not, alone is something you'll be quite a lot!",
              "Twinkle, twinkle little star. Let me get hit by a car. Oh, how I really want to die, jump off the roof and try to fly. Twinkle, twinkle little knife, help me end this fucking life!",
              "There’s death all around us. Everywhere we look. 1.8 people kill themselves every second. We just don’t pay attention. Until we do.",
              "I guess that’s what saying good-bye is always like–like jumping off an edge. The worst part is making the choice to do it. Once you’re in the air, there’s nothing you can do but let go.",
              "The sun kept on with its slipping away, and I thought how many small good things in the world might be resting on the shoulders of something terrible.",
              "As the light begins to intensify, so does my misery, and I wonder how it is possible to hurt so much when nothing is wrong.",
              "But grief makes a monster out of us sometimes . . . and sometimes you say and do things to the people you love that you can’t forgive yourself for.",
              "Have you ever wondered what a human life is worth? That morning, my brother’s was worth a pocket watch.",
              "A lot of you cared, just not enough.",
              "Breathing is hard. When you cry so much, it makes you realize that breathing is hard.",
              "It's not I can or I can't, it's I want or I don't want!",
              "It’s raining in my heart like it’s raining in the city. What is this sadness that pierces my heart?",
              "At some point, you have to realize that some people can stay in your heart but not in your life.",
              "I forgive, but I don't forget.",
              "I hate getting flashbacks from things I don't want to remember.",
              "Do you know the feeling of drowning while everyone around you is breathing?",
              "Fake friends are like shadows. They follow you in the sun but leave you in the dark.",
              "You laugh, but you wanna cry. You talk, but you wanna be quiet. Yes, you're smiling, but inside, you're dying.",
              "This life is like a war, you either win with a scar or die trying.",
              "I'm fine.",
              "If I killed myself tonight, the sun will still rise, the stars would still appear, the Earth will still rotate, the seasons will still change... so why not?",
              "No amount of sleep can cure the tiredness I feel.",
              "Even the devil, was once an angel.",
              "I like my music so loud, I can't hear my thoughts.",
              "I smile all the time so that nobody knows how sad and lonely I really am.",
              "My mind was a mess, then I found a razor. Now my body is a mess too.",
              "I draw with silver and it becomes red. Magic!",
              "Why am I so different from everyone else?",
              "Emotionally: I'm done.  Mentally: I'm drained.  Spiritually: I'm dead.  Physically: I smile.",
              "It hurts when you smile just to stop the tears from falling.",
              "My blood is red. My wounds are wide. My heart hurts. I'm dead inside.",
              "I'm not totally useless. I can be used as a bad example.",
              "I'm pretending to be fine. So are they pretending to care?",
              "I'm slowly, but surely, giving up.",
              "People don't cry cause they are weak. They cry cause they were strong for too long.",
              "When I get angry, I don't yell, I don't hit, I don't show rage... I just think about ending it all.",
              "There is a hell, believe me, I've seen it.",
              "Everyone who hurt you, who left you, who didn't understand you, one day will regret it all.",
              "Walking with a friend in the dark is better than walking alone in the light.",
              "Remember, you are not alone. Darkness is and always will be with you.",
              "I don't care if I live or not.",
              "Stop trying to find a point or a meaning. There is no such thing.",
              "Not all scars show. Not all wounds heal. You can't always see the pain that others feel.",
              "We're scared to get close, cause everyone who promised they'll stay, turned their back and left.",
              "I don't like being too happy.",
              "I wanna sleep... forever.",
              "You shall not pass!",
              "You're adopted.",
              "Why should I apologize for being a monster? When no one apologized for turning me into one.",
              "You may not be my happy ending, but you are the best chapter of my life."]
    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = ""
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name=":scroll: Scroll of quotes", value="{}".format(random.choice(quotes)))
    msg.set_footer(text=footer_text)
    await ctx.send(embed=msg)
    print("============================================================")
    print("QUOTE COMMAND")
    print("{}".format(author))
    print("============================================================")


@client.command(pass_context=True)
async def invite(ctx):
    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = "BOT INVITE :incoming_envelope:"
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name=":white_check_mark: ", value="A Invite BOT Is coming your way!\nCheck your DMs, {}!".format(author))
    msg.set_footer(text=footer_text)
    await ctx.send(embed=msg)
    await ctx.message.author.send(" **Here You GO!** https://discordapp.com/oauth2/authorize?client_id=401419300096704525&scope=bot&permissions=2146958591")


@client.command(pass_context=True)
async def server(ctx):
    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = "SERVER INVITE :bulb: "
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name=":white_check_mark: ", value="A Invite Server Is coming your way!\nCheck your DMs, {}!".format(author))
    msg.set_footer(text=footer_text)
    await ctx.send(embed=msg)
    await ctx.message.author.send("DISCORD LINK  https://discord.gg/Tk8RCer ")


# EIGHT BALL COMMAND
@client.command(pass_context=True)
async def eightball(ctx, *, args):
    answer = ["Yes!",
              "No!",
              "Probably!",
              "naa",
              "r u kidding me fuck yes",
              "ik u want the answer but NO!",
              "i'll say YEAH!",
              "TBH, no",
              "lmao whats that",
              "my daddy said no",
              "my mummy said yes",
              "HaHa Of curse",
              "Most likely!",
              "Probably not!",
              "Definately!",
              "Definately not!",
              "Of course!",
              "Of course not!",
              "WTF no!",
              "Hell yeah!"]
    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = "Magic Eight Ball"
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name=":grey_question: Question:", value="{}".format(args), inline=True)
    msg.add_field(name="\n:8ball: Eight Ball:", value="{}".format(random.choice(answer)), inline=True)
    msg.set_footer(text=footer_text)
    await ctx.send(embed=msg)
    print("============================================================")
    print("EIGHTBALL COMMAND")
    print("{}".format(author))
    print("============================================================")

@eightball.error
async def kiss_error(ctx, error):
    msg = discord.Embed(title=" ❌ Error You forgot something ;) ", colour=random.randint(0, 0xFFFFFF), description="try again with p!eightball and ur question the user ;) ")
    msg.set_footer(text=" example!! p!eightball skype or discord ")
    await ctx.send(embed=msg)

# KILL COMMAND
@client.command(pass_context=True)
async def kill(context, userName: discord.User):
    killmsgs = ["died by getting beaten with a baseball bat covered with barbed wire!",
                "died by getting all their bones broken with chains!",
                "died from a nuclear explosion!",
                "died by getting shot in the head by an intruder!",
                "died by drowning in the ocean!",
                "died by getting eaten by a shark!",
                "got roasted so hard, they started burning and died!",
                "died by forgetting how to breathe!",
                "died by falling off the 30th floor!",
                "died by getting crushed by a meteor!",
                "died from radiation!",
                "died trying to fight an anaconda!",
                "died trying to fight darkness!",
                "died by aids!",
                "died from cancer!",
                "had a very stupid death, rather not tell what happened!",
                "died in a volcano!",
                "died by trying to leave the server! Do not try that, they were later revived in a more hell-ish version of their past life!",
                "died from not having memes to look at!",
                "died from a plane crash!",
                "were killed by an mysterious human-like figure!",
                "were killed cause they were a grammar nazi!",
                "were beaten to death by the bullies!",
                ", m8 u ded lol?",
                "died fro- lol jk u not die yet",
                "got their memes stolen and died from a heart attack!",
                "died?",
                "died! Only 2 players left!",
                "were killed in the hunger games!",
                "were killed before they even had a chance to live!",
                "died lmao get r3kt",
                "were killed... BY ME!",
                "tried to cheat on a math test, almost got away with it! Their body was found in a dumpster with a big F on their chest.",
                "was killed by a cute little bunny :3",
                "was killed by Lucifer!",
                "died by watching furry porn!",
                "died.. about time.. JK JK!!",
                "got killed by a true slav!",
                "died by not squating like a true slav!",
                "died by not using google!",
                "died by opening internet explorer!",
                "died from living!",
                "died from acid rain!",
                "got hit by lightning and died!",
                "was a good person! They had a nice family and a nice house, the whole world lived in harmony and peace... until the fire nation attacked!",
                "died by reading a book!",
                "died trying!",
                "died by watching the emoji movie!",
                "died by watching the bee movie!",
                "was killed lol",
                "left the game!",
                "died trying to do a backflip!",
                "got their heart ripped out!",
                "wasn't even born, what are you on about?",
                "can't die, they are already dead!",
                "died from looking at old memes!",
                "was killed by a fidget spinner!",
                "was killed by an attack helicopter!",
                "went inside a white van and never came out!",
                "got their head ripped off!",
                "starved in a supermarket while there was a zombie apocalypse!",
                "died while trying to steal Zero's chocolate!",
                "died by trying to hit a cat!",
                "died by trying to fly!",
                "died by getting hit with an anvil!",
                "died by setting their hair on fire!",
                "was killed by a kat!",
                "was last seen entering a white van!",
                "died by having no internet connection for more than 5 seconds!",
                "died by loosing their hentai stash!",
                "was killed after someone stole their memes!",
                "was killed by a retarded chicken!",
                "died by sun light!",
                "died after commiting suicide!",
                "died trying to perform a magic trick!",
                "left the game.",
                "was always the type of person who fights fire with fire... that didn't end well. They were a fireman!",
                "was killed by a bunneh!",
                "died before they had a chance to live!",
                "died... inside!",
                "had a boring death!",
                "died being a hero!"]

    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = ""
    msg.add_field(name="NEWS :gun:", value="`{} {}`".format(userName.display_name, random.choice(killmsgs)))
    msg.set_footer(text=footer_text)
    await context.send(embed=msg)
    print("============================================================")
    print("KILL COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")


# ROAST COMMAND
@client.command(pass_context=True)
async def roast(context, userName: discord.User):
    roasts = ["I saw a piece of shit today. It reminded me of you.",
              "your face is a physical weapon.",
              "I know you from somewhere. Oh yea, I see you in the trashcan."
              "don't worry, you're not adopted... yet. We still haven't found anyone who wants you.",
              "unless your name is 'Google', stop acting like you know everything.",
              "if I wanted to kill myself I would climb up your ego and jump in your IQ",
              "you are so stupid that you got hit by a parked car.",
              "you're so fat that when god created light, you were asked to move out of the way.",
              "I heard you were taken to a dog show and you won.",
              "you suck so much, I can use you as a vacumcleaner.",
              "maybe you should stop making fun of others just to get attention, cause the world doesn't rotate around your crap looking ass.",
              "try not to spit when you talk, we don't need a public shower here.",
              "you remind me of the owner, eew.",
              "I can't breathe when I see you... cause I'm suffocating of your bullshit.",
              "your mom is twice the man you will ever be.",
              "you have the right to remain silent, cause what ever you say will be stupid anyways.",
              "the only thing you are good at is being a cunt.",
              "it's hard for you isn't it? Not to be a dick.",
              "it's hard to ignore you, mostly cause you smell like shit.",
              "you must've fallen from Mars, cause you clearly can't understand anything happening around you.",
              "did you fall from Heaven? Cause so did Satan.",
              "you're so ugly, you went to an ugly competition and they said 'No professionals allowed!'.",
              "you really shouldn't try cooking, cause the last time you did, it ended with 3 houses being on fire.",
              "did Satan send you to kill people? Cause your smell is killing me.",
              "I'd give you a nasty look but you've already got one.",
              "if laughter is the best medicine, your face must be curing the world.",
              "the only way you'll ever get laid is if you crawl up a chicken's ass and wait.",
              "scientists say the universe is made up of neutrons, protons and electrons. They forgot to mention morons.",
              "your family tree must be a cactus because everyone on it is a prick.",
              "someday you'll go far... and I hope you stay there.",
              "save your breath, you'll need it to blow your date.",
              "the zoo called. They're wondering how you got out of your cage?",
              "you have something on your chin... no, the 3rd one down.",
              "thought of you today. It reminded me to take the garbage out.",
              "you're so ugly when you look in the mirror, your reflection looks away.",
              "it's better to let someone think you're stupid than open your mouth and prove it.",
              "were you born this stupid or did you take lessons?",
              "calling you an idiot would be an insult to all stupid people.",
              "I just stepped in something that was smarter than you... and smelled better too."]
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = ""
    msg.add_field(name=":fire: Roast Machine", value="`{}, {}`".format(userName.display_name, random.choice(roasts)))
    msg.set_footer(text=footer_text)
    await context.send(embed=msg)
    print("============================================================")
    print("ROAST COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")


# HEAVEN COMMAND
@client.command(pass_context=True)
async def heaven(ctx):
    heaven = ["Heaven is Real – God created it",
              "Jesus, the Christ came down to Earth from Heaven",
              "Jesus went back to Heaven when He rose from the dead",
              "Jesus is now seated at the right hand of God (the Majesty) in Heaven",
              "heaven is also known as a place where the birds fly and the clouds float – the Bible also calls this the firmament",
              "heaven is a place where the stars, sun and constellations shine – this is the stellar heaven",
              "Heaven is where the believer goes when he leaves this planet – it is home",
              "Believers can look forward to a new heaven – it is the blessed hope and a perfect place",
              "Heaven is God’s home and He existed before His creation – this is the Heaven of heavens; the high and holy place",
              "Before creation, Jesus (God’s Son) and Holy Spirit lived in Heaven with God", ]
    author = ctx.message.author
    footer_text = "Paradise"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = ""
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name=":angel:  Heaven Facts", value="{}".format(random.choice(heaven)))
    msg.set_footer(text=footer_text)
    await ctx.send(embed=msg)
    print("============================================================")
    print("HEAVEN COMMAND")
    print("{}".format(author))
    print("============================================================")


# SUICIDE COMMAND
@client.command(pass_context=True)
async def suicide(ctx):
    suicide = ["In 2015 (latest available data), there were 44,193 reported suicide deaths in the U.S.",
               "Suicide is the 2nd leading cause of death for those between the ages of 15 and 34 in the United States.",
               "Currently, suicide is the 10th leading cause of death in the United States.",
               "A person dies by suicide about every 12.8 minutes in the United States.",
               "Every day, approximately 121 Americans take their own life.",
               "Ninety percent of all people who die by suicide have a diagnosable psychiatric disorder at the time of their death.",
               "There are four male suicides for every female suicide, but three times as many females as males attempt suicide.",
               "494,169 people visited a hospital for injuries due to self-harm behavior, suggesting that approximately 12 people harm themselves (not necessarily intending to take their lives) for every reported death by suicide.",
               "25 million Americans suffer from depression each year.",
               "Over 50 percent of all people who die by suicide suffer from major depression. If one includes alcoholics who are depressed, this figure rises to over 75 percent.",
               "Depression affects nearly 5-8 percent of Americans ages 18 and over in a given year.",
               "Depression is among the most treatable of psychiatric illnesses. Between 80 percent and 90 percent of people with depression respond positively to treatment, and almost all patients gain some relief from their symptoms. But first, depression has to be recognized.",
               "More Americans suffer from depression than coronary heart disease, cancer, and HIV/AIDS.",
               "Nearly 30,000 Americans commit suicide every year.",
               "In the U.S., suicide rates are highest during the spring.",
               "Suicide is the 3rd leading cause of death for 15 to 24-year-olds and 2nd for 24 to 35-year-olds.",
               "On average, 1 person commits suicide every 16.2 minutes.",
               "Each suicide intimately affects at least 6 other people.",
               "About 2/3 of people who complete suicide are depressed at the time of their deaths. Depression that is untreated, undiagnosed, or ineffectively treated is the number 1 cause of suicide.",
               "There is 1 suicide for every 25 attempted suicides.",
               "Males make up 79% of all suicides, while women are more prone to having suicidal thoughts.",
               " in 65,000 children ages 10 to 14 commit suicide each year.", ]
    author = ctx.message.author
    footer_text = "Paradise "
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = ""
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name=":skull: Suicide Facts", value="{}".format(random.choice(suicide)))
    msg.set_footer(text=footer_text)
    await ctx.send(embed=msg)
    print("============================================================")
    print("SUICIDE COMMAND")
    print("{}".format(author))
    print("============================================================")


# SAY COMMAND
@client.command(pass_context=True)
async def say(context, *, args):
    await context.send("`{}`".format(args))
    print("============================================================")
    print("SAY COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")


# USER INFO COMMAND
@client.command(pass_context=True)
async def profile(context, userName: discord.Member):
    imageurl = userName.avatar_url
    author = context.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
    msg.title = ":page_with_curl: USER INFORMATION"
    msg.set_thumbnail(url=imageurl)
    msg.set_author(name=str(userName), icon_url=userName.avatar_url)
    msg.add_field(name="NAME:", value=(userName), inline=True)
    msg.add_field(name="ID:", value=(userName.id), inline=True)
    msg.add_field(name="CREATED AT:", value=(userName.created_at), inline=True)
    msg.add_field(name="JOINED AT:", value=(userName.joined_at), inline=True)
    msg.add_field(name="STATUS:", value=(userName.status), inline=True)
    msg.add_field(name="IS BOT:", value=(userName.bot), inline=True)
    msg.add_field(name="GAME:", value=(userName.game), inline=True)
    msg.add_field(name="NICKNAME:", value=(userName.nick), inline=True)
    msg.add_field(name="TOP ROLE:", value=(userName.top_role), inline=True)
    msg.set_footer(text=footer_text)
    await context.send(embed=msg)
    print("============================================================")
    print("PROFILE COMMAND")
    print("{}".format(author))
    print("============================================================")


'''
MODERATION COMMANDS
'''


# RAW SAY COMMAND
@client.command(pass_context=True)
async def rawsay(context, *, args):
    for role in context.message.author.roles:
        if role.name == "Paradise Bot":
            await context.send("{}".format(args))
            print("============================================================")
            print("RAWSAY COMMAND")
            print("{}".format(context.message.author))
            print("============================================================")


# TAKE/GIVE ROLE COMMAND
@client.command(pass_context=True)
async def takerole(ctx, userName: discord.Member, *, rolename):
    for role in ctx.message.author.roles:
        if role.name == "Paradise Bot":
            rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(rolename))
            await client.remove_roles(userName, rolename2)
            author = ctx.message.author
            footer_text = "Paradise ☁"
            msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
            msg.title = ""
            msg.set_author(name=str(author.name), icon_url=author.avatar_url)
            msg.add_field(name=":outbox_tray: Taking away role...",
                          value="`{} has removed {} from {}`".format(ctx.message.author, rolename2,
                                                                     userName.display_name), inline=True)
            msg.set_footer(text=footer_text)
            await ctx.send(embed=msg)
            print("============================================================")
            print("TAKEROLE COMMAND")
            print("{}".format(author))
            print("============================================================")


@client.command(pass_context=True)
async def giverole(ctx, userName: discord.Member, *, rolename):
    for role in ctx.message.author.roles:
        if role.name == "Paradise Bot":
            rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(rolename))
            await client.add_roles(userName, rolename2)
            author = ctx.message.author
            footer_text = "Paradise ☁"
            msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
            msg.title = ""
            msg.set_author(name=str(author.name), icon_url=author.avatar_url)
            msg.add_field(name=":inbox_tray: Giving role...",
                          value="`{} has given {} to {}`".format(ctx.message.author, rolename2, userName.display_name),
                          inline=True)
            msg.set_footer(text=footer_text)
            await ctx.send(embed=msg)
            print("============================================================")
            print("GIVEROLE COMMAND")
            print("{}".format(author))
            print("============================================================")


# UNBAN COMMAND
@client.command(pass_context=True)
async def unban(ctx, userID):
    for role in ctx.message.author.roles:
        if role.name == "Paradise Bot":
            banned_users = await client.get_bans(ctx.message.server)
            user = discord.utils.get(banned_users, id=userID)
            if user is not None:
                await client.unban(ctx.message.server, user)
                author = ctx.message.author
                footer_text = "Paradise ☁"
                msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
                msg.title = ""
                msg.set_author(name=str(author.name), icon_url=author.avatar_url)
                msg.add_field(name=":tools: UNBAN TOOLS",
                              value="`{}#{} has been unbanned by {}!`".format(user.name, user.discriminator,
                                                                              ctx.message.author), inline=True)
                msg.set_footer(text=footer_text)
                await ctx.send(embed=msg)
                print("============================================================")
                print("UNBAN COMMAND")
                print("{}".format(author))
                print("============================================================")
            else:
                author = ctx.message.author
                footer_text = "Paradise ☁"
                msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
                msg.title = ""
                msg.set_author(name=str(author.name), icon_url=author.avatar_url)
                msg.add_field(name=":octagonal_sign: ERROR", value="`{} isn't banned!`".format(user.name), inline=True)
                msg.set_footer(text=footer_text)
                await ctx.send(embed=msg)
                print("============================================================")
                print("UNBAN COMMAND")
                print("{}".format(author))
                print("============================================================")


# KICK COMMAND
def kick_msg_generator(user="unknown", reason="unknown", status="unresolved", desc=""):
    em = discord.Embed(color=discord.Color.gold(), title="Moderation: KICK", description=desc)
    if not user == "unknown":
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="User:", value=user.name, inline=False)
    else:
        em.add_field(name="User:", value=user, inline=False)
    em.add_field(name="Reason:", value=reason, inline=False)
    em.set_footer(text="Status: {}".format(status))
    return em


@client.command(pass_context=True)
async def kick(ctx):
    message = ctx.message
    if not message.author.guild_permissions.kick_members:
        await ctx.send(":x: **You do not have permission to kick members!**")
        return

    status_msg = await ctx.send(embed=kick_msg_generator())
    q1 = await ctx.send(":cop: **Mention the user you want to kick:**")

    def check_q1(m):
        try:
            mentions = m.mentions[0]
        except IndexError:
            mentions = False
        return mentions and m.channel == message.channel and m.author == message.author

    try:
        u_msg = await client.wait_for('message', check=check_q1, timeout=60.0)
        k_user = u_msg.mentions[0]
    except asyncio.TimeoutError:
        try:
            await status_msg.delete()
            await q1.delete()
        except (discord.errors.Forbidden, discord.errors.NotFound):
            pass
        await message.channel.send(":x: **Kick case canceled!**")
        return
    else:
        await status_msg.edit(embed=kick_msg_generator(k_user))
        try:
            await u_msg.delete()
        except (discord.errors.Forbidden, discord.errors.NotFound):
            pass
        await q1.edit(content=":notepad_spiral: **Type the reason of the kick (type '-' for nothing):**")

        def check_q2(m):
            return m.channel == message.channel and m.author == message.author

        try:
            r_msg = await client.wait_for('message', check=check_q2, timeout=60.0)
        except asyncio.TimeoutError:
            try:
                await status_msg.delete()
                await q1.delete()
                await r_msg.delete()
            except (discord.errors.Forbidden, discord.errors.NotFound, UnboundLocalError):
                pass
            await message.channel.send(":x: **Kick case canceled!**")
            return
        else:
            r_txt = r_msg.content
            try:
                await r_msg.delete()
                await q1.delete()
            except discord.errors.NotFound:
                pass
            await status_msg.edit(embed=kick_msg_generator(k_user, r_txt, "Waiting for conformation",
                                                           "**React with ✅ to confirm kick or with ❌ to cancel.**"))
            await status_msg.add_reaction('✅')
            await status_msg.add_reaction('❌')

            def check_r(reaction, user):
                return user == message.author and (str(reaction.emoji) == '❌' or str(reaction.emoji) == '✅')

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check_r)
            except asyncio.TimeoutError:
                try:
                    await status_msg.delete()
                except discord.errors.NotFound:
                    pass
                await ctx.send(":x: **Kick case canceled!**")
            else:
                if str(reaction) == '✅':
                    try:
                        await status_msg.clear_reactions()
                        await status_msg.edit(embed=kick_msg_generator(k_user, r_txt, "Resolved",
                                                                       "Kicked by: {}".format(message.author.name)))
                    except discord.errors.NotFound:
                        pass
                    try:
                        await message.guild.kick(user=k_user)
                    except discord.errors.Forbidden:
                        await ctx.send(
                            ":white_check_mark: **This user cannot be kicked by a bot!**")
                        try:
                            await status_msg.delete()
                        except discord.errors.NotFound:
                            pass
                        return
                elif str(reaction) == '❌':
                    await status_msg.delete()
                    await ctx.send(":x: **Kick case canceled!**")
                else:
                    await status_msg.clear_reactions()
                    await ctx.send("**An error occurred.**")


# BAN COMMAND
@client.command(pass_context=True)
async def ban(ctx, userName: discord.Member, days=None):
    message = ctx.message
    if not message.author.guild_permissions.ban_members:
        await ctx.send(":x: **You do not have permission to ban members!**")
        return
    if days == None:
        await ctx.message.guild.ban(user=userName)
        author = ctx.message.author
        footer_text = "Paradise ☁"
        msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
        msg.title = ""
        msg.set_author(name=str(author.name), icon_url=author.avatar_url)
        msg.add_field(name=":hammer: BAN HAMMER",
                      value="`{} has been banned by {}! No messages were deleted!`".format(
                          userName.display_name, ctx.message.author), inline=True)
        msg.set_footer(text=footer_text)
        await ctx.send(embed=msg)
        print("============================================================")
        print("BAN COMMAND")
        print("{}".format(author))
        print("============================================================")
    else:
        await ctx.message.guild.ban(user=userName, delete_message_days=days)
        author = ctx.message.author
        footer_text = "Paradise ☁"
        msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description="")
        msg.title = ""
        msg.set_author(name=str(author.name), icon_url=author.avatar_url)
        msg.add_field(name=":hammer: BAN HAMMER",
                      value="`{} has been banned by {}! Deleting messages from the past {} days...`".format(
                          userName.display_name, ctx.message.author, days), inline=True)
        msg.set_footer(text=footer_text)
        await ctx.send(embed=msg)
        print("============================================================")
        print("BAN COMMAND")
        print("{}".format(author))
        print("============================================================")
		
		
async def send_announcment(server_id, embed):
    guild = client.get_guild(int(server_id))
    f_channel = None
    try:
        if guild.system_channel is not None:
            await guild.system_channel.send(embed=embed)
        else:
            for c in guild.text_channels:
                if not c.permissions_for(guild.me).send_messages:
                    continue
                f_channel = c
                break
            if f_channel is not None:
                await f_channel.send(embed=embed)
    except Exception:
        print("Sending announcement failed!")
		
@client.command(pass_context=True)
async def announce(ctx, *, args):
    if int(ctx.message.author.id) != 398409207793319936:
        await ctx.send("Not allowed!")
        return
    msg = discord.Embed(title="Announcement:", color=discord.Color.green(), description=" __**- Hi Guys Paradise shes Back use p!help for more commands**__ | [CLICK ME](https://www.patreon.com/paradisebot)".format(args))
    msg.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    msg.set_footer(icon_url=client.user.avatar_url, text="Thank You! For Supporting Paradise Bot :) ")
    for guild in client.guilds:
        try:
            await send_announcment(guild.id, msg)
        except Exception as e:
            print("There was an error: {}".format(e))
'''
'''
# THIS WILL TURN ON YOUR BOT
requests.post('https://cleverbot.io/1.0/create', json={'user': CBuser, 'key': CBkey, 'nick': 'Paradise'})

client.run(os.getenv('Token'))
