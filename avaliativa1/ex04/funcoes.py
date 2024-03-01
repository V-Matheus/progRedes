import os, random

def lerArquivo():
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'palavras.txt')
    with open(caminho_arquivo, 'r') as arquivo:
        palavras = [palavra.strip() for palavra in arquivo.readlines() if 5 <= len(palavra.strip()) <= 8]
    return palavras


def sortearPalavra(listaPalavras):
    return list(listaPalavras[random.randint(1, len(listaPalavras))].lower())
