def lerCabecalho(nomeArquivo):
    try:
        # Ler o cabeçalho
        with open(nomeArquivo, 'rb') as arquivo:
            # I = Lê 4 bytes do arquivo // H = lê 2 bytes do arquivo // B = 2 Byte // < = Lê do bit menos significativo para o mais significativo
            # Cria uma túpla com os valores desempacotados
          magicNumber = struct.unpack('<I', arquivo.read(4))[0]
          majorVersion, minorVersion = struct.unpack('<HH', arquivo.read(4))
          reserved1 = struct.unpack('<I', arquivo.read(4))[0]
          reserved2 = struct.unpack('<I', arquivo.read(4))[0]
          snapLen = struct.unpack('<I', arquivo.read(4))[0]
          linkType = struct.unpack('<I', arquivo.read(4))[0]

          print("\nMagic Number:", hex(magicNumber))
          print("Major Version:", majorVersion)
          print("Minor Version:", minorVersion)
          print("Reserved1:", reserved1)
          print("Reserved2:", reserved2)
          print("SnapLen:", snapLen)
          print("FCS Link Type:", linkType)

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    except Exception as e:
        print("Erro ao ler o arquivo:", e)
        return None

def lerPacoteIp(nomeArquivo):
    # Lendo o cabeçalho do pacote IP
    ipHeader = nomeArquivo.read(20)  # O cabeçalho do pacote IP tem 20 bytes de tamanho

    # Interpretando os campos do cabeçalho IP
    versionHeaderLenght = ipHeader[0]  # Primeiro byte contém a versão do IP e o comprimento do cabeçalho
    version = versionHeaderLenght >> 4  # Pega os primeiros 4 bits
    headerLength = (versionHeaderLenght & 0x0F) * 4  # Pega os 4 últimos bits e multiplica por 4 que é o valor em bytes do restante do cabeçalho

    tipoServico, totalLength, identificacao, flagsFragOffset = struct.unpack('!BBHH', ipHeader[1:7])
    flags = (flagsFragOffset & 0xE000) >> 13 # Pega os 13 bits contanto da direita para a esquerda
    fragmentOffset = flagsFragOffset & 0x1FFF # Pega o restante dos bits
    timeToLive, protocol, checksum = struct.unpack('!BBH', ipHeader[8:12])
    origem, destino = struct.unpack('!4s4s', ipHeader[12:20])

    # Convertendo os endereços IP de binário para formato legível
    origemIp = '.'.join(map(str, origem))
    destinoIp = '.'.join(map(str, destino))

    print("\nVersão:", version)
    print("Comprimento do Cabeçalho:", headerLength)
    print("Tipo de Serviço:", tipoServico)
    print("Comprimento Total:", totalLength)
    print("Identificação:", identificacao)
    print("Flags:", flags)
    print("Fragment Offset:", fragmentOffset)
    print("Time To Live:", timeToLive)
    print("Protocolo:", protocol)
    print("Checksum:", checksum)
    print("Endereço de Origem:", origemIp)
    print("Endereço de Destino:", destinoIp)

    return headerLength

def tempoInicioFim(nomeArquivo):
    with open(nomeArquivo, 'rb') as arquivo:
        primeiroTimestamp = None
        ultimoTimestamp = None

    while True:
        ipHeader = arquivo.read(20)

        if not ipHeader: 
            break

        # Ler o timestamp do pacote (os primeiros 8 bytes do cabeçalho IP)
        timestamp = struct.unpack('!Q', ipHeader[:8])[0]

        # Depois de percorrer todos os bytes vai pegar o valor mínimo (primeiroTimestamp) e o valor máximo (ultimoTimestamp)
        if primeiroTimestamp is None:
            primeiroTimestamp = timestamp
        else:
            primeiroTimestamp = min(primeiroTimestamp, timestamp)

        if ultimoTimestamp is None:
            ultimoTimestamp = timestamp
        else:
            ultimoTimestamp = max(ultimoTimestamp, timestamp)


    print("\nTempo de início da captura:", primeiroTimestamp)
    print("Tempo de término da captura:", ultimoTimestamp)

def tamanhoMaiorTcp(nomeArquivo):
    maiorTamanhoTcp = 0

    with open(nomeArquivo, 'rb') as arquivo:
        while True:
            try:
                headerLength = lerPacoteIp(arquivo)  # Ler o cabeçalho do pacote IP
                arquivo.read(headerLength)
               
                proximoProtocolo = arquivo.read(1)  # Lendo o próximo byte
 
                if proximoProtocolo == b'\x06':     # Se for 6, significa que o próximo protocolo é TCP
                    tamanhoTcp = struct.unpack('!H', arquivo.read(2))[0]
                    if tamanhoTcp > maiorTamanhoTcp:
                        maiorTamanhoTcp = tamanhoTcp
            except struct.error:
                break

    print(maiorTamanhoTcp)

