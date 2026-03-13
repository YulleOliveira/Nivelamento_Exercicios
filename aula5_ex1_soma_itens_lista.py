lista = []
print("Crie uma lista de números: \n")
soma = 0
resp = "s"
while resp == "s":
    n = int(input("Digite um número: "))
    lista.append(n)
    print("Lista criada: ", lista)
    resp = input("Deseja continuar? [s/n] \n")
for i in lista:
    soma += i
print(" ")
print("Lista final: ", lista)
print("Soma de todos os números: ", soma)
