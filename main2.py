item = []
mercado = []

for i in range (3):
    item.append(input("Digite o nome do item: "))
    item.append(input("Digite a quantidade: "))
    item.append(input("Digite o valor: "))
    mercado.append(item[:])
    item.clear()
print(mercado)
