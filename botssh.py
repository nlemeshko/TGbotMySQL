from tokens import *

from datetime import datetime
from subprocess import Popen, PIPE, STDOUT
import operator
import collections
from telebot import types
import time
import telepot



poll = 300  # секунд
shellexecution = []
setpolling = []
stopmarkup = {'keyboard': [['MetaProd to Production'],['Stop']]}

hide_keyboard = {'hide_keyboard': True}

def clearall(chat_id):
    if chat_id in shellexecution:
        shellexecution.remove(chat_id)



class RPI3Bot(telepot.Bot):
    def __init__(self, *args, **kwargs):
        super(RPI3Bot, self).__init__(*args, **kwargs)
        self._answerer = telepot.helper.Answerer(self)
        self._message_with_inline_keyboard = None

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        print("Your chat_id:" + str(chat_id))
        if chat_id in adminchatid:
            if content_type == 'text':
                if msg['text'] == '/start' and chat_id not in shellexecution:
                    bot.sendMessage(chat_id, "Hello! Welcome to GNS ImportExport DB. Type /gns to start" )


                    now = datetime.now()

                    #bot.sendMessage(chat_id, disable_web_page_preview=True)
                elif msg['text'] == "Stop":
                    clearall(chat_id)
                    bot.sendMessage(chat_id, "All operations are stoped.", reply_markup=hide_keyboard)

                elif msg['text'] == "MetaProd to Production":
                    bot.sendChatAction(chat_id, 'typing')
                    p = Popen("bash metatoprod.sh", shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
                    bot.sendMessage(chat_id, "Export from MetaProduction to Production starting. Wait Bot answer..." )
                    output = p.stdout.read()
                    if output != b'':
                        bot.sendMessage(chat_id, output, disable_web_page_preview=True)
                    else:
                        bot.sendMessage(chat_id, "ERROR! Send message to @kelahselai", disable_web_page_preview=True)

            )


                elif msg['text'] == "/gns" and chat_id not in shellexecution:
                    bot.sendMessage(chat_id, "Good. Choose your transfer",  reply_markup=stopmarkup)
                    shellexecution.append(chat_id)

                elif chat_id in shellexecution:
                    bot.sendChatAction(chat_id, 'typing')
                    bot.sendMessage(chat_id, "Может не будешь строчить, а выберешь уже какой ты хочешь бекап? Не? Бесишь..." )


TOKEN = telegrambot

bot = RPI3Bot(TOKEN)
bot.message_loop()
tr = 0
xx = 0

while 1:
    if tr == poll:
        tr = 0
        timenow = datetime.now()

    time.sleep(10)
    tr += 10
