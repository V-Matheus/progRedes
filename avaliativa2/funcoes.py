def lerArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'rb') as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    except Exception as e:
        print("Erro ao ler o arquivo:", e)
        return None
