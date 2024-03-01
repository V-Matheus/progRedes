def cifra_xor(file_origem, palavraPasse, file_destino):
    with open(file_origem, 'rb') as origem_arquivo:
        dados = origem_arquivo.read()

    palavraPasse_bytes = palavraPasse.encode('utf-8')

    dados_criptografados = []


