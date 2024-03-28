import os
from funcoes import *

nomeArquivoTcp = input("Digite o nome do arquivo capturado pelo tcpdump: ")
diretorioAtual = os.path.dirname(__file__)
caminhoArquivoTcp = os.path.join(diretorioAtual, nomeArquivoTcp)

lerCabecalho(caminhoArquivoTcp)
pacotesLidos = 0
# A) Mostre o conteúdo de cada um dos campos nos headers dos pacotes IP capturados
with open(caminhoArquivoTcp, 'rb') as arquivo:
    while True:
        try:
            header_length = lerPacoteIp(arquivo)
            arquivo.read(header_length)  # Ler apenas o cabeçalho
            pacotesLidos += 1  # Incrementa a contagem de pacotes lidos
            print("Pacote lido:", pacotesLidos)  # Exibe a contagem de pacotes lidos

        except struct.error:
            print("Fim do arquivo alcançado.")
            break

# B) Em que momento inicia/termina a captura de pacotes?
tempoInicioFim(caminhoArquivoTcp) 

# C) Qual o tamanho do maior TCP pacote capturado?
tamanhoMaiorTcp(caminhoArquivoTcp)

# d) Há pacotes que não foram salvos nas suas totalidades? Quantos?
verificacaoDePacotesSalvos(caminhoArquivoTcp)

# e) Qual o tamanho médio dos pacotes UDP capturados?
tamanhoMedioUdp(caminhoArquivoTcp)

# f) Qual o par de IP com maior tráfego entre eles?
calcularMaiorTrafego(caminhoArquivoTcp)

# g) Com quantos outros IPs o IP da interface capturada interagiu?
ipInterface = '192.168.1.100' # Esse Ip é apenas de teste
contarIpsInteragidos(caminhoArquivoTcp, ipInterface)