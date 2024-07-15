numero = int(input("Digite um numero:"))
# O resto divisao de qualquer numero por 2 é = 0
# o resto devisao de qualquer numero impar por 2 é = 1
resultado = numero % 2
if resultado == 0:
    print(f"O numero {numero} é par")
else:
    print(f" o resultado {numero} é impar")