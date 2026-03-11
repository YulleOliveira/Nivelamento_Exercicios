n = int(input("Digite um número: "))
f = n
for cont in range(n, 1, -1):
    n *= (cont - 1)
print(f"{f}! = {n}")