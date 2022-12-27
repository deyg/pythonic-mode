clientes = []
cliente = "_"


def adiciona_cliente(nome):
        clientes.append(nome)


def cliente_valido(cliente):
    if cliente != "":
        return True


def apresenta_clientes(clientes):
        print(clientes)


def entrada_clientes():
    global cliente
    while cliente != "":
        cliente = input("Digite o nome do cliente: ")
        if cliente_valido(cliente):
            adiciona_cliente(cliente)
            apresenta_clientes(clientes)


entrada_clientes()
