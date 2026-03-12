x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
e = x**y
print(f"Todos os números entre 0 e {e}:")
for cont in range(0, e+1):
    print(cont)
