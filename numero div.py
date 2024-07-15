resultados = []

for numero in range(2000, 3201):
    if numero % 7 == 0 and numero % 5 != 0:
        resultados.append(str(numero))

print(','.join(resultados))

