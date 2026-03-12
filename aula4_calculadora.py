print('''  
      =============================
      |        CALCULADORA        |
      |                           |
      | [1] Soma                  |
      | [2] Subtração             |
      | [3] Multiplicação         |
      | [4] Divisão               |
      | [5] Exponenciação         |
      | [6] Raiz                  |
      | [7] Função afim           |
      | [8] Função quadrática     |
      | [9] Fibonacci             |
      | [10] Fatorial             |
      |                           |
      =============================
''')
resp = "s"
opc = int(input("Selecione uma opção: "))
if opc == 1:
    print("SOMA")
    print(" ")
    while resp == "s":
        n1 = float(input("Digite o 1º número: "))  
        n2 = float(input(f"Digite o 2º número: {n1} + " ))
        print(f"{n1} + {n2} = ", n1 + n2)
        resp = input("Deseja continuar? [s/n] ")  
        print(" ")
elif opc == 2:
    print("SUBTRAÇÃO")
    print(" ")
    while resp == "s":
        n1 = float(input("Digite o 1º número: "))
        n2 = float(input(f"Digite o 2º número: {n1} - "))
        print(f"{n1} - {n2} = ", n1 - n2)
        resp = input("Deseja continuar:? [s/n] ")
        print(" ")
elif opc == 3:
    print("MULTIPLICAÇÃO")
    print(" ")
    while resp == "s":
        n1 = float(input("Digite o 1º número: "))
        n2 = float(input(f"Digite o 2º número: {n1} x "))
        mult = n1 * n2
        print(f"{n1} x {n2} = ", mult)
        resp = input("Deseja continuar:? [s/n] ")
        print(" ")
    