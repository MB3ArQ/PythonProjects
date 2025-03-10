import telebot
from telebot import types
from datetime import datetime
import os
import ctypes
import PIL.ImageGrab
import random
from win32com.shell import shell, shellcon

bot_token = "6045644127:AAGHko3p88Hh5mo7sXxGv8JT1a4UHX53Omk"
accessUsers = [511407184]
bot = telebot.TeleBot(bot_token)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Выключение компуктера")
item2 = types.KeyboardButton("Предупреждение!!!")
item3 = types.KeyboardButton("Время работы компуктера")
item4 = types.KeyboardButton("Скриншот")
markup.row(item1, item3)
markup.row(item2, item4)
start_time = datetime.now()
@bot.message_handler(commands=['start'])
def start_message(message):
    if message.chat.id in accessUsers:
        bot.send_message(message.chat.id, 'Привет')
        bot.send_message(message.chat.id, 'Выбери нужную операцию: ', reply_markup=markup)

def SendAttentionText(message):
    text = message.text
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, text, 'АХТУНГ!', 0x40000)
    bot.send_message(message.chat.id, 'Предупреждение получено')

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.chat.id in accessUsers:
        if message.text == 'Выключение компуктера':
            bot.send_message(message.chat.id, 'Выключаю кампутор')
            os.system("shutdown /s /t 0")            
        elif message.text == 'Предупреждение!!!':
            bot.send_message(message.chat.id, 'Введите текст предупреждения: ')
            bot.register_next_step_handler(message, SendAttentionText)
        elif message.text == 'Время работы компуктера':
            bot.send_message(message.chat.id, 'Время работы ПК: %s'% (datetime.now() - start_time))        
        elif message.text == 'Скриншот':
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
            bot.send_photo(message.chat.id, img)
            os.remove(f"{word}.png")        

@bot.message_handler(content_types=['document', 'video', 'audio', 'voice', 'video_note'])
def get_broadcast_file(message):
    type_name = ""
    if message.content_type == 'document':
        f = bot.get_file(message.document.file_id)
        type_name = "Документ"
    if message.content_type == 'video':
        f = bot.get_file(message.video.file_id)
        type_name = "Видео"
    if message.content_type == 'audio':       
        f = bot.get_file(message.audio.file_id)
        type_name = "Аудио"
    if message.content_type == 'voice':
        f = bot.get_file(message.voice.file_id)        
        type_name = "Голосовое сообщение"
    if message.content_type == 'video_note':
        f = bot.get_file(message.video_note.file_id)        
        type_name = "Видео-кружок"
    file_path = f.file_path
    if file_path != '':                  
        msg = bot.send_message(message.chat.id, "Выполняется отправка файла...")        
        file = bot.download_file(file_path)              
        send_path = shell.SHGetKnownFolderPath(shellcon.FOLDERID_Documents) + "/Свалка"
        os.makedirs(send_path, 0o774, True)
        if os.path.isdir(send_path):            
            send_path += "/" + os.path.basename(file_path)
            with open(send_path, "wb") as new_file:
                new_file.write(file)
            bot.delete_message(message.chat.id, msg.message_id)
            bot.reply_to(message, type_name + " отправлен на компьютер")
bot.infinity_polling()