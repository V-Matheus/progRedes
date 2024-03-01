from funcoes import *

arquivo = input('Digite o nome do arquivo: ')

palavras = lerArquivo(arquivo)
print(sortearPalavra(palavras))