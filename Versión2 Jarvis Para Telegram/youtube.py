#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
# JarvisIA is an idea of Daniel Dieser @initiasur, @NiperiaLab, independent robotics researcher and I.A. JarvisIA is the first voice assistant in Spanish and was created to encourage the use and development of Artificial Intelligence technologies among Latinos.
#The collaborators of this development are a cool team that were students of programming and hacking Daniel Dieser in the city of Puerto Madryn, Argentina. They are: Dante Vargas, Cristian Aparicio, Mauricio Vega, Pichu @MgMoy1, and Matias Gimenez.
import sys
import urllib.request
import urllib.parse
import re
import os
import webbrowser

cancion = " ". join(sys.argv[1:len(sys.argv)])
query_string = urllib.parse.urlencode({"search_query" : (cancion)})
html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
#os.system('google_speech -l es "reproduciendo su lista:" -e speed 1 pitch -600 ')

print("https://www.youtube.com/watch?v=" + search_results[0])
#webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
#os.system('python ./twitter.py "Estamos escuchando junto a @daletoniris, hoy puede ser un gran día! :-): http://www.youtube.com/watch?v="'+(search_results[0]))
os.system('/usr/bin/mpv --no-video "https://www.youtube.com/watch?v="' + (search_results[0]))
#os.system('python ./twitter.py "Reproduciendo para Niperia Lab:{}"'+(search_results[0]))
