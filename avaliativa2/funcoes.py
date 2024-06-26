import struct

def lerCabecalho(nomeArquivo):
    cabecalho = {}
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

            # Adiciona as informações do cabeçalho ao dicionário
            cabecalho["Magic Number"] = hex(magicNumber)
            cabecalho["Major Version"] = majorVersion
            cabecalho["Minor Version"] = minorVersion
            cabecalho["Reserved1"] = reserved1
            cabecalho["Reserved2"] = reserved2
            cabecalho["SnapLen"] = snapLen
            cabecalho["FCS Link Type"] = linkType

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    
    return cabecalho


def lerPacoteIp(nomeArquivo):
    cabecalhoIp = {}
    # Lendo o cabeçalho do pacote IP
    ipHeader = nomeArquivo.read(20)  # O cabeçalho do pacote IP tem 20 bytes de tamanho

    if len(ipHeader) < 20:
        print("Cabeçalho IP com tamanho insuficiente.")
        return None

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

    cabecalhoIp["nVersão"] = version
    cabecalhoIp["Comprimento do Cabeçalho"] = headerLength
    cabecalhoIp["Tipo de Serviço"] = tipoServico
    cabecalhoIp["Comprimento Total"] = totalLength
    cabecalhoIp["Identificação"] = identificacao
    cabecalhoIp["Flags"] = flags
    cabecalhoIp["Fragment Offset"] = fragmentOffset
    cabecalhoIp["Time To Live"] = timeToLive
    cabecalhoIp["Protocolo"] = protocol
    cabecalhoIp["Checksum"] = checksum
    cabecalhoIp["Endereço de Origem"] = origemIp
    cabecalhoIp["Endereço de Destino"] = destinoIp

    return cabecalhoIp

def tempoInicioFim(nomeArquivo):
    with open(nomeArquivo, 'rb') as arquivo:
        primeiroTimestamp = None
        ultimoTimestamp = None

        while True:
            ipHeader = arquivo.read(20)

            if not ipHeader: 
                break

            if len(ipHeader) >= 8:
                segundos, microssegundos = struct.unpack('!II', ipHeader[:8])
            else:
                print("Final dos pacotes")

            # Combinar segundos e microssegundos para formar o timestamp completo
            timestamp = segundos + microssegundos / 1000000.0

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
    contagem = 0
    with open(nomeArquivo, 'rb') as arquivo:
        while contagem < 20:
            try:
                proximoProtocolo = arquivo.read(1)  # Lendo o próximo byte
                if proximoProtocolo == b'\x06':     # Se for 6, significa que o próximo protocolo é TCP
                    tamanhoTcp = struct.unpack('!H', arquivo.read(2))[0]
                    if tamanhoTcp > maiorTamanhoTcp:
                        maiorTamanhoTcp = tamanhoTcp
                    contagem += 1  # Incrementa a contagem apenas se encontrarmos um pacote TCP
            except struct.error:
                break

    print("\nMaior tamanho TCP: ", maiorTamanhoTcp)

def verificacaoDePacotesSalvos(nomeArquivo):
    totalPacotes = 0
    pacotesIncompletos = 0

    with open(nomeArquivo, 'rb') as arquivo:
        while totalPacotes < 20:
            try:
                cabecalhoIp = lerPacoteIp(arquivo)  # Ler o cabeçalho do pacote IP
                arquivo.read(cabecalhoIp['Comprimento do Cabeçalho'])
                proximoProtocolo = arquivo.read(1)
                # Se for 17, significa que o próximo protocolo é UDP
                if proximoProtocolo == b'\x11':
                    # Lendo o campo que contém o tamanho do pacote capturado
                    capturedLength = struct.unpack('<I', arquivo.read(4))[0]
                    # Lendo o campo que contém o tamanho original do pacote
                    original_length = struct.unpack('<I', arquivo.read(4))[0]
                    totalPacotes += 1
                    if capturedLength < original_length:
                        pacotesIncompletos += 1
            except struct.error:
                break

    print("\nNúmero de pacotes incompletos:", pacotesIncompletos)

def tamanhoMedioUdp(nomeArquivo):
    totalPacotesUdp = 0
    tamanhoTotalUdp = 0

    with open(nomeArquivo, 'rb') as arquivo:
        while totalPacotesUdp < 20:
            try:
                proximoProtocolo = arquivo.read(1)
                # Se for 17, significa que o próximo protocolo é UDP
                if proximoProtocolo == b'\x11':
                    # Lendo o campo que contém o tamanho do pacote capturado
                    capturedLength = struct.unpack('<I', arquivo.read(4))[0]
                    totalPacotesUdp += 1
                    tamanhoTotalUdp += capturedLength
            except struct.error:
                break

    if totalPacotesUdp == 0:
        return 0
    else:
        print("\nTamanho médio dos pacotes UDP capturados em bytes: ",tamanhoTotalUdp / totalPacotesUdp)


def calcularMaiorTrafego(nomeArquivo):
    trafegoIp = {}
    contagem = 0
    with open(nomeArquivo, 'rb') as arquivo:
        while contagem < 20:
            try:
                contagem += 1
                proximoProtocolo = arquivo.read(1)
                # Se for 17, significa que o próximo protocolo é UDP
                if proximoProtocolo == b'\x11':
                    # Lendo o campo que contém o endereço IP de origem (12 bytes)
                    ipOrigem = arquivo.read(12)
                    # Lendo o campo que contém o endereço IP de destino (12 bytes)
                    ipDestino = arquivo.read(12)
                    capturedLength = struct.unpack('<I', arquivo.read(4))[0]

                    # Atualizar o dicionário com o tráfego entre os IPs
                    if (ipOrigem, ipDestino) in trafegoIp:
                        trafegoIp[(ipOrigem, ipDestino)] += capturedLength
                    else:
                        trafegoIp[(ipOrigem, ipDestino)] = capturedLength
            except struct.error:
                break

    # Verifica se o dicionário não está vazio antes de tentar encontrar o maior tráfego
    if trafegoIp:
        maiorTrafego = max(trafegoIp, key=trafegoIp.get)
        print("\nPar de IPs com maior tráfego:", maiorTrafego)
    else:
        print("\nNão há tráfego registrado entre os IPs.")


def contarIpsInteragidos(nomeArquivo, ipInterface):
    ipsInteragidos = set()
    contagem = 0 
    with open(nomeArquivo, 'rb') as arquivo:
        while contagem < 20:
            try:
                contagem += 1
                proximoProtocolo = arquivo.read(1)
                if proximoProtocolo == b'\x11':
                    ipOrigem = arquivo.read(12)
                    ipDestino = arquivo.read(12)

                    # Verificar se o IP da interface capturada é igual ao IP de origem ou destino
                    if ipOrigem == ipInterface:
                        ipsInteragidos.add(ipDestino)
                    elif ipDestino == ipInterface:
                        ipsInteragidos.add(ipOrigem)

            except struct.error:
                break

    print("Número de outros IPs com os quais o IP da interface capturada interagiu:", len(ipsInteragidos))
