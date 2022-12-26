class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano Invalido")

try:
    cliente_1 = Cliente("Denilson", "test@test.com", "basic")
    print(cliente_1.nome)
    cliente_2 = Cliente("Miausculo", "test@test.com", "premium")
    print(cliente_2.nome)
    cliente_3 = Cliente("Pythonman", "test@test.com", "full hackado")
    print(cliente_3.nome)
except Exception as e:
    print(e)
