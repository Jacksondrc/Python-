num1= int(input("Digite um numero:"))
num2 =int(input("Digite outro numero:"))

#Troca de numeros usando uma variavel temporaria
temp = num1
num1 = num2
num2 = temp

#exebição do resultado
print("Depois da troca:")
print("num1=",num1)
print("num2=",num2)