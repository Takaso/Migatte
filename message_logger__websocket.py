import websocket
import json
import threading
import time
from colors import black, blue, red, green, yellow, cyan, reset, magenta, white
import sys

with open("config.json", "r") as jsonfile:
    ConfigData = json.load(jsonfile)

token = ConfigData["YOURTOKEN"]


def send_json_request(ws, request):
    ws.send(json.dumps(request))

def recieve_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def heartbeat(interval, ws):
    print("[%s+%s] %sHeartbeat begin%s" % (green(), reset(), green(), reset()))
    while True:
        time.sleep(interval)
        heartbeatJSON = {
            "op": 1,
            "d": "null"
        }
        send_json_request(ws, heartbeatJSON)
        print("[%s+%s] %sHeartbeat sent!%s" % (green(), reset(), green(), reset()))

def messagelogger():
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
    event = recieve_json_response(ws)
    
    heartbeat_interval = event['d']['heartbeat_interval'] / 1000
    threading._start_new_thread(heartbeat, (heartbeat_interval, ws))
    payload = {
        'op': 2,
        "d": {
            "token": token,
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
            print(f"\nGuild ID: {event['d']['guild_id']}, Channel ID: {event['d']['channel_id']}, {event['d']['author']['username']}: {event['d']['content']}")
            op_code = event('op')
            if op_code == 11:
                print("\nHeartbeat received")
        except:
            pass

messagelogger()

