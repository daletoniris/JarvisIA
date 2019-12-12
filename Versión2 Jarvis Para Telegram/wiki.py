
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
# JarvisIA is an idea of Daniel Dieser @initiasur, @NiperiaLab, independent robotics researcher and I.A. JarvisIA is the first voice assistant in Spanish and was created to encourage the use and development of Artificial Intelligence technologies among Latinos.
#The collaborators of this development are a cool team that were students of programming and hacking Daniel Dieser in the city of Puerto Madryn, Argentina. They are: Dante Vargas, Cristian Aparicio, Mauricio Vega, Pichu @MgMoy1, and Matias Gimenez.
#te trae un lindo resumen de algun tema en especial desde la wiki
import wikipedia 
import os
import sys 
#consulta = " ".join(sys.argv[3:len(sys.argv)]) 
#consulta = sys.argv[3:len(sys.argv)]
consulta = " ". join(sys.argv[3:len(sys.argv)]) 
wikipedia.set_lang("es") 
resumen = wikipedia.summary(consulta) 
#print resumen.encode('utf-8')
print (resumen)
os.system('google_speech -l es " {}" -e speed 1 pitch -600 '.format(resumen))
