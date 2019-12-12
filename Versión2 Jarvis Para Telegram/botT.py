#NiperiaLab, version 1.0 de desarrollo. www.niperia.com
#Autor: daletoniris@gmail.com
#Colaboradores y desarrolladores: cristian.apa@gmail.com - matias.gim15@gmail.com

import os, sys
from utils1 import wit_response
import telebot
import time

bot = telebot.TeleBot("578056637:AAF8HZNQkr-PBwTvDI8hsuR133PFT8ZDmFE")

bot.send_message('283929559', 'Hola mundo!')
#@bot.message_handler(commands=['start', 'help'])
#def send_welcome(message):
#bot.reply_to( "hola que hace?")

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
 #  print (message.text)
  # texto=message.text
##cid=message.chat.id
#print (cid)
#response= None
#def discover(bot, update, user_data):

 #  voice = bot.getFile(update.message.voice.file_id)
  # voice.download('file.ogg')

 #  client = Wit(wit_access_token)

   #with open('file.ogg', 'rb') as f:
    #   resp = client.speech(f, True, {'Content-Type': 'audio/ogg'})
   #print('Yay, got Wit.ai response: ' + str(resp))
   #entity, value = wit_response(texto)
  # if entity == 'saludojarvis':
        
    #     print ("hola, daniel como estas?")
     #    os.system("google_speech -l es 'hola daniel, como estas?' -e speed 1 pitch -600")
response = "hola daniel, como estas?"
