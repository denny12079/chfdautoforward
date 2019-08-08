import json

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, JoinEvent, LeaveEvent, TextMessage, TextSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('fvn8HoTvQ2R+EZZDFaA5+ldyNirnvjYpNvHqwUWT1Bgr7iQPVPtQ3bzN/UxnX4+jfmuPPJodUUdKdPl2ia+s8EO+RoP8sa9SmUh5mGIlYcow4V/evtEaUSRwR+Xa5DlrGqNwnn1SPtys/LAwhpNs1AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('11292826d4f9b5fb7d76696eb836e2de')

# 監聽所有來自 /callback 的 Post Request
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

@handler.add(JoinEvent)
def handle_join(event):
    newcoming_text = "謝謝邀請我這個機器來至此群組！！我會盡力為大家服務的～"
    line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=newcoming_text)


if __name__ == "__main__":
    app.run()
