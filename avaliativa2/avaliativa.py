from funcoes import *

nomeArquivoTcp = input("Digite o nome do arquivo capturado pelo tcpdump: ")
lerCabecalho(nomeArquivoTcp)

# A) Mostre o conteúdo de cada um dos campos nos headers dos pacotes IP capturados
with open(nomeArquivoTcp, 'rb') as arquivo:
  arquivo.read(24)  # O cabeçalho do arquivo tem 24 bytes de tamanho

  while True:
    try:
      header_length = lerPacoteIp(arquivo)
      arquivo.read(header_length)  # Ler apenas o cabeçalho

    except struct.error:
      break

# B) Em que momento inicia/termina a captura de pacotes?
tempoInicioFim(nomeArquivoTcp) 

# C) Qual o tamanho do maior TCP pacote capturado?
tamanhoMaiorTcp(nomeArquivoTcp)

# d) Há pacotes que não foram salvos nas suas totalidades? Quantos?
verificacaoDePacotesSalvos(nomeArquivoTcp)

# e) Qual o tamanho médio dos pacotes UDP capturados?
tamanhoMedioUdp(nomeArquivoTcp)