import os 

diretorioAtual = os.path.abspath(__file__)

while True:
    try:
        nomeDoArquivo = input('DIgite o nome do arquivo: ')

        diretorioEx01 = os.path.join(diretorioAtual, '..', 'ex01', nomeDoArquivo + '.txt')
        
        with open(diretorioEx01, 'r', encoding='utf-8') as diretorioEx01:
            conteudo_ex01 = arquivo_ex01.read()
        print(conteudo_ex01)

        break

    except TypeError:
        print("\nERROR: Digite um valor válido de arquivo")
        continue
    except FileNotFoundError:
        print(f"\nERROR: O arquivo não foi encontrado")
    except Exception as e:
        print(f"\nERROR: {e}")