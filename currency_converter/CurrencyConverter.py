import google_currency
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
stip=0
From=""
to=""
ccc={}
def buttons():
        keyboard_buttons = []
        for key,value in google_currency.CODES.items():
            keyboard_buttons.append([KeyboardButton(text=value)])
            ccc[value]=key
        return ReplyKeyboardMarkup(keyboard=keyboard_buttons, one_time_keyboard=True)
def message(msg):
    try:
        global stip,From,to
        content_type,chat_type,chat_id=telepot.glance(msg)
        if content_type == 'text':
            if msg["text"]=="/start":
                bot.sendMessage(chat_id, f"Welcome {msg['from']['first_name']} to this bot. This bot allows you to  convert currencies . Please select from currency ", reply_markup=buttons())
                stip=0
            else:
                if stip==0:
                    try:
                        re=ccc.get(msg["text"])
                        From=re
                        stip=1
                        bot.sendMessage(chat_id,"now send currency to", reply_markup=buttons())
                    except:
                        bot.sendMessage(chat_id,"error")
                elif stip==1:
                    try:
                        re=ccc.get(msg["text"])
                        to=re
                        stip=2
                        bot.sendMessage(chat_id,"now send  converting value", reply_markup=None)
                    except:
                        bot.sendMessage(chat_id,"error")
                elif stip==2:
                    try:
                        result=google_currency.convert(From,to,int(msg["text"]))
                        stip=0
                        bot.sendMessage(chat_id,"result=" + str(result))   
                        bot.sendMessage(chat_id, f"Welcome {msg['from']['first_name']} to this bot. This bot allows you to  convert currencies . Please select from currency ", reply_markup=buttons())
                    except:
                        result="error"
                        bot.sendMessage(chat_id,"result=" + str(result))   
        else:
            bot.sendMessage(chat_id,"please send text messages only")
    except:
        pass

bot=telepot.Bot("6846519705:AAEaHGxLjtt_MpiTHHvIQv1xa53txCYi0WM")
bot.deleteWebhook()
MessageLoop(bot,{"chat":message}).run_as_thread()
print("runing")
while True:
    pass