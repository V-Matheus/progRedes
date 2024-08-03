import socket, os

# --------------------------------------------------
# Documentação Protocolo HTTP
# https://datatracker.ietf.org/doc/html/rfc2616
# --------------------------------------------------

url_host    = 'www.httpbin.org'
url_image   = '/image/png'

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

image_filename = os.path.basename(url_image)

print(f'Host: {url_host}')
print(f'Path: {url_image}')
print(f'Nome do arquivo da imagem: {image_filename}')

#url_host    = 'ead.ifrn.edu.br'
#url_image   = 'portal/wp-content/uploads/2019/03/4Iwakb0M_400x400.png'

# ead.ifrn.edu.br/portal/wp-content/uploads/2019/03/4Iwakb0M_400x400.png

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

header, image_data = response.split(b'\r\n\r\n', 1)

# Salvar a imagem em um arquivo
with open(image_filename, 'wb') as image_file:
    image_file.write(image_data)

print(f'A imagem foi salva como {image_filename}')

print('-'*50)

sock_img.close()