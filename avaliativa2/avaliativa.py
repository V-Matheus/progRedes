from funcoes import *

nomeArquivoTcp = input("Digite o nome do arquivo capturado pelo tcpdump: ")
lerCabecalho(nomeArquivoTcp)

with open(nomeArquivoTcp, 'rb') as arquivo:
  arquivo.read(24)  # O cabeçalho do arquivo tem 24 bytes de tamanho

  while True:
    try:
      header_length = ler_pacote_ip(arquivo)
      arquivo.read(header_length)  # Ler apenas o cabeçalho

    except struct.error:
      break