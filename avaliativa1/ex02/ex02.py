from funcoes import *

while True:
  nomeDoArquivo = input('Digite o nome do arquivo: ')

  arquivoLidoComSucessso, valoresLidos = ler_arquivo(nomeDoArquivo)
  
  if arquivoLidoComSucessso:
    print(valoresLidos)
    break

while True:
  metodoOrdena = input('DIgite o método de ordenação (BUBBLE, INSERTION, SELECTION, QUICK): ')

  ordenacaoFeitaComSucesso, resultadoOrdenacao = ordena_lista(valoresLidos, metodoOrdena)
  
  if ordenacaoFeitaComSucesso:
    print(resultadoOrdenacao)
    break