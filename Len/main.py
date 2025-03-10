from pyrogram import Client ,filters
import os
import ctypes
import string as strr
from datetime import datetime
import PIL.ImageGrab
import random
import pyautogui

start_time = datetime.now()

api_id = '21662197'
api_hash = '8c812ac7e5521ec4e9f3777521ebd8bb'
bot_token='6045644127:AAGHko3p88Hh5mo7sXxGv8JT1a4UHX53Omk'
bot = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

accessUsers = [511407184]

@bot.on_message(filters.command("off"))
def help_command(client, message):
    if message.chat.id in accessUsers:
        message.reply_text("Выключаю кампутор")
        os.system("shutdown /s /t 0")

@bot.on_message(filters.command("attention"))
def help_command(client, message):
    if message.chat.id in accessUsers:
        message.reply_text("Предупреждение отправлено")
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, message.text.replace("/attention", ""), 'АХТУНГ!', 0)

@bot.on_message(filters.command("time"))
def help_command(client, message):
    if message.chat.id in accessUsers:
        message.reply_text("Время работы пк: %s"%(datetime.now()-start_time))

@bot.on_message(filters.command("screenshot"))
def help_command(client, message):
    if message.chat.id in accessUsers:
        img = PIL.ImageGrab.grab(all_screens=True)
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        chars1 = "1234564890"
        gen1 = random.choice(chars)
        gen2 = random.choice(chars)
        gen3 = random.choice(chars1)
        gen4 = random.choice(chars)
        gen5 = random.choice(chars)
        gen6 = random.choice(chars)
        gen7 = random.choice(chars1)
        gen8 = random.choice(chars)
        gen9 = random.choice(chars)
        gen10 = random.choice(chars1)
        word = f"{message.from_user.id}-MOE{gen1}{gen2}{gen3}{gen4}{gen5}{gen6}{gen7}{gen8}{gen9}{gen10}"
        img.save(f'{word}.png')
        message.reply_document(
            document=f"{word}.png",
            caption = f'ваш скрин'
        )
        os.remove(f"{word}.png")

# @bot.on_message(filters.command("dance"))
# def help_command(client, message):
#     if message.chat.id in accessUsers:
#         message.reply_text("Пошел танец")
#         for i in range(int(message.text.replace("/dance", ""))):
#             pyautogui.moveRel(random.randint(-1000, 1000),random.randint(-1000, 1000))

bot.run()