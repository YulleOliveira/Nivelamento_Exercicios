def calcularFatorial(numero):
    for cont in range (num, 1, -1):
        num *= (cont - 1)
    fatorial = num
    return fatorial
num = int(input("Fatorial do número: "))
fatorial = calcularFatorial(num)
print(fatorial)
