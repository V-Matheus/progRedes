import hashlib, struct, time

def findNonce(dataToHash, bitsToBeZero):

  nonce = None
  tempo = None

  return nonce, tempo


transacoes = input('Digite um texto para validação: ').encode('utf-8')
bitsZero = int(input('Quantidade de Bits 0: '))

isNonce, intTempo = findNonce(transacoes, bitsZero)

if isNonce:
  print(isNonce, intTempo)

else:
  print('Não foi encontrado NONCE...')