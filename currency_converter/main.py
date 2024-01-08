import message,app,google_currency
import telegram
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import CommandHandler,MessageHandler,filters,ApplicationBuilder,CallbackQueryHandler
with open("token.bot","r",encoding="utf-8") as file:
    bot=ApplicationBuilder().token(file.read()).build()
stip=0
From=""
to=""
ccc={}
def buttons():
        keyboard_buttons = []
        for key,value in google_currency.CODES.items():
            keyboard_buttons.append([KeyboardButton(text=value)])
            ccc[value]=key
        return ReplyKeyboardMarkup(keyboard=keyboard_buttons,one_time_keyboard=True)

async def start(update,contextt):
    info=update.effective_user
    global stip
    stip=0
    keyboard=InlineKeyboardMarkup([[InlineKeyboardButton("donate",url="https://www.paypal.me/AMohammed231")],[InlineKeyboardButton("help",callback_data="help")]])
    await message.Sendmessage(chat_id=info.id,text="welcome " + str(info.first_name) + "to this bot. This bot allows you to  convert currencies . Please select from currency ",reply_markup=keyboard)
    await message.Sendmessage(info.id,"from",reply_markup=buttons())
async def helb(update,contextt):
    links="""<a href="https://t.me/mesteranasm">telegram</a>

<a href="https://t.me/tprogrammers">telegram channel</a>

<a href="https://x.com/mesteranasm">x</a>

<a href="https://Github.com/mesteranas">Github</a>

email:
anasformohammed@gmail.com

<a href="https://Github.com/mesteranas/currency_converter_telegrambot">visite project on Github</a>
"""
    info=update.effective_user
    await message.Sendmessage(info.id,"""name: {}\nversion: {}\ndescription: {}\n developer: {}\n contect us {}""".format(app.name,str(app.version),app.description,app.developer,links))
async def callBake(update,contextt):
    q=update.callback_query
    q.answer()
    if q.data=="help":
        await helb(update,contextt)
async def currency(update,contextt):
    info=update.effective_user
    global stip,From,to
    if stip==0:
        try:
            re=ccc.get(update.message.text)
            From=re
            stip=1
            await message.Sendmessage(info.id,"now send currency to", reply_markup=buttons())
        except:
            await message.Sendmessage(info.id,"error")
    elif stip==1:
        try:
            re=ccc.get(update.message.text)
            to=re
            stip=2
            await message.Sendmessage(info.id,"now send  converting value", reply_markup=None)
        except:
            await message.Sendmessage(info.id,"error")
    elif stip==2:
        try:
            result=google_currency.convert(From,to,int(update.message.text))
            stip=0
            await message.Sendmessage(info.id,"result=" + str(result))   
            await message.Sendmessage(info.id, f"Welcome {info.first_name} to this bot. This bot allows you to  convert currencies . Please select from currency ", reply_markup=buttons())
        except:
            await message.Sendmessage(info.id,"error")


print("running")
bot.add_handler(CommandHandler("start",start))
bot.add_handler(CommandHandler("help",helb))
bot.add_handler(CallbackQueryHandler(callBake))
bot.add_handler(MessageHandler(filters.TEXT,currency))
bot.run_polling()