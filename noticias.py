#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
# JarvisIA is an idea of Daniel Dieser @initiasur, @NiperiaLab, independent robotics researcher and I.A. JarvisIA is the first voice assistant in Spanish and was created to encourage the use and development of Artificial Intelligence technologies among Latinos.
#The collaborators of this development are a cool team that were students of programming and hacking Daniel Dieser in the city of Puerto Madryn, Argentina. They are: Dante Vargas, Cristian Aparicio, Mauricio Vega, Pichu @MgMoy1, and Matias Gimenez.
import requests
import os
import  sys 
import random
reload ( sys ) 
sys . setdefaultencoding ( 'utf8' )

##Usamos la api de newsapi y establecemos una pagina como fuente en Source, en este caso Infobae
json_data = requests.get('https://newsapi.org/v2/top-headlines?sources=infobae&apiKey=a4be83e5481345568a2c541775611021').json()

##Solo vemos las primeras 5 noticias
for pagina in range (0,5):

	titulo = json_data['articles'][pagina]['title']
	titulo = '' + str() + ' ' + titulo
        link = json_data['articles'][pagina]['url']
	print (titulo);
        print (link);
        os.system('google_speech -l es "{} " -e speed 1 pitch -600 '.format(titulo))
        os.system('python ./twitter.py "Noticia del día: {} "'.format((link)))
