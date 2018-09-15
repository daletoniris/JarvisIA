#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
# JarvisIA is an idea of Daniel Dieser @initiasur, @NiperiaLab, independent robotics researcher and I.A. JarvisIA is the first voice assistant in Spanish and was created to encourage the use and development of Artificial Intelligence technologies among Latinos.
#The collaborators of this development are a cool team that were students of programming and hacking Daniel Dieser in the city of Puerto Madryn, Argentina. They are: Dante Vargas, Cristian Aparicio, Mauricio Vega, Pichu @MgMoy1, and Matias Gimenez.
import pyttsx3

import pygame
import os
#import RPi.GPIO as GPIO
import time
engine = pyttsx3.init()
engine.setProperty('rate', 180) 
engine.setProperty('voice',  "spanish")

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(24, GPIO.IN)

#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def habla(texto):
    engine.say(texto)
    engine.runAndWait()

while True:
    #uncomment this line if you use a button to start recording on a raspberry
    #input_state = GPIO.input(18)
    #if input_state == False:
       # print('Button Pressed')
        #time.sleep(0.2)

        #pygame.mixer.init()
        #pygame.mixer.music.load("Data_6.wav")
        #pygame.mixer.music.play()



        
#habla("que musica quieres escuchar?")
   #print ("hable por favor")
   #os.system("google_speech -l es 'en que puedo ayudarte?' -e speed 1 pitch -600")

#print ("habla por favor...")
   os.system("arecord -d 5 -D plughw:0,0 test1.wav")
        #time.sleep(3)
           
   os.system("python ./jarvispoc.py")
   #time.sleep(1)
             
