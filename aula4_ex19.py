n = int(input("Quantos números da sequência de Fibonacci você deseja visualizar? "))
soma = 0
num1 = 0
num2 = 1
print(num1)
print(num2)
for cont in range(3, n+1):
    soma = num1 + num2
    print(soma)
    num1 = num2
    num2 = soma