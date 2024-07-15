a = int(input("Digite primeiro número A: "))
b = int(input("Digite primeiro número B: "))
c = int(input("Digite primeiro número C: "))
if a > b and a > c:
    print(a)
else:
    if b > c:
        print(b)
    else:
        print(c)