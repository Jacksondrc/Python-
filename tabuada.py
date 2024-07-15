
'''
num= int(input("Digite um numero para escolher a tabuda:"))
num1 = num *1
num1 = num *2
num1 = num *3
num1 = num *4
print(f"{num}x{1}={num1}"
===============
def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Solicita um número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Chama a função para exibir a tabuada
tabuada(numero)
============
'''
 #Função para exibir a tabuada de um número
def tabuada(numero):
    i = 1
    print(f"Tabuada do {numero}:")
    while i <= 10:
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        i += 1

# Solicita um número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Chama a função para exibir a tabuada
tabuada(numero)