import json
with open("jason.txt","r") as arquivo:
    texto= arquivo.read()
cenario=json.loads(texto)