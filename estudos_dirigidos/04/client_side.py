import socket

SERVER = '127.0.0.1'
PORT   = 31435

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(20) 
#sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF, 25000)

while True:
    strNomeArq = input('Nome do arquivo a fazer download: ')
    sock.sendto(strNomeArq.encode('utf-8'), (SERVER, PORT))

    try:
        fd = open(strNomeArq, 'wb')
        tam = 0
        while True:
            data, addr = sock.recvfrom(4096)

            if not data: 
                break

            tam += len(data)
            print (f'Recebi {len(data) / tam} bytes')
            fd.write(data)

    except socket.timeout:
        print('Tempo de espera esgotado')
        fd.close()
        break

    finally:
        fd.close()

sock.close()