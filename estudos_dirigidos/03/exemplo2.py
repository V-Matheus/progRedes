import socket, sys, os

# --------------------------------------------------
# Documentação Protocolo HTTP
# https://datatracker.ietf.org/doc/html/rfc2616
# --------------------------------------------------

# --------------------------------------------------
PORT        = 80  # 443
CODE_PAGE   = 'utf-8'
BUFFER_SIZE = 256
# --------------------------------------------------

host = input('\nInforme o nome do HOST ou URL do site: ')

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
caminho_do_arquivo = os.path.join(os.path.dirname(__file__), 'output.html')

try:
    tcp_socket.connect((host, PORT))
except:
    print(f'\nERRO.... {sys.exc_info()[0]}')
else:
    tcp_socket.settimeout(5)
    requisicao = f'GET / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
    try:
        tcp_socket.sendall(requisicao.encode(CODE_PAGE))
    except:
        print(f'\nERRO.... {sys.exc_info()[0]}')
    else:
        print('-'*50)
        resposta_completa = ''
        while True:
            try:
                resposta = tcp_socket.recv(BUFFER_SIZE).decode(CODE_PAGE)
                if not resposta:
                    break
                resposta_completa += resposta
            except socket.timeout:
                break
        print('Arquivo salvo em output.html')

        cabecalho, corpo = resposta_completa.split('\r\n\r\n', 1)

        with open(caminho_do_arquivo, 'w', encoding=CODE_PAGE) as file:
            file.write(corpo)
        print('-'*50)
    tcp_socket.close()


# Deve desconsiderar o cabeçalho !!