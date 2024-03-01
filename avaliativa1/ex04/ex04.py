from funcoes import *

try:
  palavras = lerArquivo()
  palavraSorteada = sortearPalavra(palavras)
  palavraSorteada_string = ''.join(palavraSorteada)
  tentativas = 1

  print(f'A palavra tem {len(palavraSorteada)} letras')

  while True:
      chute = input('Digite uma palavra entre 5 e 8 letras: ').lower()

      if any(char.isdigit() for char in chute):
          print("Entrada inválida. Digite apenas letras.")
          continue 

      if (not (5 <= len(chute)) <= 8) or (len(chute) > len(palavraSorteada)):
          print(f'A palavra tem {len(palavraSorteada)} letras')
          continue

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
          break

      tentativas += 1

      if tentativas == 6:
          print(f'Você perdeu, acabou as suas tentativas :( \n A palavra secreta era {palavraSorteada_string}')
          break


except Exception as e:
    print(f"Erro geral: {e}")
