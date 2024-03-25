from funcoes import *

while True:
  nomeArquivoTcp = input("Digite o nome do arquivo capturado pelo tcpdump: ")
  conteudoArquivo = lerArquivo(nomeArquivoTcp)
  if conteudoArquivo:
    break

