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

line_bot_api = LineBotApi('fvn8HoTvQ2R+EZZDFaA5+ldyNirnvjYpNvHqwUWT1Bgr7iQPVPtQ3bzN/UxnX4+jfmuPPJodUUdKdPl2ia+s8EO+RoP8sa9SmUh5mGIlYcow4V/evtEaUSRwR+Xa5DlrGqNwnn1SPtys/LAwhpNs1AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('11292826d4f9b5fb7d76696eb836e2de')

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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))http://localhost:5000/edit/Documents/GitHub/chfdautoforward/app.py#
 


if __name__ == "__main__":
    app.run()