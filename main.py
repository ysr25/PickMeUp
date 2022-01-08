import os
import telebot
from pickup import random_pickup

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id

    bot.reply_to(
        message,
        "Looking to be picked up? Wanna learn some pickup lines to pick someone up? \n\nSend /pickup to reveal a pickup line! 😉"
    )

    bot.send_sticker(
        chat_id=chat_id,
        data=
        'CAACAgQAAxkBAAEDonhh2HrOHsqDZZ3X_XF2wOboBTzyeAACBAADGnJbEHtql2cQmmR0IwQ'
    )


@bot.message_handler(commands=['help'])
def send_help(message):

    help_text = 'Give me the commands :3 \n'
    help_text += '/start    : start the bot \n'
    help_text += '/help    : reveal all commands \n'
    help_text += '/pickup: get pickup line \n'
    help_text += '<3'

    bot.reply_to(message, help_text)


@bot.message_handler(commands=['pickup'])
def send_praise(message):
    pickup_line = random_pickup()
    bot.reply_to(message, pickup_line)


# Handle all other messages with content_type 'text' (content_types defaults to ['text']) (from the API doc)
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Try another command or use /help 😘")


bot.infinity_polling()
