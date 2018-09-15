#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
# JarvisIA is an idea of Daniel Dieser @initiasur, @NiperiaLab, independent robotics researcher and I.A. JarvisIA is the first voice assistant in Spanish and was created to encourage the use and development of Artificial Intelligence technologies among Latinos.
#The collaborators of this development are a cool team that were students of programming and hacking Daniel Dieser in the city of Puerto Madryn, Argentina. They are: Dante Vargas, Cristian Aparicio, Mauricio Vega, Pichu @MgMoy1, and Matias Gimenez.

import os, sys
#from flask import Flask, request
from utils import wit_response, wit_access_token
import requests
import json
from Recorder import record_audio, read_audio
import os
import pygame
from wit import Wit
import time


# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'

# Wit.ai api access token

def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 5):
    
    
    
    # reading audio
    audio = read_audio(AUDIO_FILENAME)
    
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}

    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
    global data
    # converting response content to JSON format
    data = json.loads(resp.content)
    #data = response.json()
    global text
    #global locate
    #global entity
    # get text from data
    text = data['_text']
    #locate = data['location']
    #entity = data['entities']    
# return the text
    return text
    #return locate
    #return entity
if __name__ == "__main__":
    text =  RecognizeSpeech('test1.wav', 4)
   
#    print(u"\nTu dices: {}".format(text))
    
    messaging_text = text

    response = None

    entity, value = wit_response(messaging_text)
    
    if entity == 'saludojarvis':
         #coloca aquí tu nombre
         print ("hola, daniel como estas?")
         os.system("google_speech -l es 'hola daniel, como estas?' -e speed 1 pitch -600")
    elif entity == 'estadodeanimobien':
          
          os.system("google_speech -l es 'me alegro que te encuentres bien' -e speed 1 pitch -600")
    elif entity == 'lucesazules':
           print ("modo luz azul activado")                      
           os.system("google_speech -l es 'modo luz azul activado' -e speed 1 pitch -600")
           os.system("ssh pi@dir ip de tu raspberry pi python /home/pi/SpeakPy/celeste.py")
    elif entity == 'lucesverdes':
           print ("modo luz verde activado")
           os.system("google_speech -l es 'modo verde activado' -e speed 1 pitch -600")
           os.system("ssh pi@dir ip de tu raspberry pi python /home/pi/SpeakPy/verde.py")

    elif entity == 'lucesdescanso':
           print ("modo luz descanso activado")
           os.system("google_speech -l es 'modo luz descanso activado' -e speed 1 pitch -600")
           os.system("ssh pi@dir ip de tu raspberry pi python /home/pi/SpeakPy/naranja.py")

    elif entity == 'lucesrojas':
           print ("modo luz roja activado")
           os.system("google_speech -l es 'modo luz roja activado' -e speed 1 pitch -600")
           os.system("ssh pi@dir ip de tu raspberry pi python /home/pi/SpeakPy/rojo.py")
    elif entity == 'lucespurpura':
           print ("modo luz purpura activado")
           os.system("google_speech -l es 'modo luz purpura activado' -e speed 1 pitch -600")
           #esta linea la comentas si estás corriendo el codigo en una raspberry pi y descomentas la de abajo.
           os.system("ssh pi@dir ip de tu raspberry pi python /home/pi/SpeakPy/purpura.py")
           os.system("python purpura.py")
    elif entity == 'estadojarvis':
         print ("muy bien por, con mucho animo")
         os.system("google_speech -l es 'muy bien!! con mucho animo!' -e speed 1 pitch -600")
    elif entity == 'climaenmadryn':
         os.system("python ./clima1.py")
         
    elif entity == 'fechahora':
          hora=(time.strftime("%I:%M:%S:%p"))
          os.system('google_speech -l es "La hora actual es: {}" -e speed 1 pitch -600 '.format(hora))

                                               
    elif entity == 'solofecha':
          fecha=(time.strftime("%d/%m/%y"))
          os.system('google_speech -l es "La fecha de hoy es: {}" -e speed 1 pitch -600 '.format(fecha))
    elif entity == 'intentomejorar':
          os.system("google_speech -l es 'intento mejorar dia a dia!!! para servirte...' -e speed 1 pitch -600")
    elif entity == 'musica':
        
         os.system(('python3 youtube.py {} ') + (text))
         
    elif entity == 'tempambiente':
          os.system("ssh pi@dir ip de tu raspberry pi python /home/pi/SpeakPy/DHT11_Python/dht11_example.py")
    elif entity == 'wikipedia_search_query':
         
         os.system(('python3 wiki.py {} ') + (text))
    
    elif entity == 'noticias':
         
         os.system('python noticias.py ')
    elif entity == 'twitter':
         
         os.system('python3 twitter.py ')          
    elif entity == 'aguamate':
         
         os.system("google_speech -l es 'calentando agua para mate' -e speed 1 pitch -600")
        #esta linea la comentas si estás corriendo el codigo en una raspberry pi y descomentas la de abajo.
         os.system("ssh pi@dir ip de tu raspberry pi python /home/pi/SpeakPy/mate.py")
         #os.system('python3 mate.py ') 
         os.system("google_speech -l es 'agua lista para mate' -e speed 1 pitch -600")
    else:
      print ("Intente hablar nuevamente...")
