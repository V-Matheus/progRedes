import os

def ler_arquivo(nome_arquivo):
    try:
      caminhoArquivo = os.path.abspath(f'avaliativa1\ex01\{nome_arquivo}.txt')

      with open(caminhoArquivo, 'r', encoding='utf-8') as arquivoSelecionado:
          listaValores = [int(linha.strip()) for linha in arquivoSelecionado]
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

    
def ordena_bubble(listaValores):

  n = len(listaValores)

  for i in range(n):
    for j in range(0, n - i - 1):
      if listaValores[j] > listaValores[j + 1]:
         listaValores[j], listaValores[j + 1] = listaValores[j + 1], listaValores[j]
  return True, listaValores

def ordena_selection(listaValores):
    n = len(listaValores)

    for i in range(n):
        # Encontra o índice do menor elemento na parte não ordenada
        indice_minimo = i
        for j in range(i + 1, n):
            if listaValores[j] < listaValores[indice_minimo]:
                indice_minimo = j

        # Troca o menor elemento com o primeiro elemento não ordenado
        listaValores[i], listaValores[indice_minimo] = listaValores[indice_minimo], listaValores[i]

    return True, listaValores

def ordena_insertion(listaValores):
    try:
        # Convertendo para uma lista de números, caso não esteja
        listaValores = [int(valor) for valor in listaValores]

        n = len(listaValores)

        for i in range(1, n):
            chave = listaValores[i]
            j = i - 1
            while j >= 0 and chave < listaValores[j]:
                listaValores[j + 1] = listaValores[j]
                j -= 1
            listaValores[j + 1] = chave

        return True, listaValores

    except Exception as e:
        print(f"\nERROR: {e}")
        return False, None

def ordena_lista(nome_lista, método_ordena):
  try:
    if método_ordena == 'BUBBLE':
      return ordena_bubble(nome_lista)

    elif método_ordena == 'INSERTION':
      return ordena_insertion(nome_lista)

    elif método_ordena == 'SELECTION':
      return ordena_insertion(nome_lista)

    elif método_ordena == 'QUICK':
      print('QUICK')


  except Exception as e:
      print(f"\nERROR: {e}")
      return False, None