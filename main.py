import telebot
from telebot import types
import requests
import random
from bs4 import BeautifulSoup

URL = 'https://www.anekdot.ru/last/good'
def parser(url):
	response = requests.get(url)
	#beautiful soup
	soup = BeautifulSoup(response.text, 'html.parser')
	#all
	allAnekdot = soup.find_all('div', class_='text')
	return [c.text for c in allAnekdot]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

#bot
bot = telebot.TeleBot('')#token

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, text="Hello")

#button
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Анекдот")

	markup.add(item1)

	#bot.send_message(message.chat.id, "Что будем делать?", reply_markup=markup)

# send anekdot
@bot.message_handler(content_types=['text'])
def youmor(message):
	if message.chat.type == 'private':
		if message.text == 'Анекдот':
			bot.send_message(message.chat.id, list_of_jokes[0])
			del list_of_jokes[0]

#interval bots
bot.polling(none_stop=True, interval=0)
