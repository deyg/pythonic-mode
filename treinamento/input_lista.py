clientes = []


def adiciona_cliente(nome):
    clientes.append(nome)


cliente = "_"
while cliente != "":
    cliente = input("Digite o nome do cliente: ")
    if cliente != "":
        adiciona_cliente(cliente)
        print(clientes)
        