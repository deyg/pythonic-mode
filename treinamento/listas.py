minha_lista = [1, 2, 3]
print("minha_lista:", minha_lista)

tamanho = len(minha_lista)
print("minha_lista.len():", tamanho)

posicao_1 = minha_lista[1]
print("minha_lista[1]:", posicao_1)

posicao_menos_1 = minha_lista[-1]
print("minha_lista[-1]:", posicao_menos_1)

minha_lista.insert(2,6)
print("minha_lista.insert(2,6):", minha_lista)

minha_lista.append(7)
print("minha_lista.append(7):", minha_lista)

minha_lista.sort()
print("minha_lista.sort():", minha_lista)

minha_lista.reverse()
print("minha_lista.reverse():", minha_lista)

minha_lista.remove(2)
print("minha_lista.remove(2):", minha_lista)

indice = minha_lista.index(7)
print("minha_lista.index(7):", indice)

maximo = max(minha_lista)
print("max(minha_lista):", maximo)

minimo = min(minha_lista)
print("min(minha_lista):", minimo)

nova_lista = minha_lista + minha_lista
print("minha_lista + minha_lista:", nova_lista)

#percorrer uma lista
print("\nfor valor in minha_lista - lista:", minha_lista)
for valor in minha_lista:
    print("...valor:", valor)
