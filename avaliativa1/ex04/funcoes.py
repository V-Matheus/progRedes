import os

def lerArquivo(nome_arquivo):
    try:
        caminho_arquivo = os.path.join(os.path.dirname(__file__), nome_arquivo + '.txt')
        with open(caminho_arquivo, 'r') as arquivo:
            palavras = [palavra.strip() for palavra in arquivo.readlines() if 5 <= len(palavra.strip()) <= 8]
        return palavras
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return None