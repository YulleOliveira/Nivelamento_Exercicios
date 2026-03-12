lista = []
print(lista)
resp = "s"
while resp == "s":
    resp = int(input('''Deseja:
                [1] Adicionar itens
                [2] Remover itens
                \n'''))
    if resp == 1:
        tipo_item = int(input('''Tipo de item que deseja adicionar: 
            [1] Palavra
            [2] Número 
            '''))
        if tipo_item == 1:
            item = input("Insira um item: ")
            indice = int(input("Escolha o índice: "))
            lista.insert(indice, item)
        if tipo_item == 2:
            item = float(input("Insira um número: "))
            item2 = int(item)
            indice = int(input("Escolha o índice:"))
            lista.insert(indice, item2)
        print(lista,"\n")
        resp = input("Deseja continuar? [s/n] \n")
    elif resp == 2:
        tipo_item = int(input('''Tipo de item que deseja remover: 
            [1] Palavra
            [2] Número 
            '''))
        if tipo_item == 1:
            item = input("Item que deseja remover: ")
            lista.remove(item)
        if tipo_item == 2:
            item = float(input("Número que deseja remover: "))
            item2 = int(item)
            lista.remove(item)
        print(lista,"\n")
        resp = input("Deseja continuar? [s/n] \n")