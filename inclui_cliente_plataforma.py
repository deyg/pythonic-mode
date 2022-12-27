from plataforma_streams import Cliente

try:
    cliente_1 = Cliente("Denilson", "test@test.com", "basic")
    print(cliente_1.nome)
    cliente_2 = Cliente("Miausculo", "test@test.com", "premium")
    print(cliente_2.nome)
    cliente_3 = Cliente("Pythonman", "test@test.com", "full hackado")
    print(cliente_3.nome)
except Exception as e:
    print(e)