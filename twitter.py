#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
# JarvisIA is an idea of Daniel Dieser @initiasur, @NiperiaLab, independent robotics researcher and I.A. JarvisIA is the first voice assistant in Spanish and was created to encourage the use and development of Artificial Intelligence technologies among Latinos.
#The collaborators of this development are a cool team that were students of programming and hacking Daniel Dieser in the city of Puerto Madryn, Argentina. They are: Dante Vargas, Cristian Aparicio, Mauricio Vega, Pichu @MgMoy1, and Matias Gimenez.
import tweepy
from keys import *
import sys
import os
tweetear = " ".join(sys.argv[1:len(sys.argv)])

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(akey, asecret)


twitter = tweepy.API(auth)

#con esta funcion tweeteo en mi cuenta
def tuitear(tweetear):
	twitter.update_status(tweetear)



#con esta funcion obtengo los 5 tweets mas recientes de la busqueda que quiero
#en ITMS va la cantidad total de tweets que queremos que nos devuelva
#en COUNT va la cantidad de tweets que pueden entrar en cada pagina
def buscartuits(tweetear):
	contador = 0
	for tweet in tweepy.Cursor(twitter.search,
                           q=tweetear,
                           count=100,
                           result_type="recent",
                           include_entities=True,
                           lang="es").items(5):
		contador = contador + 1
		texto= (tweet.text+'\n\n')
                os.system('google_speech -l es "{} " -e speed 1 pitch -600 '.format(texto))
                 
#textoo=(tweet.text)

                #os.system('google_speech -l es "{} " -e speed 1 pitch -600 '.format(tweetear))

buscartuits(tweetear)
#tuitear(tweetear)
#os.system('google_speech -l es "{} " -e speed 1 pitch -600 '.format(texto))

