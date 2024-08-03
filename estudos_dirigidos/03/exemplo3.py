import socket, os

# --------------------------------------------------
# Documentação Protocolo HTTP
# https://datatracker.ietf.org/doc/html/rfc2616

# Exemplo de imagem
# ead.ifrn.edu.br/portal/wp-content/uploads/2019/03/4Iwakb0M_400x400.png
# --------------------------------------------------

def hostECaminho(url):
    if "http://" in url:
        url = url[7:]
    elif "https://" in url:
        url = url[8:]
    
    caminhoIndex = url.find("/")
    if caminhoIndex == -1:
        return url, "/"
    else:
        return url[:caminhoIndex], url[caminhoIndex:]

userURl = input('Informe a URL da imagem: ')

url_host, url_image = hostECaminho(userURl)

nomeImagem = os.path.basename(url_image)
caminho_do_arquivo = os.path.join(os.path.dirname(__file__), nomeImagem)

HOST_PORT   = 80
BUFFER_SIZE = 1024

sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, HOST_PORT))

get_url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
sock_img.sendall(get_url_request.encode())

response = b""
while True:
    data = sock_img.recv(BUFFER_SIZE)
    if not data:
        break
    response += data

header, dataImagem = response.split(b'\r\n\r\n', 1)

headerLinhas = header.decode().split('\r\n')
content_length = 0
for line in headerLinhas:
    if line.startswith('Content-Length:'):
        content_length = int(line.split(': ')[1])
        break

if content_length and len(dataImagem) == content_length:
    with open(caminho_do_arquivo, 'wb') as image_file:
      image_file.write(dataImagem)

    print(f'A imagem foi salva como {nomeImagem}')
else:
  print('Aviso: O tamanho dos dados recebidos não corresponde ao Content-Length indicado. Dowload Cancelado')

sock_img.close()