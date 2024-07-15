import random
max=10
n =random.randint(1,max)
print("Bem vindo ao jogo de adivinhar um numero!")
print("Adivinhe um numero de 1 para mais")
adivinhar = None
while adivinhar!=n:
    adivinhar = int(input("Você pode tentar:"))
    if adivinhar > n:
        print('Muito alto')
    if adivinhar <n:
        print("Muito baixo")
print("Parabêns, você acertou")    
    

