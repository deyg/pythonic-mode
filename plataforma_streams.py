class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano Invalido")

cliente_1 = Cliente("Denilson", "test@test.com", "basic")
cliente_2 = Cliente("Denilson", "test@test.com", "premium")

print(cliente_1.nome)
print(cliente_2.nome)
try:
    cliente_3 = Cliente("Denilson", "test@test.com", "full hackado")
except Exception as e:
    print(e)
    