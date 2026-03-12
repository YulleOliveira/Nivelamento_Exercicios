soma = 0
for numero in range (2, 51):
    q_divisores = 0
    for divisor in range (1, numero+1):
        if numero%divisor == 0:
            q_divisores += 1
    if q_divisores == 2:
        soma += numero
print("A soma de todos os primos de 1 a 50: ", soma)
