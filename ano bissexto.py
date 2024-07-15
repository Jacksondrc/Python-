ano  = int(input("Qual o ano:"))
if (ano % 4==0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é ano bissexto")
else:
    print(f"{ano} nao é anos bissexto")
    

# A condiçao (ano % 4==0 and ano % 100 != 0) or (ano % 400 == 0) verifica se o ano é divisivel por 4, mas nao por 100, a menos que tambem seja divisivel por 400