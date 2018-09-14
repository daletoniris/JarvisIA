# JarvisIA is an idea of Daniel Dieser @initiasur, @NiperiaLab, independent robotics researcher and I.A. JarvisIA is the first voice assistant in Spanish and was created to encourage the use and development of Artificial Intelligence technologies among Latinos.
#The collaborators of this development are a cool team that were students of programming and hacking Daniel Dieser in the city of Puerto Madryn, Argentina. They are: Dante Vargas, Cristian Aparicio, Mauricio Vega, Pichu @MgMoy1, and Matias Gimenez.
import time
import RPi.GPIO as GPIO
import sys
import pyttsx
import pygame
import os
engine = pyttsx.init()
engine.setProperty('rate', 160)  
engine.setProperty('voice',  "spanish")

def habla(texto):
    engine.say(texto)
    engine.runAndWait()

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.HIGH)
#configuramos el pin GPIO17 como una salida




while True:

                #replace the value (28-000006dfa76c) below with yours
                tempfile = open("/sys/bus/w1/devices/28-02146388faff/w1_slave")

                #read the current temperature from DS18B20
                thetext = tempfile.read()
                tempfile.close()
                #clean the raw data
                tempdata = thetext.split("\n")[1].split(" ")[9]
                temperature = float(tempdata[2:])
                temperature = temperature / 1000
                #display the temperature
                print temperature
                #wait 1 second before next read
                time.sleep(1)
                if temperature >= 40.1:
                 GPIO.output(23, GPIO.LOW)
                 
                 os.system("google_speech -l es 'Agua lista para su mate' -e speed 1 pitch -600 ")
                #habla("agua a punto para su mate")
                #raise MiError=(temperature >= 24.5)
                 time.sleep(1)
                 break                 #3sys.exit(1):
                 #GPIO.output(23, GPIO.LOW)
                  #pass
#except MiError as temperature:
# print "fin" 

