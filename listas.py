lista = [1, 2, 3]
lista.append("Neto")
lista.append(True)
lista.remove(1)  # exclui pelo valor
del lista[0]     # exclui pelo indice
print("tamanho da lista é", len(lista))
for i in range(len(lista)):
    print("valor de i", i)
    print("valor do indice i", lista[i])

for i in lista:
    print("o valor de i é", i)
