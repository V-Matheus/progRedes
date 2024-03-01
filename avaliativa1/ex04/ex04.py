from funcoes import *

palavras = lerArquivo()
# palavraSorteada = sortearPalavra(palavras)
palavraSorteada = list('python')

while True:

  tentativas = 1
  chute = input('Digite uma palavra entre 5 e 8 letras: ').lower()

  for index, letra in enumerate(chute):
    if letra in palavraSorteada:
      if palavraSorteada[index] == letra:
        print(f'A letra "{letra}" está correta')
      else:
        print(f'A letra "{letra}" existe, porém não está no local correto')
    else:
      print(f'Não existe a letra "{letra}" na palavra secreta')
  print('')
