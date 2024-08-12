import socket, time

SERVER = '127.0.0.1'
PORT   = 31435

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER, PORT))

print ('Esperando pedidos .... ')

while True:
    msg, addr = sock.recvfrom(4096)
    print(f"Recebido pedido de {addr}: {msg.decode('utf-8')}")
    strNomeArq = msg.decode('utf-8')
    strNomeArq = msg.decode('utf-8')

    print(f"Abrindo o arquivo {strNomeArq}...")
    fd = open(strNomeArq, 'rb')
    conteudo_arq = fd.read(4096)
    print(f"Conteúdo lido: {conteudo_arq[:50]}...")
    while conteudo_arq != b'':
        print(f'Enviando {len(conteudo_arq)} bytes ...')
        sock.sendto(conteudo_arq, addr)
        conteudo_arq = fd.read(4096)

    fd.close()

sock.close()