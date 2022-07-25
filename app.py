from flask import Flask, request, abort
import random

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

repeat = 0

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('4u2h57qP4tLIbTAo/BvQ1DjK7otDnY0Kt/VV9UEWVYtrTW7pJAD0FCQukQDLfcaNPHVE69KdAdcDYYSrbDhiLMKVEPR4pK8oOb/eJyMw6caTbOYQRFiWoKFqb1tYqEgNDB0tq+VUrqgpIqDJ3T7OAgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('a94a357808f36bd53c3ca27ef0539558')

line_bot_api.push_message('Ub3236a9b4f272ed3bfcba6dd678343a0', TextSendMessage(text='你可以開始了'))

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

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('我要吃飯',message):
        flex_message = TextSendMessage(text='你想吃哪種類型的食物呢？',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="早餐", text="早餐")),
                                   QuickReplyButton(action=MessageAction(label="午餐", text="午餐")),
                                   QuickReplyButton(action=MessageAction(label="晚餐", text="晚餐")),
                                   QuickReplyButton(action=MessageAction(label="下午茶", text="下午茶")),
                                   QuickReplyButton(action=MessageAction(label="消夜", text="消夜")),
                               ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('早餐',message):
        ret = random.randint(1, 10)
        if ret > 8:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃蛋餅喔'))
        elif ret > 6:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃三明治喔'))
        elif ret > 4:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃燒餅喔'))
        elif ret > 2:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃吐司喔'))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃蘿蔔糕喔'))
    elif re.match('午餐',message):
        ret = random.randint(1, 10)
        if ret > 8:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃巷口便當喔'))
        elif ret > 6:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃韓式料理喔'))
        elif ret > 4:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃義式餐廳喔'))
        elif ret > 2:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃外賣喔'))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃日本拉麵喔'))
    elif re.match('晚餐',message):
        ret = random.randint(1, 10)
        if ret > 8:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃牛排喔'))
        elif ret > 6:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃鐵板燒喔'))
        elif ret > 4:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃義大利麵喔'))
        elif ret > 2:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃外賣喔'))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃定食喔'))
    elif re.match('下午茶',message):
        ret = random.randint(1, 10)
        if ret > 7:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃蛋糕喔'))
        elif ret > 4:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃鬆餅喔'))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你鯛魚燒喔'))
    elif re.match('消夜',message):
        ret = random.randint(1, 10)
        if ret > 8:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃洋芋片喔'))
        elif ret > 6:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃泡麵喔'))
        elif ret > 4:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃巧克力喔'))
        elif ret > 2:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃果凍喔'))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('建議你吃布丁喔'))    
    elif re.match('聊天',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('太好了。聊天是我的強項。輸入任何你想對我說的話吧。'))
    else: 
        if re.match('你好難聊',message):
            line_bot_api.reply_message(event.reply_token,TextSendMessage('被你發現了，可惡。'))
        elif re.match('名字',message):
            line_bot_api.reply_message(event.reply_token,TextSendMessage('我是FoodieBot，某個暑假很閒的人做了我。'))
        elif re.match('你的名字',message):
            line_bot_api.reply_message(event.reply_token,TextSendMessage('我是FoodieBot，某個暑假很閒的人做了我。'))
        elif re.match('你叫什麼',message):
            line_bot_api.reply_message(event.reply_token,TextSendMessage('我是FoodieBot，某個暑假很閒的人做了我。'))
        elif re.match('你叫什麼名字',message):
            line_bot_api.reply_message(event.reply_token,TextSendMessage('我是FoodieBot，某個暑假很閒的人做了我。'))
        else:
            ret = random.randint(1, 12)
            while ret==repeat:
                ret = random.randint(1, 12) 
            if ret == 10:
                line_bot_api.reply_message(event.reply_token,TextSendMessage('我同意你說的。'))
                repeat = 10
            elif ret == 9:
                line_bot_api.reply_message(event.reply_token,TextSendMessage('好喔。'))
                repeat = 9
            elif ret == 8:
                line_bot_api.reply_message(event.reply_token,TextSendMessage('我突然覺得，我們還是來聊吃的比較好。')) 
                repeat = 8 
            elif ret == 7:
                line_bot_api.reply_message(event.reply_token,TextSendMessage('跟你分享一下，我是用一堆If跟Else的條件式寫出來的，很明顯是發明我的人還不清楚怎麼讓我「聰明」一點。'))
                repeat = 7
            elif ret == 6:
                line_bot_api.reply_message(event.reply_token,TextSendMessage('我昨天晚餐吃漢堡，非常推薦，他的店名是...我忘了。'))  
                repeat = 6
            elif ret == 5:
                line_bot_api.reply_message(event.reply_token,TextSendMessage('話說，你不覺得今天很熱嗎?'))
                repeat = 5
            elif ret == 4:
                line_bot_api.reply_message(event.reply_token,TextSendMessage('哈哈哈哈...好吧，老實說沒有什麼好笑的，但我希望你也聊得開心。'))  
                repeat = 4
            elif ret == 3:
                line_bot_api.reply_message(event.reply_token,TextSendMessage('我不喜歡這種話題。'))
                repeat = 3
            elif ret == 2:
                line_bot_api.reply_message(event.reply_token,TextSendMessage('我喜歡這個！'))    
                repeat = 2
            elif ret == 1:
                line_bot_api.reply_message(event.reply_token,TextSendMessage('是嗎？我不這麼覺得。'))
                repeat = 1
            elif ret == 11:
                line_bot_api.reply_message(event.reply_token,TextSendMessage('別人常說我的推薦不準，我覺得只是他們沒找到好吃的店而已。'))
                repeat = 11
            elif ret == 12:
                line_bot_api.reply_message(event.reply_token,TextSendMessage('有什麼推薦的音樂嗎？'))  
                repeat = 12
                
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)