import sys
import os

while True:
    try:
      quantidadeDeItens = int(input('Digite a quantidade de itens: '))
      valorMinimo = int(input('Digite o valor minimo: '))
      valorMaximo = int(input('Digite o valor máximo: '))
      if quantidadeDeItens < 0 or valorMinimo < 0 or valorMaximo < 0:
          print("Digite um valor válido")
          continue
      else:
        break
    except ValueError:
      print("\nERROR: O valor informado precisa ser inteiro de base 10!")
      continue
    except Exception as typeError:
      print(f"\nERROR: {typeError}")

def  gerar_lista( quantidade = None,  valor_minimo = None, valor_maximo =None):
  try:

    quantidade = int(quantidade)
    valor_minimo = int(valor_minimo)
    valor_maximo = int(valor_maximo)

    listaGeradaCorretamente = True
    lista = None

    if valor_minimo > valor_maximo:
      print("O valor mínimo não pode ser maior que o valor máximo")
      listaGeradaCorretamente = False
      return listaGeradaCorretamente, lista

    if quantidade <= 0 or valor_minimo < 0 or valor_maximo < 0:
      raise ValueError("Todos os valores devem ser inteiros positivos")

    if quantidade is None or valor_minimo is None or valor_maximo is None:
      raise ValueError("Todos os campos devem ser preenchidos")

    if listaGeradaCorretamente:
      periodo = valor_maximo - valor_minimo + 1
      lista = [itens for itens in range(valor_minimo, valor_maximo + 1)] * (quantidade + periodo // periodo)
      lista = lista[:quantidade]
      return listaGeradaCorretamente, lista

  except ValueError as valueError:
    print(f"\nERROR: {valueError}")
    listaGeradaCorretamente = False
    sys.exit()

  except TypeError as typeError:
    print(f"\nERROR: {typeError}")
    listaGeradaCorretamente = False
    sys.exit()

  except Exception as exceptionError:
    print(f"\nERROR: {exceptionError}") 
    listaGeradaCorretamente = False
    sys.exit()

def salvar_lista(nome_lista, nome_arquivo):
    try:
        diretorio_atual = os.path.dirname(os.path.realpath(__file__))
        caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)

        with open(caminho_arquivo, 'w') as arquivo:
            for item in nome_lista:
                arquivo.write(str(item) + '\n')
        print('Arquivo salvo com sucesso')
    except Exception as e:
        print(f"\nERROR ao salvar lista: {e}")

listaGeradaCorretamente, lista = gerar_lista(quantidadeDeItens, valorMinimo, valorMaximo)
resultado = salvar_lista(lista, 'minha_lista.txt')



