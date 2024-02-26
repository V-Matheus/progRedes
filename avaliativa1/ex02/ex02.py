import os 

while True:
  nomeDoArquivo = input('DIgite o nome do arquivo: ')

  def ler_arquivo(nome_arquivo):
    try:
      caminhoArquivo = os.path.abspath(f'avaliativa1\ex01\{nome_arquivo}.txt')

      with open(caminhoArquivo, 'r', encoding='utf-8') as arquivoSelecionado:
          listaValores = [linha.strip() for linha in arquivoSelecionado]
          return True, listaValores

    except TypeError:
        print("\nERROR: Digite um valor válido de arquivo")
        return False, None

    except FileNotFoundError:
        print(f"\nERROR: O arquivo não foi encontrado")
        return False, None

    except Exception as e:
        print(f"\nERROR: {e}")
        return False, None

  arquivoLidoComSucessso, listaValores = ler_arquivo(nomeDoArquivo)
  
  if arquivoLidoComSucessso:
    print(arquivoLidoComSucessso, listaValores)
    break

def ordena_bubble(listaValores):
  n = len(listaValores)

  for i in range(n):
    for j in range(0, n - i - 1):
      if listaValores[j] > listaValores[j + 1]:
         listaValores[j], listaValores[j + 1] = listaValores[j + 1], listaValores[j]

while True:
  metodoOrdena = input('DIgite o método de ordenação (BUBBLE, INSERTION, SELECTION, QUICK): ')

  def ordena_lista(nome_lista, método_ordena):
    try:
      if método_ordena == 'BUBBLE':
        return ordena_bubble(nome_lista)   

      elif método_ordena == 'INSERTION':
        ordena_insertion()

      elif método_ordena == 'SELECTION':
        ordena_selection()

      elif método_ordena == 'QUICK':
        ordena_quick()

    except Exception as e:
        print(f"\nERROR: {e}")
        return False, None

  ordenacaoFeitaComSucesso, resultadoOrdenacao = ordena_lista(nomeDoArquivo, metodoOrdena)
  
  if ordenacaoFeitaComSucesso:
    print(ordenacaoFeitaComSucesso, resultadoOrdenacao)
    break