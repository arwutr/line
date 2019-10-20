import os
from flask import Flask, request, abort, jsonify
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['Dz9v90U5WxPHGplIxCX+os1ChKg6i7gAJxBC7Z/YL0SW+ZDV1dHRpskr6vUflgcjrnyK2v8lIvP7rBrdAHdDRKVF3PO+jAso06oSS0S/7pJrUKWRlOTyCcHs5oszpYCuiuJQKIFu9a46rbMOEMyS2AdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['fcd982271308e19a09ffcac084277bad'])

@app.route("/")
def index():
    return "Hello World สวัสดีชาวโลก"

@app.route("/callback", methods=['POST'])
def callback():
#    return "ok"
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
#        TextSendMessage(text=event.message.text)
        TextSendMessage(text="สบายดีไหม")
    )


if __name__ == "__main__":
    app.run()
