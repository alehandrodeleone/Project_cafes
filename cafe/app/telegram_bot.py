import telebot
from telebot import types
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cafe.settings")
import django
django.setup()
from app.models import request_token,Restaurant,support_message,application_new_restaurant
from django.contrib.auth.models import User
from telegram import InputFile

# Создаем экземпляр бота, указывая токен вашего бота
bot = telebot.TeleBot("6581255900:AAHlSpSFWuHGcmcM-x3wrfrlNe3JL-8X0Kc")

@bot.message_handler(commands=['home'])
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет Админ! Тут ты сможешь получить информацию о ресторанах,запросы на получение токенов и вопросы пользователей")
    button = types.InlineKeyboardMarkup()
    button.add(types.InlineKeyboardButton("Информация о запросах Токена", callback_data="execute_request"))
    button.add(types.InlineKeyboardButton("Информация о пользователях", callback_data="request_user"))
    button.add(types.InlineKeyboardButton("Неопубликованные Заведения", callback_data="restaurant_topublishNone"))
    button.add(types.InlineKeyboardButton("Опубликованные Заведения", callback_data="restaurant_topublishTrue"))
    button.add(types.InlineKeyboardButton("Открытые вопросы пользователей", callback_data="open_questions"))
    button.add(types.InlineKeyboardButton("Заявления на регистрацию ресторана",callback_data="new_restaurant_application"))
    bot.send_message(message.chat.id, "Нажмите кнопку, чтобы выполнить запрос", reply_markup=button)


@bot.message_handler(commands=['RequestToken'])
def RequestToken(message):
    records = request_token.objects.all()
    for record in records:
        bot.send_message(message.chat.id, f"Запрос ТОКЕНА\n Пользователь:{record.request_token_user}\n Дата запроса: {record.date_request}")
    button_home = types.InlineKeyboardMarkup()
    button_delete_req = types.InlineKeyboardMarkup()
    button_delete_req.add(types.InlineKeyboardButton("Очистить Базу данных", callback_data="delete_all_request_token"))
    bot.send_message(message.chat.id, "Удалить все данные из БД", reply_markup=button_delete_req)
    button_home.add(types.InlineKeyboardButton("Домой", callback_data="Home"))
    bot.send_message(message.chat.id, "Нажмите кнопку, чтобы вернуться на главную", reply_markup=button_home)



def delete_request_token():
    request_token.objects.all().delete()


def RequestUser(message):
    Users = User.objects.all()
    for user in Users:
        bot.send_message(message.chat.id, f"Пользователь.\nЛогин:{user.username}\nИмя:{user.first_name}\nФамилия:{user.last_name}")
    button_home = types.InlineKeyboardMarkup()
    button_home.add(types.InlineKeyboardButton("Домой", callback_data="Home"))
    bot.send_message(message.chat.id, "Нажмите кнопку, чтобы вернуться на главную", reply_markup=button_home)
def requestPublishRestaurant(message):
    publishrestaurant=Restaurant.objects.filter(to_publish=True)
    for restaurant in publishrestaurant:
        bot.send_message(message.chat.id,f"Название:{restaurant.Name_restaurant}\nВладелец:{restaurant.owner_cafe}"
                                         f"\nEmail:{restaurant.email}\nНомер:{restaurant.phone}\nЗарегистрирован:{restaurant.datetime}")
    button_home = types.InlineKeyboardMarkup()
    button_home.add(types.InlineKeyboardButton("Домой", callback_data="Home"))
    bot.send_message(message.chat.id, "Нажмите кнопку, чтобы вернуться на главную", reply_markup=button_home)

def requestNonePublishRestaurant(message):
    NonePublishRestaurant=Restaurant.objects.filter(to_publish=False)
    for restaurant in NonePublishRestaurant:
        bot.send_message(message.chat.id,f"Название:{restaurant.Name_restaurant}\nВладелец:{restaurant.owner_cafe}"
                                         f"\nEmail:{restaurant.email}\nНомер:{restaurant.phone}\nЗарегистрирован:{restaurant.datetime}")
    button_home = types.InlineKeyboardMarkup()
    button_home.add(types.InlineKeyboardButton("Домой", callback_data="Home"))
    bot.send_message(message.chat.id, "Нажмите кнопку, чтобы вернуться на главную", reply_markup=button_home)

def question_user_info(message):
    question=support_message.objects.filter(answered=False)
    for question_user in question:

        bot.send_message(message.chat.id,f'Пользователь:{question_user.application_user}'
                                         f'\nСообщение:{question_user.message}\nДата обращения:{question_user.datetime}')

        button_home = types.InlineKeyboardMarkup()
        button_home.add(types.InlineKeyboardButton("Домой", callback_data="Home"))

        bot.send_message(message.chat.id, "Нажмите кнопку, чтобы вернуться на главную", reply_markup=button_home)
        
def show_application_new_restaurant(message):
    application=application_new_restaurant.objects.filter(publish=False)

    
    for a in application:

        bot.send_message(message.chat.id, f"Пользователь: {a.user}\nНазвание ресторана: {a.name_new_restaurant}"
                                          f"\nДата заявления: {a.datetime}")

        blank = open(a.blank.path, 'rb')
        bot.send_document(message.chat.id, blank, caption="Заявление")
        blank.close()

        document1_file = open(a.document1.path, 'rb')
        bot.send_document(message.chat.id, document1_file, caption="Документ 1")
        document1_file.close()

        document2_file = open(a.document2.path, 'rb')
        bot.send_document(message.chat.id, document2_file, caption="Документ 2")
        document2_file.close()

        document3_file = open(a.document3.path, 'rb')
        bot.send_document(message.chat.id, document3_file, caption="Документ 3")
        document3_file.close()

        bot.send_message(message.chat.id,"Это вся информация на данного пользователя")

        button_home = types.InlineKeyboardMarkup()
        button_home.add(types.InlineKeyboardButton("Домой", callback_data="Home"))
        bot.send_message(message.chat.id, "Нажмите кнопку, чтобы вернуться на главную", reply_markup=button_home)




@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'execute_request':
        RequestToken(call.message)
    if call.data == 'Home':
        start(call.message)
    if call.data == 'request_user':
        RequestUser(call.message)
    if call.data=='delete_all_request_token':
        delete_request_token()
    if call.data == 'restaurant_topublishNone':
        requestNonePublishRestaurant(call.message)
    if call.data == 'restaurant_topublishTrue':
        requestPublishRestaurant(call.message)
    if call.data=="open_questions":
        question_user_info(call.message)
    if call.data=="new_restaurant_application":
        show_application_new_restaurant(call.message)

def start_bot():
    bot.polling()