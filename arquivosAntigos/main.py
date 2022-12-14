
soma = 0  # acumulador das idade
quantidade = 0  # acumulador da quantidade
idade = int(input("digite a idade:"))
while (idade >= 0):
    soma = soma + idade
    quantidade = quantidade + 1
    idade = int(input("digite a idade:"))
else:
    print("fim")
print("a soma das idade é", soma)
print("a quantidade de valores digitados foi", quantidade)
media = soma/quantidade
print("a media é", media)
