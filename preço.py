preço = float(input("Qual o preço por unidade:"))
quantidade = int(input("Quantas unidades:"))
pago = float(input("Qual valor pago:"))

#Cálculo do custo total
ct = preço*quantidade

# Cálculo do troco
troco = pago - ct

#Exibição do resultado

print(f"Quantidade de unidades comprados:{quantidade}")
print(f"Custo total do intens:{ct}")
print(f"Troco:{troco}")