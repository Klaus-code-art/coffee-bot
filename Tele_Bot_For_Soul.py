import telebot
import random

from dotenv import load_dotenv

import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
PHONE = os.getenv('PHONE')

bot = telebot.TeleBot(TOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard4 = telebot.types.ReplyKeyboardMarkup()
keyboard5 = telebot.types.ReplyKeyboardMarkup()
keyboard6 = telebot.types.ReplyKeyboardMarkup()
keyboard7 = telebot.types.ReplyKeyboardMarkup()
game_board = telebot.types.ReplyKeyboardMarkup()


keyboard1.row('Кто ты ?', 'Расскажи о Кофейне', "Расскажи Музыкальной школе")
keyboard2.row('Расскажи о Кофейном Оазисе', "Расскажи Гильдии Менестрелей", "Давай поиграем")
keyboard3.row('Кто ты ?', 'Расскажи о Кофейне', "Расскажи Музыкальной школе")
keyboard4.row("Go back")
keyboard5.row("Как начать учиться у вас?", "Скинь вк группу", "Go back")
keyboard6.row("Расскажи о Кофе", "Расскжи о Чаепитии", "Расскажи об играх")
keyboard7.row("Куда писать?", "Кому звонить? ", "Куда ходить?", "Go back")
game_board.row("Начать игру", "Go back")


def plug(message):

	bot.send_message(message.chat.id, "Извини, я не знаю что ответить (", reply_markup=keyboard4)

def moving_dialogue(message):

	bot.send_message(message.chat.id, "Что хочешь узнать еще интересненького, друг? (", reply_markup=keyboard2)

@bot.message_handler(commands = ['start'])
def handle_start_help(message):
	bot.send_message(message.chat.id, 'Привет, ты написал мне...', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])


#elif message.text.lower() == '' :

def send_text(message):

	if message.text.lower() == 'кто ты ?':
		bot.send_message(message.chat.id, 'Я душа Белого Котика поддерживающая Гильдию Менестрелей и Кофейный Оазис')
		bot.send_message(message.chat.id, 'Что еще желаешь узать? ^_^', reply_markup=keyboard2)

	elif message.text.lower() == 'расскажи о кофейне' or message.text.lower() == "расскажи о кофейном оазисе" :
		bot.send_message(message.chat.id, "кофе тут замечательный ")
		bot.send_message(message.chat.id, "И не только кофе... Вкуснятин много ^_^ ", reply_markup=keyboard6)

	elif message.text.lower() == 'расскажи музыкальной школе' or message.text.lower() == "расскажи гильдии менестрелей":

		bot.send_message(message.chat.id, "Это интересное заведение где обучают музыке с нуля за адекватные сроки, взгляни на красивый сайт http://www.music4soul.ru", reply_markup=keyboard5)
	elif message.text.lower() == 'go back':
		bot.send_message(message.chat.id, "Что желаешь узнать интересненького ?", reply_markup=keyboard1)

	elif message.text.lower() == 'как начать учиться у вас?':
		bot.send_message(message.chat.id, "Звони, приходи, пиши Мастерам , Муррр", reply_markup=keyboard7)

	elif message.text.lower() in ("люблю", "love", "влюблен", "я тебя люблю"):
		bot.send_sticker(message.chat.id, "CAACAgEAAxkBAANJXu8SKgV5FUxDUb9Ly2YKXplRgxMAAlceAAJ4_MYFiWCMCXM4NQgaBA", reply_markup=keyboard2)

	elif message.text.lower() == 'скинь вк группу':
		bot.send_message(message.chat.id, "Делжи ^_^ https://vk.com/artlabmusicforsoul, будь в курррсе всех новостей ")

	elif message.text.lower() == 'расскажи о кофе' :
		bot.send_message(message.chat.id, "Есть огромный очерширительный творческий рацион...")
		bot.send_message(message.chat.id, "А сиропы просто вкустятина... Сними есть Шедрая викторина ..", reply_markup=keyboard2)

	elif message.text.lower() == 'куда писать?':
		bot.send_message(message.chat.id, "Пиши нашему Главному куратору https://vk.com/finefriend, он поможет найти грани твоей одаренности в на пути волшебном искусства ", reply_markup=keyboard5)

	elif message.text.lower() == 'куда ходить?':
		bot.send_message(message.chat.id, "Улица Гарибальди дом 36, м Новые черемушки Москва... ")

	elif message.text.lower() in ("кому звонить?"):
		bot.send_message(message.chat.id, " Звони по телефону" + PHONE + " добрый админ ответит" )

	elif message.text.lower() == 'давай поиграем':
		bot.send_message(message.chat.id, 'Муррр...Пусть победит сильнейший ', reply_markup=game_board)

	elif message.text.lower() == 'расскжи о чаепитии':

		bot.send_message(message.chat.id, "Оно веселое как у Шляпника, который завариает превосходный листовой чай", reply_markup=keyboard4)

	elif message.text.lower() == 'расскажи об играх':

		bot.send_message(message.chat.id, "Мой создатель разрабатывает концепции некоторых интересных шарад, сложнАААА =_=")

	elif message.text.lower() == 'начать игру':

		bot.send_message(message.chat.id, "Мой создатель разрабатывает игру, будте терпеливы ^.^", reply_markup=keyboard4)
		moving_dialogue(message)

	else:
		plug(message)

print("Бот запущен")
bot.polling()