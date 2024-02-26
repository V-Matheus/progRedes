import os 

while True:
    try:
        nomeDoArquivo = input('DIgite o nome do arquivo: ')

        caminhoArquivo = os.path.abspath(f'avaliativa1\ex01\{nomeDoArquivo}.txt')
        with open(caminhoArquivo, 'r', encoding='utf-8') as arquivoSelecionado:
            conteudoDoArquivo = arquivoSelecionado.read()
        print(conteudoDoArquivo)

        break

    except TypeError:
        print("\nERROR: Digite um valor válido de arquivo")
        continue
    except FileNotFoundError:
        print(f"\nERROR: O arquivo não foi encontrado")
    except Exception as e:
        print(f"\nERROR: {e}")