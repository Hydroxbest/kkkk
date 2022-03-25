import discord
from webserver import keep_alive
from discord.ext import commands, tasks
import random
import os
import colorama
from colorama import Fore
import string
import requests
from datetime import *
import time
import sys
from pyfiglet import Figlet
import time
import random
import base64
import asyncio
import discord
import json
import time
import datetime
from datetime import date,timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re, time
from urllib import parse
from urllib.request import Request, urlopen
from proxyscrape import create_collector


client = commands.Bot(command_prefix= "-", self_bot=True, help_command=None)





@client.command(aliases = ["h"])
async def help(ctx):
 await ctx.send(f'```\nMenu By ˜”*°•.MR.Incognito.•°*”˜#0001\n-nitrogen <amount>\n-spam <amount> <text>\n-stopspam yes\n-coinflip\n-watching <text>\n-stopwatching\n-listening <text>\n-stoplistening\n-stream\n-usdtobtc <amount>\n-btctousd <amount>\n-stopspam <text>\n-cum\n-terrorist\n-nickname <text>\n-junknickname\n-hack <@user>\n-ip <ip>\n-haxor <text>\n-ping <@user>\n-shrug\n-pfp <@user>\n-dox <user>\n-dick <@user>\n-junk\n-purge <amount>\n-hypesquad<bravery,brilliance,balance,random>\n-shutdown```')

#use the .env feature to hide your token

@client.event
async def on_ready():
    # and set False
    global stop_spam_flag
    stop_spam_flag = False
    print(f'Logged in as {client.user}')


#code 
purple_dark= 0x6a006a
purple_medium= 0xa958a5
purple_light= 0xc481fb
orange= 0xffa500
gold= 0xdaa520
red_dark= 8e2430
red_light= 0xf94343
blue_dark= 0x3b5998
cyan= 0x5780cd
blue_light= 0xace9e7
aqua= 0x33a1ee
pink= 0xff9dbb
green_dark= 0x2ac075
green_light= 0xa1ee33
white= 0xf9f9f6
cream= 0xffdab9

@client.command()
async def nitrogen(ctx, arg):
    global status
    await ctx.send(f"Generating {arg} nitro codes...")
    amount = int(arg)
    await ctx.message.delete()
    nitrocodes = ""
    print(Fore.YELLOW + f"[>] Generating {arg} nitro codes...")
    for i in range(0,amount):
        code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        nitrocode = "https://discord.gift/" + code + "\n"
        nitrocodes += nitrocode
        status = "Generating..."
    print(Fore.GREEN + f"[>] Generated")
    myfile = open("codes.txt","w+")
    myfile.write("CODES: " + "\n")
    myfile.close()
    myfile2=open("codes.txt", "a+")
    myfile2.write(nitrocodes)
    myfile2.close
    endfile=discord.File("codes.txt")
    await ctx.send(file=endfile)
    print(Fore.GREEN + f"[>] Sent")
    status = "Finished"
    endfile.close()
    f = open('codes.txt', 'r+')
    f.truncate(0)
    f.close()







@client.command()
async def ip(ctx, ip: str=None):
    if ip is None: await ctx.send("Please sepcify an IP address");return
    else:
        try:
            with requests.session() as ses:
                resp = ses.get(f'https://ipinfo.io/{ip}/json')
                if "Wrong ip" in resp.text:
                    await ctx.send("Invalid IP address")
                    return
                else:
                    try:
                        j = resp.json()
                        embed= discord.Embed(color= blue_light, title=f"INFO",timestamp=datetime.utcfromtimestamp(time.time()))
                        embed.add_field(name=f'IP', value=f'{ip}', inline=True)
                        embed.add_field(name=f'City', value=f'{j["city"]}', inline=True)
                        embed.add_field(name=f'Region', value=f'{j["region"]}', inline=True)
                        embed.add_field(name=f'Country', value=f'{j["country"]}', inline=True)
                        embed.add_field(name=f'Coordinates', value=f'{j["loc"]}', inline=True)
                        embed.add_field(name=f'Postal', value=f'{j["postal"]}', inline=True)
                        embed.add_field(name=f'Timezone', value=f'{j["timezone"]}', inline=True)
                        embed.add_field(name=f'Organization', value=f'{j["org"]}', inline=True)
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
        except Exception as e:
            await ctx.send(f"Error: {e}")


@client.command()
async def spfp(ctx):
    try:
        embed= discord.Embed(color= aqua, description=f"[Server Icon]({ctx.guild.icon_url})",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
    except discord.HTTPException:    
        await ctx.send(f"{ctx.guild.icon_url}")
    except:
        await ctx.send(f"You must be into a guild! For user avatar use {ctx.prefix}pfp <user>")

@client.command()
async def pfp(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send(f"Usage: {ctx.prefix}pfp <user>")
    else:
        try:
            embed= discord.Embed(color= purple_dark, description=f"[{user.name}'s Avatar]({user.avatar_url})",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_image(url=user.avatar_url)
            await ctx.send(embed=embed)
        except discord.HTTPException:    
            await ctx.send(f"{user.avatar_url}")
        except Exception as e:
            await ctx.send(f"Eror: {e}")

@client.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')

@client.command(aliases=["jerkoff", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')




@client.command()
async def hack(ctx, user: discord.Member = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")



@client.command()
async def dick(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    await ctx.send(f"{user.mention}'s Dick size\n8{dong}D")





@client.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))



@client.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://333hub.tk/",
    )
    await client.change_presence(activity=stream)


@client.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await client.change_presence(activity=game)


@client.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))


@client.command()
async def invisiblenickname(ctx):
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
        await ctx.send(f"Now your nickname is invisible")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@client.command()
async def junknickname(ctx):

    try:
        name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫" 
        await ctx.author.edit(nick=name)
        await ctx.send(f"Now your nickname is a big mess :)")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@client.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await client.change_presence(activity=None, status=discord.Status.dnd)


@client.command()
async def nickname(ctx, *, name: str=None):
    if name is None:
        await ctx.send(f"Usage: {ctx.prefix}rename <new name>")
    elif len(name) < 1:
        await ctx.send("Name need to have atleast 1 characters")
    else:
        try:
            await ctx.author.edit(nick=name)
            await ctx.send(f"Change nickname into `{name}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")


@client.command()
async def ping(ctx):
    try:
        embed= discord.Embed(color= green_light, title=f"Pong",timestamp=datetime.utcfromtimestamp(time.time()))
        before = time.monotonic()
        message = await ctx.send(embed=embed)
        await asyncio.sleep(1)
        ping = (time.monotonic() - before) * 1000
        embed= discord.Embed(color= green_light, title=f"Ping: {int(ping)}ms",timestamp=datetime.utcfromtimestamp(time.time()))
        await message.edit(embed=embed)

    except discord.HTTPException:
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Ping: `{int(ping)}ms`")


@client.command()
async def usdtobtc(ctx, num:int=None):
    if num is None:
        await ctx.send("Invalid format pal")
    else:
        with requests.session() as ses:
            resp = ses.get('https://blockchain.info/ticker')
            pret = int(resp.json()['USD']['last'])
            final = num/pret
            try:
                embed= discord.Embed(color= orange, title="USD -> BTC", description=f"USD: {num}\n BTC: {final}",timestamp=datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url="https://i.imgur.com/GCPDIYU.png")
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"USD -> BTC:\n\nUSD: {num}\n BTC: {final}")



@client.command()
async def btctousd(ctx, num:int=None):
    if num is None:
        await ctx.send("Invalid format pal")
    else:
        with requests.session() as ses:
            resp = ses.get('https://blockchain.info/ticker')
            pret = int(resp.json()['USD']['last'])
            final = num*pret
            try:
                embed= discord.Embed(color= orange, title="BTC -> USD", description=f"BTC: {num}\n USD: {final}",timestamp=datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url="https://i.imgur.com/HHSzzNz.png")
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"BTC -> USD:\n\nBTC: {num}\n USD: {final}")

@client.command()
async def shrug(ctx):
    await ctx.send("¯\_(ツ)_/¯")



@client.command()
async def junk(ctx):
    for each in range(0, 11):
        d = "\n"*100
        await ctx.send(f".{d}.")

@client.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass



@client.command()
async def haxor(ctx, *, message: str=None):
    
    if message is None:
        await ctx.send("Insert message sir")
    else:
        try:
            word = message
            leetmsg = word
            leetwords = "aeioutsyou"
            for letter in word:
                if letter in leetwords:
                    leetmsg = leetmsg.replace('a', str(4))
                    leetmsg = leetmsg.replace('e', str(3))
                    leetmsg = leetmsg.replace('i', str(1))
                    leetmsg = leetmsg.replace('o', str(0))
                    leetmsg = leetmsg.replace('t', str(7))
                    leetmsg = leetmsg.replace('s', '$')
                    leetmsg = leetmsg.replace('you', 'j00')

            embed= discord.Embed(color= green_dark, title="1337 Haxor", description=f"{leetmsg.upper()}",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/TR2cv3C.jpg")
            await ctx.send(embed=embed)
        except discord.HTTPException:
            word = message
            leetmsg = word
            leetwords = "aeioutsyou"
            for letter in word:
                if letter in leetwords:
                    leetmsg = leetmsg.replace('a', str(4))
                    leetmsg = leetmsg.replace('e', str(3))
                    leetmsg = leetmsg.replace('i', str(1))
                    leetmsg = leetmsg.replace('o', str(0))
                    leetmsg = leetmsg.replace('t', str(7))
                    leetmsg = leetmsg.replace('s', '$')
                    leetmsg = leetmsg.replace('you', 'j00')
            await ctx.send(f"{leetmsg.upper()}")



@client.command()
async def dox(ctx, user: discord.Member=None):
    emaillist = random.choice(["gmx.de", "yahoo.com", "protonmail.com", "gmail.com"])
    nr = random.choice(range(0,9999))
    ip = random.choice(["127.0.0.1", "192.168.0.1", "192.168.0.101"])
    country = random.choice(['Niger', 'Niggeria', "3rd wolrd country", "Africa"])
    if user is None:
        await ctx.send("Please mention a member")
    else:
        try:
            embed= discord.Embed(color= green_dark, title=f"Doxing in progress %0",description="Getting his email and address",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            a = await ctx.send(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color= green_dark, title=f"Doxing in progress %50",description="Getting ip and stuffs",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color= green_dark, title=f"Doxing in progress %100",description="Getting mom credit cards",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color= green_dark, title=f"Dox of {user.name}",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.add_field(name=f'Email', value=f'{user.name}{nr}@{emaillist}', inline=False)
            embed.add_field(name=f'IP', value=f'{ip}', inline=False)
            embed.add_field(name=f'Country', value=f'{country}', inline=False)
            await a.edit(embed=embed)
            await asyncio.sleep(2)
        except discord.HTTPException:
            a = await ctx.send("Doxing in progress %0 - Getting his email and address")
            await asyncio.sleep(2)
            await a.edit(content="Doxing in progress %50 - Getting ip and stuffs")
            await asyncio.sleep(2)
            await a.edit(content="Doxing in progress %100 - Getting mom credit cards")
            await asyncio.sleep(2)
            await a.edit(content=f"Dox of {user.name}:\n\nEmail: {user.name}{nr}@{emaillist}\nIP: {ip}\nCountry: {country}")


@client.command()
async def shutdown(ctx):
    def check(m):
            return m.author == ctx.author and m.content == "yes" or m.content == "y"
    await ctx.send("‎‏‏‎You have 10 seconds type `y` or `yes` or command will be avoided")
    try:
        m = await client.wait_for('message', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Command avoided")
            
    else:
        os._exit(0)


@client.command()
async def coinflip(ctx):
    lista = ['head', 'tails']
    coin = random.choice(lista)
    try:
        if coin == 'head':
            embed= discord.Embed(color= orange, title="Head",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://webstockreview.net/images/coin-clipart-dime-6.png")
            await ctx.send(embed=embed)
        else:
            embed= discord.Embed(color= orange, title="Tails",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
            await ctx.send(embed=embed)
    except discord.HTTPException:
        if coin == 'head':
            await ctx.send("Coinflip: **Head**")
        else:
            await ctx.send("Coinflip: **Tails**")


@client.command(name="spam", help="spam some message")
async def spam(ctx, times:int, *, message):
    global stop_spam_flag
    for i in range(times):
        await ctx.send(message)
        if stop_spam_flag:
            break
    stop_spam_flag = False

@client.command(name="stopspam", help="stops the spam messages")
async def stopspam(ctx, *, message):
    user = ctx.author
    global stop_spam_flag
    if message == 'yes':
        stop_spam_flag = True, await ctx.send(f"{user.mention} 😎 Your cool you stopped the spam")



@client.command()
async def servers(ctx):
    messages = []
    for guild in client.guilds:
         messages.append(f"**🔹{guild.name}**")
    await ctx.send("\n".join(messages))



@client.command()
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')




@client.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    link = str(r['message'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_dog.png"))
    except:
        await ctx.send(link)

@client.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_cat.png"))
    except:
        await ctx.send(link)


@client.command()
async def sadcat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/sadcat").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_sadcat.png"))
    except:
        await ctx.send(link)


@client.command()
async def bird(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/birb").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_bird.png"))
    except:
        await ctx.send(link)

@client.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    link = str(r["image"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"exeter_fox.png"))
    except:
        await ctx.send(link)


@client.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=5).flatten()
    for message in messages:
        await message.add_reaction(emote)



@client.command(pass_context=True)
async def autoOwO(ctx):
	await ctx.message.delete()
	await ctx.send('auto OwO is now **enabled**!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send('owoh')
			print(f"{Fore.GREEN}succefully owoh")
			await asyncio.sleep(15)
			await ctx.send('owo sell all')
			print(f"{Fore.GREEN}succefully sell")
			await ctx.send('owo flip 500')
			print(f"{Fore.GREEN}succefully owo flip 500")
			await asyncio.sleep(10)
			await ctx.send('owo cash')
			print(f"{Fore.GREEN}succefully cash")
			await asyncio.sleep(10)


@client.command()
async def stopautoOwO(ctx):
	await ctx.message.delete()
	await ctx.send('auto OwO is now **disabled**!')
	global dmcs
	dmcs = False



@client.command(aliases=['spamchangegcname', 'changegcname'])
async def gcspam(ctx):
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = '˜”*°•.MR.Incognito.•°*”˜#0001 on top'
        name = ''
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)

@client.command()
async def virus(ctx, user: discord.Member = None, *, virus: str = "trojan"):
        user = user or ctx.author
        list = (
            f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
            f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
            f"``Successfully downloaded {virus}-virus.exe``",
            "``Injecting virus.   |``",
            "``Injecting virus..  /``",
            "``Injecting virus... -``",
            f"``Successfully Injected {virus}-virus.exe into {user.name}``",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)


@client.command()
async def fn(ctx):
    await ctx.message.delete()
    message = await ctx.send("""```
    ⣀⣤
⠀⠀⠀⠀⣿⠿⣶
⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⣶⣶⣿⠿⠛⣶
⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤
⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀
⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿
⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉
⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿
⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿
⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿
⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿
⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿
⠀⠀⠀⠛⠛
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
   ⣀⣶⣀
⠀⠀⠀⠒⣛⣭
⠀⠀⠀⣀⠿⣿⣶
⠀⣤⣿⠤⣭⣿⣿
⣤⣿⣿⣿⠛⣿⣿⠀⣀
⠀⣀⠤⣿⣿⣶⣤⣒⣛
⠉⠀⣀⣿⣿⣿⣿⣭⠉
⠀⠀⣭⣿⣿⠿⠿⣿
⠀⣶⣿⣿⠛⠀⣿⣿
⣤⣿⣿⠉⠤⣿⣿⠿
⣿⣿⠛⠀⠿⣿⣿
⣿⣿⣤⠀⣿⣿⠿
⠀⣿⣿⣶⠀⣿⣿⣶
⠀⠀⠛⣿⠀⠿⣿⣿
⠀⠀⠀⣉⣿⠀⣿⣿
⠀⠶⣶⠿⠛⠀⠉⣿
⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⣶⣿⠿
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠶⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿
⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⣀
⠀⠿⣿⣿⣀
⠀⠉⣿⣿⣀
⠀⠀⠛⣿⣭⣀⣀⣤
⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀
⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶
⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿
⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿
⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿
⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿
⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀
⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶
⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉
⣀⣶⣿⠛
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿
⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉
⠀⠀⠀⠀⠀⠀⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉
⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿
⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣛⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀
⠀⠀⠀⠀⠀⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠉
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⣤⣶⣶
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀
⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿
⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿
⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿
⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤
⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿
⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛
⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿
⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⠤⣿⠿⠿⠿
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⣀
⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤
⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀
⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀
⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣤⣤⣤⣿⣿⣿
⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿
⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶
⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤
⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿
⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣶
⠀⠀⠀⠀⣿⠉⠿⣿⣿
⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿
⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶
⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶
⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤
⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀
⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿
⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶
⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒
⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉
⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛
⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿
⠀⠀⠀⠀⠀⠀⣿⠛
⠀⠀⠀⠀⠀⠀⣭⣶
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀
⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀
⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣿⣿⣿⣀
⠀⣀⣿⣿⣿⣿⣿⣿
⣶⣿⠛⣭⣿⣿⣿⣿
⠛⠛⠛⣿⣿⣿⣿⠿
⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣀⣭⣿⣿⣿⣿⣀
⠀⠤⣿⣿⣿⣿⣿⣿⠉
⠀⣿⣿⣿⣿⣿⣿⠉
⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣿⣿
⠉⠛⣿⣿⣶⣤
⠀⠀⠉⠿⣿⣿⣤
⠀⠀⣀⣤⣿⣿⣿
⠀⠒⠿⠛⠉⠿⣿
⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⣶⠿⠿⠛
```""")



@client.command()
async def createtxt(ctx, *, txt=''):
	await ctx.message.delete()
	if txt == '':
		await ctx.send('provide a message dude')
	else:
		file = open("customtxtfile.txt", "w")
		file.write(txt)
		file.close()
		pp = discord.File(fp="customtxtfile.txt")
		await ctx.send(f"here is your txt file {ctx.author.name} ↓", file=pp)


@client.command()
async def smalltxt(ctx, *, text=None):
	await ctx.message.delete()
	if text is None:
		await ctx.send("what do you want as a small message???")
	else:
		frt = text.replace('a', 'ᴬ').replace('A', 'ᴬ').replace(
		    'b',
		    'ᴮ').replace('B', 'ᴮ').replace('c', 'ᶜ').replace('C', 'ᶜ').replace(
		        'd', 'ᴰ').replace('D', 'ᴰ').replace('e', 'ᴱ').replace(
		            'E', 'ᴱ').replace('f', 'ᶠ').replace('F', 'ᶠ').replace(
		                'g', 'ᴳ').replace('G', 'ᴳ').replace('h', 'ᴴ').replace(
		                    'H',
		                    'ᴴ').replace('i', 'ᴵ').replace('I', 'ᴵ').replace(
		                        'j', 'ᴶ').replace('J', 'ᴶ').replace(
		                            'k', 'ᴷ').replace('K', 'ᴷ').replace(
		                                'l', 'ᴸ').replace('L', 'ᴸ').replace(
		                                    'm', 'ᴹ'
		                                ).replace('M', 'ᴹ').replace(
		                                    'n', 'ᴺ'
		                                ).replace('N', 'ᴺ').replace(
		                                    'o', 'ᴼ'
		                                ).replace('O', 'ᴼ').replace(
		                                    'p', 'ᴾ'
		                                ).replace('P', 'ᴾ').replace(
		                                    'q', 'ᵠ'
		                                ).replace('Q', 'ᵠ').replace(
		                                    'r', 'ᴿ'
		                                ).replace('R', 'ᴿ').replace(
		                                    's', 'ˢ'
		                                ).replace('S', 'ˢ').replace(
		                                    't', 'ᵀ'
		                                ).replace('T', 'ᵀ').replace(
		                                    'u', 'ᵁ'
		                                ).replace('U', 'ᵁ').replace(
		                                    'v', 'ⱽ'
		                                ).replace('V', 'ⱽ').replace(
		                                    'w', 'ᵂ'
		                                ).replace('W', 'ᵂ').replace(
		                                    'x', 'ˣ').replace(
		                                        'X', 'ˣ').replace(
		                                            'y', 'ʸ').replace(
		                                                'Y', 'ʸ').replace(
		                                                    'z', 'ᶻ').replace(
		                                                        'Z', 'ᶻ')
		await ctx.send(frt)



@client.command()
async def hooksend(ctx, webhook, *, message):
    await ctx.message.delete()
    _json = {"content": message}
    requests.post(webhook, json=_json)
    rs = requests.get(webhook).json()
    if "Unknown Webhook" or "Invalid" in rs["message"]:
        await ctx.send('Sent message', delete_after=2)
    else:
        await ctx.send(f'Successfully sent `{message}` to webhook `{webhook}`', delete_after=2)




@client.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization': TOKEN,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)



@client.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"karamveerselfbot_boobs.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)





@client.command(aliases=['halftoken'])
async def tokenhalf(ctx, member: discord.Member):#
    string = member.id
    string = str(string)
    data = base64.b64encode(string.encode())
    final = str(data).replace("'","")
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await ctx.send(f"{member.name}'s Token Begins With : \n`{final[1:]}`")
    await ctx.message.edit(content="",embed=embed)


@client.command()
async def fucking(ctx):
	await ctx.message.delete()
	message = await ctx.send("8==D     {(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==D    {(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==D   {(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==D  {(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==D {(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==D{(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==D(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==.)}")
	await asyncio.sleep(2)
	await message.edit(content="8==D{(.)}")
	await asyncio.sleep(0.5)
	await message.edit(content="8==D~{(.)}")
	await asyncio.sleep(0.5)
	await message.edit(content="8==D~~{(.)}")

@client.command(aliases=["cyanblock"])
async def cyantext(ctx,*,message):
    await ctx.send(message)
    await ctx.message.edit(content=f"```json\n\"{message}\"```")


@client.command()
async def Incognito(ctx):
    await ctx.send("""``` ___                             _ _        
|_ _|_ __   ___ ___   __ _ _ __ (_) |_ ___  
 | || '_ \ / __/ _ \ / _` | '_ \| | __/ _ \ 
 | || | | | (_| (_) | (_| | | | | | || (_) |
|___|_| |_|\___\___/ \__, |_| |_|_|\__\___/ 
                     |___/                  
```""")
    await ctx.message.delete()

@client.command()
async def bots(ctx):
    bots = []
    for member in ctx.guild.members:
        if member.bot:
            bots.append(
                str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
    bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
    await ctx.send(bottiez)


@client.command()
async def adminservers(ctx):
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in client.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)


@client.command(aliases=["rick"])
async def rickroll(ctx):
  await ctx.message.delete()
  message = await ctx.send(f'Were no stangers to love')
  time.sleep(1.5)
  await message.edit(content='You know the rules and so do I') 
  time.sleep(1.5)
  await message.edit(content='A full commitments what Im thinking of') 
  time.sleep(1.5)
  await message.edit(content='You wouldnt get this from any other guy') 
  time.sleep(1.5)
  await message.edit(content='I just wanna tell you how Im feeling') 
  time.sleep(1.5)
  await message.edit(content='Gotta make you understand') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye') 
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you') 
  time.sleep(1.5)
  await message.edit(content='We known each other for so long') 
  time.sleep(1.5)
  await message.edit(content='Your hearts been aching but your too shy to say it')
  time.sleep(1.5)
  await message.edit(content='Inside we both know whats been going on') 
  time.sleep(1.5)
  await message.edit(content='We know the game and were gonna play it')
  time.sleep(1.5)
  await message.edit(content='And if you ask me how Im feeling') 
  time.sleep(1.5)
  await message.edit(content='Dont tell me your too blind to see') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down')
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye')
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye') 
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give, never gonna give')
  time.sleep(1.5)
  await message.edit(content='(Give you up)') 
  time.sleep(1.5)
  await message.edit(content='(Ooh) Never gonna give, never gonna give') 
  time.sleep(1.5)
  await message.edit(content='(Give you up)')
  time.sleep(1.5)
  await message.edit(content='We known each other for so long') 
  time.sleep(1.5)
  await message.edit(content='Your hearts been aching but your too shy to say it')
  time.sleep(1.5)
  await message.edit(content='Inside we both know whats been going on') 
  time.sleep(1.5)
  await message.edit(content='We know the game and we gonna play it') 
  time.sleep(1.5)
  await message.edit(content='I just wanna tell you how Im feeling')
  time.sleep(1.5)
  await message.edit(content='outta make you understand') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up')
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(conetent='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry') 
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye')
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you')
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you')
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye') 
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye') 
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt...') 
  time.sleep(1.5)


@client.command(aliases=['load'])
async def loading(ctx, *, args='srsly'):
    await ctx.message.delete()
    message = await ctx.send(f'..--------------------------')
    await message.edit(content='...------------------------')
    await message.edit(content='....-----------------------')
    await message.edit(content='....-----------------------')
    await message.edit(content='.....----------------------')
    await message.edit(content='......---------------------')
    await message.edit(content='.......--------------------')
    await message.edit(content='........-------------------')
    await message.edit(content='.........------------------')
    await message.edit(content='..........-----------------')
    await message.edit(content='...........----------------')
    await message.edit(content='............---------------')
    await message.edit(content='.............--------------')
    await message.edit(content='..............-------------')
    await message.edit(content='...............------------')
    await message.edit(content='................-----------')
    await message.edit(content='.................----------')
    await message.edit(content='..................---------')
    await message.edit(content='...................--------')
    await message.edit(content='....................-------')
    await message.edit(content='.....................------')
    await message.edit(content='......................-----')
    await message.edit(content='.......................----')
    await message.edit(content='........................---')
    await message.edit(content='.........................--')
    await message.edit(content='..........................-')
    await message.edit(content='...........................')
    await message.edit(content=f'{args}')



@client.command()
async def history(ctx, limit: int = 99999999999):
	await ctx.message.delete()
	channel = ctx.message.channel
	messages = await ctx.channel.history(limit=limit).flatten()
	await ctx.send(
	    "please wait, the amount of time it takes depends on how many messages there are on the server."
	)

	with open(f"{channel}_messages.txt", "a+", encoding="utf-8") as f:
		print(f"\nhistory Saved by - {ctx.author.display_name}.\n\n", file=f)
		for message in messages:
			embed = ""
			if len(message.embeds) != 0:
				embed = message.embeds[0].description
				print(f"{message.author.name} - {embed}", file=f)
			print(f"{message.author.name} - {message.content}", file=f)
	await ctx.send(f"message history has been converted into a .txt file!")
	history = discord.File(fp=f'{channel}_messages.txt', filename=None)
	await ctx.send(file=history)



@client.command(aliases=["co"])
async def cow(ctx):
        await ctx.send("""```
 __________
 |        |
 |  Moo   |
 |        |
 ¯¯¯¯¯¯¯¯¯¯
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
```""")
        await ctx.message.delete()


@client.command()
async def lpew(ctx):
        """pew pew ----------<(' - '   )"""
        await ctx.message.edit(content="pew pew ----------<(' - '   )")



@client.command()
async def warning(ctx):
        list = (
            "`LOAD !! WARNING !! SYSTEM OVER`",
            "`OAD !! WARNING !! SYSTEM OVERL`",
            "`AD !! WARNING !! SYSTEM OVERLO`",
            "`D !! WARNING !! SYSTEM OVERLOA`",
            "`! WARNING !! SYSTEM OVERLOAD !`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`ARNING !! SYSTEM OVERLOAD !! W`",
            "`RNING !! SYSTEM OVERLOAD !! WA`",
            "`NING !! SYSTEM OVERLOAD !! WAR`",
            "`ING !! SYSTEM OVERLOAD !! WARN`",
            "`NG !! SYSTEM OVERLOAD !! WARNI`",
            "`G !! SYSTEM OVERLOAD !! WARNIN`",
            "`!! SYSTEM OVERLOAD !! WARNING`",
            "`! SYSTEM OVERLOAD !! WARNING !`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.5 SEC!`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`IMMINENT SHUT-DOWN IN 0.2 SEC!`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.01 SEC!`",
            "`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`",
            "`CTRL + R FOR MANUAL OVERRIDE..`",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)







@client.command(aliases=['proxy'])
async def proxies(ctx): # b'\xfc'
    await ctx.message.delete()
    file = open("Data/Http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")


keep_alive()


TOKEN = os.environ.get("DISCORD_BOT_SECRET")



client.run(TOKEN, bot=False)