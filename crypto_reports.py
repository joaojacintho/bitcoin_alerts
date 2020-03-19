# -- coding: utf-8 --
import telebot
from telebot import types
import requests
import json

token = open("token.txt", "r")
API_TOKEN = str(token.readline())
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    cid = message.chat.id
    msg = bot.reply_to(message, "Olá, eu sou o Owen o bot criado Por João Lucas, para lhe dar alertas de valores das principais criptomoedas \n https://github.com/joaojacintho/ \n")
    bot.send_message(cid, "Caso precise de Ajuda, use a função /help")

@bot.message_handler(commands=['help'])
def send_help(message):
    cid = message.chat.id
    msg_help = bot.reply_to(message, "Listar Cryptomoedas: /crypto \n") 

    bot.send_message(cid, "Caso ainda tenha alguma duvida entre em contato pelo email owenbot@contato.com.br")

@bot.message_handler(commands=['crypto'])
def send_values_crypto(message):
    cid = message.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('BTC','LTC','BCH','XRP','ETH')

    msg_crypto = bot.reply_to(message, "Escolha qual cryptomoeda você quer ver o valor", reply_markup=markup)

    bot.register_next_step_handler(msg_crypto, send_values_crypto_step)

def send_values_crypto_step(message):
    cid = message.chat.id
    currence_selected = message.text
    response = requests.get("https://www.mercadobitcoin.net/api/"+currence_selected+"/ticker/")
    data = response.json()

    high = data['ticker']['high']
    low = data['ticker']['low']

    bot.send_message(cid, "Max: R$"+high+"\nMin: R$"+low+"\nValores das ultimas 24h")

bot.polling()
