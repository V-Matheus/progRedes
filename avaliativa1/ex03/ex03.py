import hashlib, struct, time

def findNonce(dataToHash, bitsToBeZero):

  start_time = time.time()
  nonce = 0

  for nonce in range(2**32):

        data = struct.pack('<Q', nonce) + dataToHash

        hash_result = hashlib.sha256(data).digest()

        if int.from_bytes(hash_result[:bitsToBeZero // 8], byteorder='big') == 0:
            end_time = time.time()
            tempo = end_time - start_time
            return nonce, tempo
        
        nonce += 1

  return None, None

transacoes = input('Digite um texto para validação: ').encode('utf-8')
bitsZero = int(input('Quantidade de Bits 0: '))

isNonce, intTempo = findNonce(transacoes, bitsZero)

if isNonce:
  print(isNonce, intTempo)

else:
  print('Não foi encontrado NONCE...')