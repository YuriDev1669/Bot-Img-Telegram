import telepot
from googlesearch import search
from random import randint
import os



bot = telepot.Bot("SEU TOKEN BOT")


def mandando(msg):
	valor = randint(1,50)
	txt = msg['text']
	for resultado in search(f"{txt} Pinterest",stop=valor):
		os.system("clear") or None
		print(f"\033[01;32m>> IMAGEM ENCONTRADA {valor}")
	bot.sendPhoto(703975434,resultado)
	
bot.message_loop(mandando)
while True:
	pass
