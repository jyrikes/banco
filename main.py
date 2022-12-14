from BancoLib import Banco

def contaExiste():
  numConta = int(input("digite o numero da conta:"))
  achouConta = bancoUfrpe.buscarConta(numConta)
  while not achouConta:
    print("A conta não existe")
    numConta = int(input("digite o numero da conta ou -1 para sair:"))
    if numConta == -1:
      break
      
    
  return (numConta,True)

print("Bem-vindo")
bancoUfrpe = Banco("UABJ")
print("Menu")
print("0 - Sair")
print("1 - Criar uma Nova Conta")
print("2 - Consultar Saldo Conta")
print("3 - Depositar na Conta")
print("4 - Sacar na Conta")
print("5 - Render Poupanca")
print("6 - Creditar Bonus")
escolha = int(input("digite a opção desejada:"))
while escolha > 0:
    if escolha == 1:
        # criar uma conta
        print("Criando Conta...")
        print("1 - Conta Corrente")
        print("2 - Conta Poupanca")
        print("3 - Conta Bonificada")
        opcao = int(input("digite o tipo da conta:"))
        numConta = bancoUfrpe.criarContas(opcao)
        while numConta == -1:
             print("Não foi possível criar a conta")
             print("Selecione um tipo de conta válido ou digite 0 para voltar")
             opcao = int(input("digite o tipo da conta:"))
             if opcao == 0:
                break
             numConta = bancoUfrpe.criarContas(opcao)
        if numConta != -1:      
          print("Conta criada:", numConta)
          
    elif escolha == 2:
        print("Consultando Saldo...")
        numConta = int(input("digite o numero da conta:"))
        saldo = bancoUfrpe.consultaSaldo(numConta)
        if saldo != -1:
            print("o saldo da conta", numConta, "é", saldo, "R$")
        else:
            print("Não foi possível depositar: A conta",numConta, "não existe.")
    elif escolha == 3:
       
        print("Depositando Conta...")
        numConta,contaExiste = contaExiste()
        if numConta != -1:
          valor = int(input("digite o valor que deseja depositar:"))
          saldo = bancoUfrpe.depositar(numConta, valor)
          print("Valor Depositado")
        
    elif escolha == 4:
        print("Sacando da Conta...")
        numConta,contaExiste = contaExiste()
        if numConta != -1:
          valor = int(input("digite o valor que deseja sacar:"))
          resp = bancoUfrpe.sacar(numConta, valor)
          if resp:  # significa resp == True
              print("Valor Sacado")
          else:
              print("Saldo Insuficiente")
    elif escolha == 5:
        print("Rendendo Poupanca...")
        numConta = int(input("digite o numero da conta poupanca:"))
        resp = bancoUfrpe.renderPoupanca(numConta)
        if resp:
            print("Poupanca com novo saldo")
        else:
            print("A conta não é poupanca ou não existe")
    elif escolha == 6:
        print("Bonificando na conta...")
        numConta = int(input("digite o numero da conta Bonificada:"))
        bonificado = bancoUfrpe.bonificar(numConta)
        if bonificado:
            print("A bonificação foi creditada")
        else:
            print("A conta não perminte bonificação ou não existe")
    escolha = int(input("digite a opção desejada:"))

