class Contador:


    def __init__(self, valor, incremento):
        self.valor = valor
        self.incremento = incremento

    def incrementar(self):
        self.valor += self.incremento


def classe_contador_teste_drive():
    contador_a = Contador(100, 2)

    for i in range(4):
        contador_a.incrementar()
        print(f"Contando {i}: {contador_a.valor}")


classe_contador_teste_drive()
