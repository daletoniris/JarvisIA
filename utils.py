  #!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
# JarvisIA is an idea of Daniel Dieser @initiasur, @NiperiaLab, independent robotics researcher and I.A. JarvisIA is the first voice assistant in Spanish and was created to encourage the use and development of Artificial Intelligence technologies among Latinos.
#The collaborators of this development are a cool team that were students of programming and hacking Daniel Dieser in the city of Puerto Madryn, Argentina. They are: Dante Vargas, Cristian Aparicio, Mauricio Vega, Pichu @MgMoy1, and Matias Gimenez.
import os, sys

from wit import Wit 
from gnewsclient import gnewsclient

wit_access_token = "N3NSTRW4URUL3EMK3EMXJQKC6XRKUGFA"
client = Wit(access_token = wit_access_token)

def wit_response(message_text):
	resp = client.message(message_text)
	
	entity = None
	value = None

	try:
		entity = list(resp['entities'])[0]
		value = resp['entities'][entity][0]['value']
	except:
		pass

	return (entity, value)
#print(wit_response("se ve con descargas"))
