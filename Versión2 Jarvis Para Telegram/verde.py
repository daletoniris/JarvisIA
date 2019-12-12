import os
import RPi.GPIO as GPIO
import pyttsx
import pygame
GPIO.setmode(GPIO.BOARD)
engine = pyttsx.init()
engine.setProperty('rate', 160)  
engine.setProperty('voice',  "spanish")
led = 15
led1= 11
led2=13
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.output(led, False)
GPIO.output(led1, False)
GPIO.output(led2, False)
def habla(texto):
    engine.say(texto)
    engine.runAndWait()

#habla("modo: luces verdes")
GPIO.output(led, False)
GPIO.output(led1, False)
GPIO.output(led2, True)
#time.sleep(2)
#GPIO.output(led, Fals
