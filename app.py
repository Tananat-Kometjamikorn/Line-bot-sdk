from flask import Flask, request
import requests
import json
from config import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET

app = Flask(__name__)


@app.route('/')
def home():
    return "HOME", 200


@app.route("/webhook", methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        print(message)
        # Reply_message = message
        # ReplyMessage(Reply_token,Reply_message,CHANNEL_ACCESS_TOKEN)
        return 'OK', 200
    elif request.method == 'GET':
        return 'OK', 201


def ReplyMessage(Reply_token, TextMessage, Line_Access_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Access_Token)  ##ที่ยาวๆ
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken": Reply_token,
        "messages": [{
            "type": "text",
            "text": TextMessage
        }]
    }
    data = json.dumps(data)  ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200
