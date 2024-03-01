from funcoes import *

palavras = lerArquivo()
palavraSorteada = sortearPalavra(palavras)
palavraSorteada_string = ''.join(palavraSorteada)
tentativas = 1

while True:

  chute = input('Digite uma palavra entre 5 e 8 letras: ').lower()

  print(f'A palvra tem {len(palavraSorteada)} letras')
  print(f'Você tem {6 - tentativas} tentativas restantes')

  for index, letra in enumerate(chute):
    if letra in palavraSorteada:
      if palavraSorteada[index] == letra:
        print(f'\033[93m{letra}\033[0m', end=' ')
      else:
        print(f'\033[92m{letra}\033[0m', end=' ')
    else:
      print(f'\033[1;31m{letra}\033[0m', end=' ')
  print('')

  if chute == palavraSorteada_string:
    print(f'Parabéns você ganhou :) \n Você encontrou a palavra com {tentativas} tentativa(s)')

  tentativas += 1

  if tentativas == 6:
    print(f'Você perdeu, acabou as suas tentativas :( \n A palavra secreta era {palavraSorteada_string}')
    break
