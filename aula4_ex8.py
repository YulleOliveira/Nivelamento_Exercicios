resp = 1
while resp == 1 or resp == 2 or resp == 3:
    print("Menu: \n[1]Oi \n[2]Tchau \n[3]Sair")
    resp = int(input("Selecione uma opção: "))
    if resp == 1:
        print("Oi")
    elif resp == 2:
        print("Tchau")
    elif resp == 3:
        print("Saindo...")