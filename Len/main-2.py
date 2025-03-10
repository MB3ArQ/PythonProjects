import telebot
from telebot import types
from datetime import datetime
import os
import ctypes
import PIL.ImageGrab
import random
from win32com.shell import shell, shellcon
import requests
from dotenv import load_dotenv, dotenv_values
from lxml import html

bot_token = "7603107118:AAGCOCXECxkInOLrDg_qmj_8G4SDuCn6OFU"
accessUsers = [836831213]
bot = telebot.TeleBot(bot_token)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Выключение компуктера")
item2 = types.KeyboardButton("Предупреждение!!!")
item3 = types.KeyboardButton("Время работы компуктера")
item4 = types.KeyboardButton("Скриншот")
item5 = types.KeyboardButton("Документация по CSS")
markup.row(item1, item3)
markup.row(item2, item4)
markup.row(item5)


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

def MWDCSSReferenceModulesParser(message):
    sections_names = [
    'reference', 
    'properties', 
    'at-rules_and_descriptors', 
    'functions',
    'data_types_and_values', 
    'html_attributes', 
    'interfaces', 
    'related_concepts'
    ]
    h2_sections_names = [
        'reference',
        'related_concepts'
    ]
    main_page_content = 'article[@class="main-page-content"]'

    load_dotenv()

    rt = requests.get("https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_anchor_positioning", headers={os.getenv("HEADERS_PROPERTY"): os.getenv("HEADERS_VALUE")})
    tree = html.fromstring(rt.content)

    main_sections = []
    for i in sections_names:
        head_elem = ""
        if i in h2_sections_names:
            head_elem = "h2"
        else:
            head_elem = "h3"
        main_sections.append("".join(tree.xpath(f'//{main_page_content}/section[@aria-labelledby="{i}"]/{head_elem}/a/text()')))
    if len(main_sections) > 0:
        markup1 = types.ReplyKeyboardMarkup(row_width=5)        
        row = [types.KeyboardButton(x) for x in main_sections]
        markup1.add(*row)
        msg = bot.send_message(message.chat.id, "Выберите раздел статьи: ", reply_markup=markup1)
        # bot.register_next_step_handler(message, bot.delete_message(message.chat.id, msg.message_id))            

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
        elif message.text == 'Документация по CSS':
            MWDCSSReferenceModulesParser(message)

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