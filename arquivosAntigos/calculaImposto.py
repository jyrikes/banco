def valorPagamento(valor, dias):
    if dias == 0:
        return valor
    else:
        valorPago = valor + valor * 0.03
        for i in range(dias):
            valorPago = valorPago + valorPago * 0.001
        return valorPago


valorTotal = 0  # acumulador pagamentos
quantidade = 0  # acumulador da quantidade
valor = float(input("digite o valor da conta:"))
dias = float(input("digite a quatidade de dias:"))
while(valor > 0):
    valorApagar = valorPagamento(valor, dias)
    print("o valor a ser pago é", valorApagar)
    valorTotal = valorTotal + valorApagar
    quantidade = quantidade + 1
    valor = float(input("digite o valor da conta:"))
    dias = float(input("digite a quatidade de dias:"))

print("relatório do dia")
print("foi pago no total", valorTotal)
print("e houve", quantidade, "pagamentos")
