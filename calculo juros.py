valor_principal=(float(input("Qual o valor principal(R$)")))
taxa_de_juros=(float(input("Qual a taxa de juros(%)")))
numero_de_anos=(int(input("Quantos anos:")))
 #calcule os juros anuais
juros = valor_principal * (taxa_de_juros/100)*numero_de_anos

#Calcule  o monatante total
montante = valor_principal + juros

print(f"O motante total após {numero_de_anos} anos é R$ {montante}")
print(f"Os juros acumulados nesse periodo são R${juros}")
             