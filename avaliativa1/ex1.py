while True:
    try:
        valor1 = int(input('Digite o valor 1:'))
        valor2 = int(input('Digite o valor 2:'))
        valor3 = int(input('Digite o valor 3:'))
        if valor1 < 0 or valor2 < 0 or valor3 < 0:
            print("Digite um valor válido")
            continue
        else:
            break
    except ValueError:
        print("\nERROR: O valor informado precisa ser inteiro de base 10!")
        continue
    except Exception as typeError:
        print(f"\nERROR: {typeError}")

print(valor1, valor2, valor3)