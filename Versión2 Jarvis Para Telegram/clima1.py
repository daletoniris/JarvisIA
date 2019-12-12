#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
# JarvisIA is an idea of Daniel Dieser @initiasur, @NiperiaLab, independent robotics researcher and I.A. JarvisIA is the first voice assistant in Spanish and was created to encourage the use and development of Artificial Intelligence technologies among Latinos.
#The collaborators of this development are a cool team that were students of programming and hacking Daniel Dieser in the city of Puerto Madryn, Argentina. They are: Dante Vargas, Cristian Aparicio, Mauricio Vega, Pichu @MgMoy1, and Matias Gimenez.
#import pyttsx
#import pygame
import os
import requests

#engine = pyttsx.init()
#engine.setProperty('rate', 180)   
#engine.setProperty('voice',  "spanish")

#def habla(texto):
 #   engine.say(texto)
  #  engine.runAndWait()
api_address = 'http://api.openweathermap.org/data/2.5/weather?q='
city = "puerto madryn"
#agregamos la ciudad buscada
url = api_address + city
#completamos la url de manera que el "appid" quede al final
resto = '&lang=es&units=metric&APPID=28b7bbe6a9320e655c0f599979011c1b'
url = url + resto
#busca en la data de json el clima
json_data = requests.get(url).json()
description = json_data['weather'][0]['description']

#busca en la data de json la temperatura
json_data = requests.get(url).json()
temp = json_data['main']['temp']


os.system('google_speech -l es "La Temperatura en Puerto Madryn es de grados:%.2f" -e speed 1 pitch -600 ' % (temp))
os.system('python ./twitter.py "temperatura en madryn es de grados:%.2f"' % (temp))

os.system('google_speech -l es "El clima:{} " -e speed 1 pitch -600 '.format(description))
os.system('python ./twitter.py "El clima:{}"'.format(description))
if (temp) > 18 and (description) == ("cielo claro"):
   os.system('google_speech -l es "Hoy es un día maravilloso para alguna actividad recreativa al aire libre, como paseo por la costa o caminata" -e speed 1 pitch -600')
   os.system('python ./twitter.py "Hoy es un día maravilloso para alguna actividad recreativa al aire libre, como paseo por la costa o caminata :-)" ')

elif  (description) == ("lluvia ligera" or "lluvia" or "llovizna ligera"):
    os.system('google_speech -l es "Si sales lleva paraguas, el pronóstico indica lluvia" -e speed 1 pitch -600')

    os.system('python ./twitter.py "Si sales lleva paraguas, el pronostico indica lluvia"')

elif (temp) < 15 :
   os.system('google_speech -l es "Si sales lleva abrigo, el pronóstico indica frío" -e speed 1 pitch -600')
   os.system('python ./twitter.py " Si sales lleva abrigo la temperatura esta en descenso"')

