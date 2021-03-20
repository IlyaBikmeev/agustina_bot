import telebot
import config
import random
import parse

from telebot import types

bot = telebot.TeleBot(config.TOKEN)



f = open('woman.txt','r')
answers = list()
for p in f:
    answers.append(p)


@bot.message_handler(commands = ['start','help'])
def welcome(message):
    sti = open('stickers/3.tgs','rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Статистика распространения коронавируса")

    markup.add(item1)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, создана, чтобы служить тебе, мой господин :3.".format(message.from_user, bot.get_me()),
        parse_mode='html',reply_markup=markup)


@bot.message_handler(content_types = ['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Статистика распространения коронавируса':
            sti = open("stickers/5.tgs",'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id,parse.CoronaStats(),parse_mode = 'html')
        else:
            sti = open("stickers/10.tgs",'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id,answers[random.randint(0,len(answers)-1)])
#RUN

bot.polling(none_stop=True)