import sys

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

resultado, lista = gerar_lista(quantidadeDeItens, valorMinimo, valorMaximo)

print(resultado)
print(lista)


