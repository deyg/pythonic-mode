class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = self.plano_valido(plano)

    def plano_valido(self, plano):
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            return plano
        else:
            raise Exception("Plano Invalido")
