import telebot
import requests
from telebot import types

token = "5081420211:AAG3Ojqm7wijtR31IiBMdZuaLItwWEPDxbM"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать интересный факт о китах?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/Факт_о_китах", "/Факт_о_касатках", "/Факт_о_дельфинах")
    bot.send_message(message.chat.id, 'Я умею: \n'
                                      '/fakt_o_kitah' '\n'
                                      '/fakt_o_kasatkah' '\n'
                                      '/fakt_o_delfinah' '\n')


@bot.message_handler(commands=['fakt_o_kitah'])
def start_message(message):
    bot.send_message(message.chat.id, 'Факты о китах ты можешь найти здесь: http://obshe.net/posts/id1459.html')


@bot.message_handler(commands=['fakt_o_kasatkah'])
def start_message(message):
    bot.send_message(message.chat.id, 'Факты о касатках ты можешь найти здесь: http://obshe.net/posts/id1647.html')


@bot.message_handler(commands=['fakt_o_delfinah'])
def start_message(message):
    bot.send_message(message.chat.id, 'Факты о дельфинах ты можешь найти здесь: http://obshe.net/posts/id1130.html')

@bot.message_handler(content_types=['text'])
def find_text(message):
    if message.text.lower()== "хочу":
        bot.send_message(message.chat.id,'Напиши /help')

if __name__ == '__main__':
    bot.polling(none_stop=True)
