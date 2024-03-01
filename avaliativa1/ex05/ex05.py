def cifra_xor(file_origem, palavraPasse, file_destino):
    try:
        with open(file_origem, 'rb') as origem_arquivo:
            dados = origem_arquivo.read()

        palavraPasse_bytes = palavraPasse.encode('utf-8')

        dados_criptografados = []

        for i, byte in enumerate(dados):
            indice_palavraPasse = i % len(palavraPasse_bytes)

            byte_criptografado = byte ^ palavraPasse_bytes[indice_palavraPasse]

            dados_criptografados.append(byte_criptografado)

        with open(file_destino, 'xb') as destino_arquivo:
            destino_arquivo.write(bytes(dados_criptografados))

        print("Arquivo criptografado com sucesso!")

    except FileNotFoundError:
        print("Arquivo de origem não encontrado.")
    except FileExistsError:
        print("O arquivo de destino já existe. Escolha um nome diferente.")
    except Exception as e:
        print(f"Erro: {e}")
