soma_sal = 0
soma_idade = 0
sal = 0
idade = 0
for cont in range(0, 3):
    sal = float(input("Salário: "))
    soma_sal += sal
    idade = int(input("Idade: "))
    soma_idade += idade
    print(" ")
print("Média dos salários: ", soma_sal/3)
print("Média das idades: ", soma_idade/3)
