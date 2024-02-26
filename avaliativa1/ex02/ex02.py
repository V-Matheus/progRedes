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

