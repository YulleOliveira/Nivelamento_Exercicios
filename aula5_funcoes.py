def conversao(celsius):
    fahrenheit = celsius*1.8 + 32
    return fahrenheit

c = float(input("Informe a temperatura em graus celsius: "))
f = conversao(c)
print(f)

c2 = float(input("Informe a temperatura em graus celsius: "))
f2 = conversao(c2)
print(f2)