import json
with open("json.txt","r") as arquivo:
    texto= arquivo.read()
cenario=json.loads(texto)