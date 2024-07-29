import socket, sys

# --------------------------------------------------
# Documentação Protocolo HTTP
# https://datatracker.ietf.org/doc/html/rfc2616
# --------------------------------------------------

# --------------------------------------------------
PORT        = 80
CODE_PAGE   = 'utf-8'
BUFFER_SIZE = 1024
# --------------------------------------------------

host = input('\nInforme o nome do HOST ou URL do site: ')

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def criarDicionario(string):
    lines = string.split('\n')
    socketDic = {}

    status = lines[0]
    socketDic["Status"] = status.strip()

    for line in lines[1:]:
        if ':' in line:
            key, value = line.split(':', 1)
            socketDic[key.strip()] = value.strip()

    return socketDic

try:
    tcp_socket.connect((host, PORT))
except:
    print(f'\nERRO.... {sys.exc_info()[0]}')
else:
    requisicao = f'HEAD / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
    try:
       tcp_socket.sendall(requisicao.encode(CODE_PAGE))
    except:
        print(f'\nERRO.... {sys.exc_info()[0]}')
    else:
        resposta = tcp_socket.recv(BUFFER_SIZE).decode(CODE_PAGE)
        socketDic = criarDicionario(resposta)

        print('-'*50)

        for key, value in socketDic.items():
            print(f"{key}: {value}")

        print('-'*50)
    tcp_socket.close()



