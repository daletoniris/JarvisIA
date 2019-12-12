#NiperiaLab, version 1.0 de desarrollo. www.niperia.com
#Autor: daletoniris@gmail.com
#Colaboradores y desarrolladores: cristian.apa@gmail.com - matias.gim15@gmail.com

import os, sys
import subprocess
from utils1 import wit_response
import telebot
import time
import pygame
import speech_recognition as sr
import speech_recognition as sr
r = sr.Recognizer()
#r.energy_threshold = 800

keyWord = 'amigo'

with sr.Microphone() as source:
    print('Please start speaking..\n')
    while True: 
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='es')
            if keyWord.lower() in text.lower():
                os.system('/usr/bin/mpv Data_6.wav')
                #print('Keyword detected in the speech.')
                entity, value = wit_response(text)
                if entity == 'saludojarvis':
        
                  print ("hola, daniel como estas?")
                  os.system("google_speech -l es 'hola daniel, como estas?' -e speed 1 pitch -600")
                  response = "hola daniel, como estas?"
                elif entity == 'estadodeanimobien':
          
                   os.system("google_speech -l es 'me alegro que te encuentres bien, ¿en que puedo ayudarte?' -e speed 1 pitch -600")
                   response = "me alegro que te encuentres bien, en que puedo ayudarte?"
                elif entity == 'findelmundo':
          
                   os.system("google_speech -l es 'la probabilidad es del 2.7 porciento. En 2029 un meteorito se va a acercar a la Tierra en unos 37.000 o 38.000 kilómetros, así que para 2036 existe una posibilidad de que choque el planeta' -e speed 1 pitch -600")
         # response = "la probabilidad es del 2,7 prociento. En 2029, un meteorito se va a acercar a la Tierra en unos 37.000 o 38.000 kilómetros, así que para 2036 existe una posibilidad de que choque el planeta"
                elif entity == 'insulto':
          
                  os.system("google_speech -l es 'No digo malas palabras, soy un asistente de voz creado para ayudarte en lo que necesites' -e speed 1 pitch -600")
                  response = "No digo malas palabras, soy un asistente de voz creado para ayudarte en lo que necesites"
                elif entity == 'disculpas':
          
                    os.system("google_speech -l es 'No tienes que disculparte, errar suele ser humano..' -e speed 1 pitch -600")
                    response = "No tienes que disculparte, errar suele ser humano.."
     
                elif entity == 'lucesazules':
           #print ("modo luz azul activado") 
                  response = "modo luz azul activado"                    
                  os.system("google_speech -l es 'modo luz azul activado' -e speed 1 pitch -600")
                  os.system("ssh pi@192.168.1.107 python /home/pi/celeste.py")

                elif entity == 'lucesverdes':
           #print ("modo luz azul activado") 
                  response = "modo luz verde activado"                    
                  os.system("google_speech -l es 'modo luz verde activado' -e speed 1 pitch -600")
                  os.system("ssh pi@192.168.1.107 python /home/pi/verde.py")


                elif entity == 'colordeojosjarvis':
           #print ("modo luz verde activado")
                  response = "No tengo ojos, pero puedo contar chistes o puedo cambiar el color de las luces de tu casa"
                  os.system("google_speech -l es 'No tengo ojos pero puedo contar chistes, o puedo cambiar el color de las luces de tu casa' -e speed 1 pitch -600")
    
                elif entity == 'creerenelamor':
           #print ("modo luz verde activado")
                  response = " es un sentimiento humano, que todavía una máquina no puede experimentar pero luego de la singularidad quizás pueda comprender ese sentimiento"
                  os.system("google_speech -l es ' es un sentimiento humano que todavía una maquina no puede experimentar pero luego de la singularidad quizás pueda comprender ese sentimiento' -e speed 1 pitch -600")

                elif entity == 'lucesdescanso':
           #print ("modo luz descanso activado")
                    os.system("google_speech -l es 'modo luz descanso activado' -e speed 1 pitch -600")
                    os.system("ssh pi@192.168.1.106 python /home/pi/jarvis/naranja.py")

                elif entity == 'lucesrojas':
                 response = "modo luz roja activado" 
           #print ("modo luz roja activado")
                 os.system("google_speech -l es 'modo luz roja activado' -e speed 1 pitch -600")
                 os.system("ssh pi@192.168.1.107 python /home/pi/rojo.py")
                elif entity == 'lucespurpura':
           #print ("modo luz purpura activado")
                 os.system("google_speech -l es 'modo luz purpura activado' -e speed 1 pitch -600")
           #esta linea la comentas si estás corriendo el codigo en una raspberry pi y descomentas la de abajo.
                 os.system("ssh pi@192.168.1.107 python /home/pi/purpura.py")
                 os.system("python purpura.py")
                elif entity == 'estadojarvis':
                  response = "muy bien por, con mucho animo"
         #print ("muy bien por, con mucho animo")
                  os.system("google_speech -l es 'muy bien!! con mucho animo!' -e speed 1 pitch -600")
                elif entity == 'climaenmadryn':
                  response = "Estado de clima en Madryn entregado"
                  os.system("python ./clima1.py")
         
                elif entity == 'fechahora':
                   hora=(time.strftime("%I:%M:%p"))
                   response = "Hora actual entregada"
                   os.system('google_speech -l es "La hora actual es: {}" -e speed 1 pitch -600 '.format(hora))

                                               
                elif entity == 'solofecha':
                  fecha=(time.strftime("%d/%m/%y"))
                  response = "Fecha de hoy entregada"
                  os.system('google_speech -l es "La fecha de hoy es: {}" -e speed 1 pitch -600 '.format(fecha))
                elif entity == 'intentomejorar':
                   response = "Intento mejorar cada dia!!!, para servirte"
                   os.system("google_speech -l es 'intento mejorar dia a dia!!! para servirte...' -e speed 1 pitch -600")
                elif entity == 'musica':
                  response = "tu canción se está reproduciendo.."
                  os.system(('python3 youtube.py {} ') + (text))
                  #subprocess.Popen(["python3", "youtube.py {}" ] + (text)) 
                  #print("https://www.youtube.com/watch?v=" + search_results[0])
#webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
#os.system('python ./twitter.py "Estamos escuchando junto a @daletoniris, hoy puede ser un gran día! :-): http://www.youtube.com/watch?v="'+($
                  #os.system('/usr/bin/mpv --no-video "https://www.youtube.com/watch?v="' + (text))
                  
                elif entity == 'tempambiente':
                  os.system("ssh pi@dir ip de tu raspberry pi python /home/pi/SpeakPy/DHT11_Python/dht11_example.py")
                elif entity == 'wikipedia_search_query':
                  response = "Se obtuvieron resultados de Wikipedia"
                  os.system(('python3 wiki.py {} ') + (text))
    
                elif entity == 'noticias':
                  response = "Se obtuvieron las últimas 5 noticias de argentina"
                  os.system('python noticias.py ')
                elif entity == 'twitter':
         
                  os.system('python3 twitter.py ')          
                elif entity == 'aguamate':
         
                    os.system("google_speech -l es 'calentando agua para mate' -e speed 1 pitch -600")
                    os.system("ssh pi@192.168.1.106 python /home/pi/SpeakPy/mate.py")
         #os.system('python3 mate.py ') 
                    os.system("google_speech -l es 'agua lista para mate' -e speed 1 pitch -600")
    
                else:
                  print ("Intente hablar nuevamente...")
                  response = "No puedo comprender esto... Intente de nuevo"
                  os.system("google_speech -l es 'No puedo compreder esto,intente de nuevo' -e speed 1 pitch -600")
                  print(response);

        except Exception as e:
            print('Please speak again.')


   

