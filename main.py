import telebot
from telebot import types
import datetime as dt
from modules import days, tomorrow_day, request_day_cht, request_day_necht
from request import str_cht, str_necht
from settings import tokenTgBot

token = tokenTgBot
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("хочу", "не хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Я Жорик Ибрагимов. Хочешь узнать свежую информацию о МТУСИ?',
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею показывать расписание : \n'
                                      '/week - на текущую неделю \n'
                                      '/nextweek - на следующую неделю \n'
                                      '/today - на сегодня \n'
                                      '/tomorrow - на завтра \n'
                                      '/monday - на понедельник\n'
                                      '/tuesday - на вторник\n'
                                      '/wednesday - на среду\n'
                                      '/thursday - на четверг\n'
                                      '/friday - на пятницу\n'
                                      '/saturday - на субботу\n')


@bot.message_handler(commands=['week'])
def start_message(message):
    date = dt.datetime.now()
    week = date.strftime('%U')
    if int(week) % 2 == 0:

        bot.send_message(message.chat.id, str_cht,
                         parse_mode='html')
    elif int(week) % 2 == 1:

        bot.send_message(message.chat.id, str_necht,
                         parse_mode='html')


@bot.message_handler(commands=['nextweek'])
def start_message(message):
    date = dt.datetime.now()
    week = date.strftime('%U')
    if (int(week) + 1) % 2 == 0:

        bot.send_message(message.chat.id, str_cht,
                         parse_mode='html')
    elif (int(week) + 1) % 2 == 1:

        bot.send_message(message.chat.id, str_necht,
                         parse_mode='html')


@bot.message_handler(commands=['today'])
def start_message(message):
    date = dt.datetime.now()
    week = date.strftime('%U')
    day = days(str(date.strftime('%A')))
    if int(week) % 2 == 0:
        a = request_day_cht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')

    elif int(week) % 2 == 1:
        a = request_day_necht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')


@bot.message_handler(commands=['tomorrow'])
def start_message(message):
    date = dt.datetime.now()
    week = date.strftime('%U')
    day = tomorrow_day(str(date.strftime('%A')))
    if int(week) % 2 == 0:
        a = request_day_cht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')

    elif int(week) % 2 == 1:
        a = request_day_necht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')


@bot.message_handler(commands=['monday'])
def start_message(message):
    date = dt.datetime.now()
    week = date.strftime('%U')
    day = days('Monday')
    if int(week) % 2 == 0:
        a = request_day_cht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')

    elif int(week) % 2 == 1:
        a = request_day_necht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')


@bot.message_handler(commands=['tuesday'])
def start_message(message):
    date = dt.datetime.now()
    week = date.strftime('%U')
    day = days('Tuesday')
    if int(week) % 2 == 0:
        a = request_day_cht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')

    elif int(week) % 2 == 1:
        a = request_day_necht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')


@bot.message_handler(commands=['wednesday'])
def start_message(message):
    date = dt.datetime.now()
    week = date.strftime('%U')
    day = days('Wednesday')
    if int(week) % 2 == 0:
        a = request_day_cht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')

    elif int(week) % 2 == 1:
        a = request_day_necht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')


@bot.message_handler(commands=['thursday'])
def start_message(message):
    date = dt.datetime.now()
    week = date.strftime('%U')
    day = days('Thursday')
    if int(week) % 2 == 0:
        a = request_day_cht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')

    elif int(week) % 2 == 1:
        a = request_day_necht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')


@bot.message_handler(commands=['friday'])
def start_message(message):
    date = dt.datetime.now()
    week = date.strftime('%U')
    day = days('Friday')
    if int(week) % 2 == 0:
        a = request_day_cht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')

    elif int(week) % 2 == 1:
        a = request_day_necht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')


@bot.message_handler(commands=['saturday'])
def start_message(message):
    date = dt.datetime.now()
    week = date.strftime('%U')
    day = days('Saturday')
    if int(week) % 2 == 0:
        a = request_day_cht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')

    elif int(week) % 2 == 1:
        a = request_day_necht(day)
        bot.send_message(message.chat.id, a,
                         parse_mode='html')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда вам сюда - https://mtuci.ru/')
    elif message.text.lower() == "не хочу":
        bot.send_message(message.chat.id, 'Ладно , тогда воспользуйтесь моим меню !')
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю...')


bot.polling(none_stop=True)
