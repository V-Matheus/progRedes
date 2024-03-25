def lerCabecalho(nomeArquivo):
    try:
        # Ler o cabeçalho
        with open(nomeArquivo, 'rb') as arquivo:
            # I = Lê 4 bytes do arquivo // H = lê 2 bytes do arquivo // < = Lê do bit menos significativo para o mais significativo
            # Cria uma túpla com os valores desempacotados
          magicNumber = struct.unpack('<I', arquivo.read(4))[0]
          majorVersion, minorVersion = struct.unpack('<HH', arquivo.read(4))
          reserved1 = struct.unpack('<I', arquivo.read(4))[0]
          reserved2 = struct.unpack('<I', arquivo.read(4))[0]
          snapLen = struct.unpack('<I', arquivo.read(4))[0]
          linkType = struct.unpack('<I', arquivo.read(4))[0]

          print("Magic Number:", hex(magicNumber))
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
