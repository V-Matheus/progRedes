import os
from funcoes import *
from tabulate import tabulate

nomeArquivoTcp = input("Digite o nome do arquivo capturado pelo tcpdump: ")
diretorioAtual = os.path.dirname(__file__)
caminhoArquivoTcp = os.path.join(diretorioAtual, nomeArquivoTcp)

cabecalho = lerCabecalho(caminhoArquivoTcp)
chavesCabecalho = list(cabecalho.keys())
valoresCabecalho = list(cabecalho.values())
tabelaCabecalho = [(chavesCabecalho, valoresCabecalho) for chavesCabecalho, valoresCabecalho in zip(chavesCabecalho, valoresCabecalho)]

# Imprime a tabela usando o tabulate
print(tabulate(tabelaCabecalho, headers=["Campo", "Valor"], tablefmt="grid"))

# Comente as linhas de código abaixo para evitar tantos arquivos

pacotesLidos = 0
# A) Mostre o conteúdo de cada um dos campos nos headers dos pacotes IP capturados
with open(caminhoArquivoTcp, 'rb') as arquivo:
    while pacotesLidos < 20:
        try:
            cabecalhoIp = lerPacoteIp(arquivo)  # Ler o cabeçalho do pacote IP
            chavesIp = list(cabecalhoIp.keys())
            valoresIp = list(cabecalhoIp.values())
            tabelaIp = [(chavesIp, valoresIp) for chavesIp, valoresIp in zip(chavesIp, valoresIp)]

            # Imprime a tabela usando o tabulate
            print(tabulate(tabelaIp, headers=["Campo", "Valor"], tablefmt="grid"))
            print('-' * 50)
            arquivo.read(cabecalhoIp['Comprimento do Cabeçalho'])  # Ler apenas o cabeçalho
            pacotesLidos += 1  # Incrementa a contagem de pacotes lidos

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