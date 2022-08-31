import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("dayv4LjdoptP0eM0ksh40N4RjWdOkfgeMK/MNnnYjkL9927vlM8l2eNTH97VqCrC6nhI31H1vGNdMYVNqAIuPG72hu77CPKMEV7C9qUeRZoOM20NIjEfmWMQqfwxVpbHbaoe0G3/T1vOOG4YlQs2zAdB04t89/1O/w1cDnyilFU="))
handler = WebhookHandler(os.environ.get("6310bad2fbfd0dced29ff5e821502bbf"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
