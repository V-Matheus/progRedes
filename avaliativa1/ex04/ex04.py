from funcoes import *

palavras = lerArquivo()
# palavraSorteada = sortearPalavra(palavras)
palavraSorteada = list('python')

while True:

  tentativas = 1
  chute = input('Digite uma palavra entre 5 e 8 letras: ').lower()

  print(f'A palvra tem {len(palavraSorteada)} letras')

  for index, letra in enumerate(chute):
    if letra in palavraSorteada:
      if palavraSorteada[index] == letra:
        print(f'\033[93m{letra}\033[0m', end=' ')
      else:
        print(f'\033[92m{letra}\033[0m', end=' ')
    else:
      print(f'\033[1;31m{letra}\033[0m', end=' ')
  print('')
