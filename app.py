from flask import Flask, request, abort

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


line_bot_api = LineBotApi('7JE3pGMiIfd+4AZG6F5W3PpgoJN6dva9P6QmSDhOQzWihOpJewnWATyDXFTXmgu18rt5gitPUoJCIqDuI5q3i3k/ZQU8FHSn6k4VPb9jiCUWaD9kK8kX/PpXIrMeUSzaU+HRKtzNLP30/VEY7nq48wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('68dc868eae939e9217866111b43c30f9')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user id when reply
    user_id = event.source.user_id
    print("user_id =", user_id)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

@app.route('/')
def homepage():
    return 'Hello, World!'

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
