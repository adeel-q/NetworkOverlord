#server that connects to a web based console and dispatches commands to clientBots

from flask import Flask
from flask import request, jsonify, url_for


#TODO: use nginx for effciency for serving static pages, but we can get away with it for now

app = Flask(__name__, static_url_path = '/static')

'''
windows config:

set FLASK_APP=overlord.py
set FLASK_DEBUG=1
python -m flask run
'''


#sample bots with properties
#shoud be in a db
#TODO: setup mysql, or similar
bots = [
    {
        "botAlias":"botty",
        "botId": 1,
        "botTaskQueue": [],
        "botStatus": "offline",
        "lastCmdStatus": {
            "cmd": "dir",
            "status": "failure",
            "echoCmd": ""
        },
        "botIp": '192.168.1.1'
    },
    {
        "botAlias":"shotty",
        "botId": 2,
        "botTaskQueue": [],
        "botStatus": "offline",
        "lastCmdStatus": {
            "cmd": "dir",
            "status": "success",
            "echoCmd": ""            
        },
        "botIp": '192.168.1.2'
    }
]
@app.route('/')
def index():
    return 'Root page'
#end def

@app.route('/bots', methods=['GET', 'POST'])
def all_bots():
    #return all bots
    if request.method == 'GET':
        return jsonify(results = bots)
    
    #register a new bot, should only accessible by client software.
    #client should log the bot independantly into the server...
    if request.method == 'POST':
        new_bot = request.get_json()
        for target_bot in bots:
            if target_bot['botAlias'] == new_bot['botAlias']or target_bot['botIp'] == new_bot['botIp']:
                return 'failed to add a new bot, dupilicate maybe...'
        #end for
        
        #add to db here
        bots.append(new_bot)
        return jsonify(new_bot)
    else:
        return 'F outta here dummy, you can only GET or POST here!'
#end def
        
@app.route('/bot/<int:bot_id>', methods=['GET', 'POST'])
def bot_byid(bot_id):
    if request.method == 'GET':
        for target_bot in bots:
            if target_bot['botId'] == bot_id:
                return jsonify(results = target_bot)
            #end if
        #end for
        return 'bot not found, handle json return obj'
    #end if
#end def

