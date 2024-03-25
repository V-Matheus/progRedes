def lerArquivo(nomeArquivo):
    try:
        # Ler o cabeçalho
        with open(nomeArquivo, 'rb') as arquivo:
            # I = Lê 4 bytes do arquivo // H = lê 2 bytes do arquivo // < = Lê do bit menos significativo para o mais significativo
            # Cria uma túpla com os valores desempacotados
          magic_number = struct.unpack('<I', arquivo.read(4))[0]
          major_version, minor_version = struct.unpack('<HH', arquivo.read(4))
          reserved1 = struct.unpack('<I', arquivo.read(4))[0]
          reserved2 = struct.unpack('<I', arquivo.read(4))[0]
          snap_len = struct.unpack('<I', arquivo.read(4))[0]
          fcs_link_type = struct.unpack('<I', arquivo.read(4))[0]

          return magic_number, major_version, minor_version, reserved1, reserved2, snap_len, fcs_link_type

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    except Exception as e:
        print("Erro ao ler o arquivo:", e)
        return None
