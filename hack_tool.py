import asyncio
from email import header
import os
from wsgiref import headers
from colors import black, blue, red, green, yellow, cyan, reset, magenta, white
import requests
import aiohttp
import threading
from faker import Faker
import proxygen
from itertools import cycle
import time

proxies = proxygen.get_proxies()
proxy_pool = cycle(proxies)

def generateIP():
    faker = Faker()
    ip_addr = faker.ipv4()
    print(f"\nIPv4 Address generated: {ip_addr}")  

def call(headers, victima, chanelid, autodisconnect):
    global raid
    raid = True
    try:
        json = {
            "recipients": [victima]
            }
        while raid:
            try:
                r = requests.post(f"https://discord.com/api/v9/channels/{chanelid}/call/ring",  headers=headers, json=json, proxies={"http": next(proxy_pool)})
                if autodisconnect in ["yes", "Yes", "y"]:
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
                elif r.status_code == 429:
                    a = r.json(); time.sleep(a['retry_after'])

                else:
                    print("\n%s[-] Failed to ring user%s" & (red(), reset()))
            except Exception as a:
                print(a)
    finally:
        print("\n[%s+%s] Done %sspam calling%s" % (green(), reset(), yellow(), reset()))



def menu_startup():
    print("""
%s                                            
      .--.--.     ,--,                                            
     /  /    '. ,--.'|                                            
    |  :  /`. / |  | :                                    __  ,-. 
    ;  |  |--`  :  : '                                  ,' ,'/ /| 
    |  :  ;_    |  ' |     ,--.--.        .--,   ,---.  '  | |' | 
     \  \    `. '  | |    /       \     /_ ./|  /     \ |  |   ,' 
      `----.   \|  | :   .--.  .-. | , ' , ' : /    /  |'  :  /   
     _  _ \  \  |'  : |__  \__\/: . ./___/ \: |.    ' / ||  | '    
     /  /`--'  /|  | '.'| ," .--.; | .  \  ' |'   ;   /|;  : |    
    '--'.     / ;  :    ;/  /  ,.  |  \  ;   :'   |  / ||  , ;    
      `--'---'  |  ,   /;  :   .'   \  \  \  ;|   :    | ---'     
                 ---`-' |  ,     .-./   :  \  \\   \  /           
                         `--`---'        \  ' ; `----'            
                                          `--` 
    ***************************************************************
    *                                                             *
    *     Made by Takaso, Github: https://github.com/Takaso       *
    *                                                             *
    ***************************************************************

[+] Write in the command line 'slayer help' for the command list.
%s
""" % (green(), reset()))
   

def shell():
    command_line= input("\n%s@slayer%s:%s~%s$ " % (green(), reset(), blue(), reset()))
    if command_line == "slayer help":
        print("""
[0] - help (No desc)
[1] - slayer start (No desc)
[2] - slayer gen (Generates a valid IP)
[3] - nslookup (IP Address)
[4] - call (No desc)
""")
    elif command_line == "slayer start":
        print("\nStarted!")
    elif command_line == "slayer gen":
        generateIP()
    elif command_line == "call":
        headers = {
            "Authorization": str(input("Insert your token > "))
        }
        call(headers, input("Victim ID > "), input("Channel ID > "), input("Oscuro? > "))
    else:
        os.system(command_line)

menu_startup()
while True:
    shell()