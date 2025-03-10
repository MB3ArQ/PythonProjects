import telebot
import json
import os
import sys
import flag
import matplotlib.pyplot as plt
import io
import time
from telebot import types
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

bot = telebot.TeleBot(token=os.getenv('TG_BOT_TOKEN'))
accessUsers = [int(x) for x in os.getenv('ACCESS_USERS').split(",")]

currencies = [
    {"country_image": flag.flag("RU"), "name": "RUB"},
    {"country_image": flag.flag("US"), "name": "USD"},    
    {"country_image": flag.flag("EU"), "name": "EUR"},
    {"country_image": flag.flag("CN"), "name": "CNH"},
    {"country_image": flag.flag("JP"), "name": "JPY"}
]

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('💸Добавить данные в учет')
item2 = types.KeyboardButton('🗃️Получить всю информацию учета')
item3 = types.KeyboardButton('📊График соотношения доходов и расходов')
item4 = types.KeyboardButton('📚Советы по экономии')
markup.row(item1, item2)
markup.row(item3, item4)

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item11 = types.KeyboardButton('🔺Доход')
item12 = types.KeyboardButton('🔻Расход')
markup1.row(item11, item12)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
row = [types.KeyboardButton(x['country_image'] + x['name']) for x in currencies]
markup2.add(*row)

markup_return_to_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
item21 = types.KeyboardButton('⬅️Вернуться в меню')
markup_return_to_menu.add(item21)

FOLDER_PATH = os.path.dirname(os.path.abspath(sys.argv[0])).replace("\\", "/")
JSON_FILE = FOLDER_PATH + "/" + os.getenv('JSON_FILE')
JSON_TMP_FILE = FOLDER_PATH + "/" + os.getenv('JSON_TMP_FILE')

global new_data

def ExistanceTemporaryData() -> bool:
    exist_tmp_data = ReadJSONData(JSON_TMP_FILE)
    return exist_tmp_data != {}

def RefreshBot(message):
    if ExistanceTemporaryData():
        WriteJSONData(JSONFileName=JSON_TMP_FILE, data={})                 
    new_data = {}
    new_data['user_id'] = message.chat.id
    WriteJSONData(JSONFileName=JSON_TMP_FILE, data=new_data)
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)

def ReadJSONData(JSONFileName: str) -> list:
    try:    
        with open(JSONFileName, "r", encoding="utf-8") as file:
            exist_data = json.load(file)        
    except FileNotFoundError:
        if JSONFileName == JSON_TMP_FILE:
            exist_data = {}
        else:
            exist_data = []
    return exist_data

def WriteJSONData(JSONFileName: str, data: list):
    with open(JSONFileName, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def ResumeAddNewData(message) -> dict:
    if not ExistanceTemporaryData():
        RefreshBot(message)
        return {}
    return ReadJSONData(JSON_TMP_FILE)

def GetMessageAfterOperation(message, NewData: dict):
    return f'✅Готово\nВы добавили информацию по вашим {"доходам" if NewData["operation"] == item11.text else "расходам"}'

def ChooseOperationData(message):    
    bot.send_message(message.chat.id, 'Выберите операцию', reply_markup=markup1)

def IsConvertToFloat(text: str) -> bool:
    try:
        float(text)
        return True
    except ValueError:
        return False
        
def InsertAmount(message):
    if IsConvertToFloat(message.text):        
        new_data = ResumeAddNewData(message=message)
        new_data['amount'] = float(message.text)
        WriteJSONData(JSONFileName=JSON_TMP_FILE, data=new_data)
        bot.send_message(message.chat.id, 'Выберите валюту:', reply_markup=markup2)
    else:
        bot.send_message(message.chat.id, 'Не получилось записать сумму операции')
        RefreshBot(message)

def AddOperationData(message):
    new_data = ResumeAddNewData(message=message)
    exist_data = ReadJSONData(JSON_FILE)
    new_count = len(exist_data) + 1
    new_data['id'] = new_count
    new_data['operation'] = message.text
    WriteJSONData(JSONFileName=JSON_TMP_FILE, data=new_data)
    bot.send_message(message.chat.id, 'Введите сумму:')
    bot.register_next_step_handler(message, InsertAmount)        

def getCurrentDate() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
def AddCurrencyData(message):    
    new_data = ResumeAddNewData(message=message)    
    if not (new_data['id'] or new_data['operation'] or new_data['amount']):
        RefreshBot(message=message)
        exit
    new_data['currency'] = message.text
    new_data['date'] = getCurrentDate()
    exist_data = ReadJSONData(JSON_FILE)
    exist_data.append(new_data)
    WriteJSONData(JSONFileName=JSON_FILE, data=exist_data)
    exist_data = ReadJSONData(JSON_FILE)
    new_message = GetMessageAfterOperation(message=message, NewData=new_data)
    new_data = {}
    WriteJSONData(JSONFileName=JSON_TMP_FILE, data={})
    bot.send_message(message.chat.id, new_message, reply_markup=markup_return_to_menu) 

def GetUserOperationData(message: any, OperationTypeText: str, CommonData: list) -> list: 
    return [{'amount': item['amount'], 'currency': item['currency'], 'date': item['date']} for item in CommonData if item['user_id'] == message.chat.id and item['operation'] == OperationTypeText]

def GetUserOperationDataByCurrencies(UserOperationData: list) -> str:
    """Получение всех данных по действиям пользователя по каждой валюте в рамках конкретной операции
    Args:
        UserOperationData (list): Тип операции
    Returns:
        str: Полученные данные в виде строки
    """
    currencies_data = []
    mes_txt = ""
    for item in currencies:
        item_list = [x['amount'] for x in UserOperationData if x['currency'] == item['country_image'] + item['name']]
        if item_list:
            item_sum = sum(item_list)
            currencies_data.append({'amount': item_sum, 'currency': item['country_image'] + item['name']})
    for item in currencies_data:
        mes_txt += f"\n{item['currency']}: {item['amount']}"
    return mes_txt

def IsExistUserInAllData(message: any, Data: list) -> bool:
    for item in Data:
        if item['user_id'] == message.chat.id:
            return True
    return False

def NotFoundData(message):
    bot.send_message(message.chat.id, '❌Информации по доходам и расходам не найдено')
    
def UserValidation(message) -> list:
    data = ReadJSONData(JSON_FILE)
    exist_user_data = False 
    if data != []:
       exist_user_data = IsExistUserInAllData(message=message, Data=data)
    if data == [] and not exist_user_data:
        NotFoundData()
        return None
    return data

def GetAllUserData(message):    
    data = UserValidation(message=message)
    if data:
        message_text = ""
        user_income = GetUserOperationData(message=message, OperationTypeText=item11.text, CommonData=data)    
        user_expense = GetUserOperationData(message=message, OperationTypeText=item12.text, CommonData=data)
        if user_income:
            message_text += item11.text + ":"
            message_text += GetUserOperationDataByCurrencies(UserOperationData=user_income)        
        if user_expense:
            message_text += "".join("\n\n" if user_income else "") + item12.text + ":"
            message_text += GetUserOperationDataByCurrencies(UserOperationData=user_expense)        
        bot.send_message(message.chat.id, message_text)

def CreateCurrencyDependencyGraph(data: list):    
    income_amounts = [item[1] for item in data[0]] if data[0] else []
    income_numbers = list(range(0, len(income_amounts)))
    expense_amounts = [item[1] for item in data[1]] if data[1] else []    
    expense_numbers = list(range(0, len(expense_amounts)))
    if income_numbers and income_amounts:
        plt.plot(income_numbers, income_amounts, label='Доход', marker='o', color='green', mfc='black', mec='blue')
        for (xi, yi) in zip (income_numbers, income_amounts):
            plt.text(xi, yi, f'{round(yi, 1)}', fontsize=9, ha='right', va='bottom', color='black', bbox=dict(facecolor='#7BB661', alpha=0.95))            
    if expense_numbers and expense_amounts:
        plt.plot(expense_numbers, expense_amounts, label='Расход', marker='o', color='red', mfc='black', mec='blue')
        for (xi, yi) in zip (expense_numbers, expense_amounts):
            plt.text(xi, yi, f'{round(yi, 1)}', fontsize=9, ha='right', va='top', color='black', bbox=dict(facecolor='#CB4154', alpha=0.95))            
    plt.grid(True)
    plt.legend(loc='upper right', ncol=1, frameon=True)
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    buf.seek(0)
    plt.close()
    
    return buf        
    
def GetDependencyGraphs(message):
    data = UserValidation(message=message)
    if data:
        user_income = GetUserOperationData(message=message, OperationTypeText=item11.text, CommonData=data)    
        user_expense = GetUserOperationData(message=message, OperationTypeText=item12.text, CommonData=data)
        for item in currencies:
            currency_text = item['country_image'] + item['name']
            currency_income = [[x['date'], x['amount']] for x in user_income if x['currency'] == currency_text]
            currency_expense = [[x['date'], x['amount']] for x in user_expense if x['currency'] == currency_text]
            currency_text = item['name'] + item['country_image']            
            currency_graph = CreateCurrencyDependencyGraph(data=[currency_income, currency_expense])                
            bot.send_photo(message.chat.id, photo=currency_graph, caption=f'График зависимости доходов и расходов для {currency_text}')
            time.sleep(2)

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.chat.id in accessUsers:               
        bot.send_message(message.chat.id, 'Привет')
        RefreshBot(message=message)        

@bot.message_handler(content_types='text')
def text_message(message):
    if message.chat.id in accessUsers:
        if message.text == item1.text:                        
            ChooseOperationData(message=message)
        if message.text in [item11.text, item12.text]:
            AddOperationData(message=message)
        if message.text in [x['country_image'] + x['name'] for x in currencies]:
            AddCurrencyData(message=message)
        if message.text == item21.text:
            RefreshBot(message=message)
        if message.text == item2.text:
            GetAllUserData(message=message)           
        if message.text == item3.text:
            GetDependencyGraphs(message=message)

bot.infinity_polling()