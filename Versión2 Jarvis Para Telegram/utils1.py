#NiperiaLab, version 1.0 de desarrollo. www.niperia.com
#Autor: daletoniris@gmail.com
#Colaboradores y desarrolladores:  
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
#print(wit_response("blanco y negro"))
