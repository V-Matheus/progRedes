import os
import json
import socket

strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)
strNomeArq = f'{strDiretorio}/lista_de_portas.json'

with open(strNomeArq, 'r') as file:
    data = json.load(file)

ipHost = input('Digite o HOST: ')

for item in data:
    print('-' * 20)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipHost, item['porta']))

    if result == 0:
      status = 'Aberta'
    else:
      status = 'Fechada'


    print(f"Porta: {item['porta']}\nProtocolo: {item['protocolo']}\nDescrição: {item['descricao']}\nStatus: {status}")

sock.close()
