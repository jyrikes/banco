import random
import dataBase as db
dados = db.DataBase()



class Banco():

    def __init__(self, nome):
        self.nome = nome
        self.contas =[]
        


    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        conta = db.Conta(num)
        if dados.insertConta(conta):
            return num

    def criarPoupanca(self):
        num = random.randint(0, 1000)
        p = db.Poupanca(num)
        if dados.insertConta(p):
            return num

    def criarContaBonificada(self):
        num = random.randint(0, 1000)
        contaBonificada = db.ContaBonificada(num)
        if dados.insertConta(contaBonificada):
            return num

    def criarContas(self,opcao):
        if opcao == "contaCorrente":
            numConta = self.criarConta()
            return numConta
        elif opcao == "contaPoupanca":
            numConta = self.criarPoupanca()
            return numConta
        elif opcao == "contaBonificada":
            numConta = self.criarContaBonificada()
            return numConta
        else:
            return -1
        
        
        
    def consultaSaldo(self, numConta,tipoDaConta):
        try:
            return dados.retornaSaldo(numConta,tipoDaConta)
        except:
            return -1

    def depositar(self, numConta, valor,tipoDaConta):
        conta = dados.retornaConta(numConta,tipoDaConta)
        return conta.deposite(valor,conta)

    def sacar(self, numConta, valor, tipoDaConta):
        conta = dados.retornaConta(numConta,tipoDaConta)
        return conta.sacar(valor,conta)

    def renderPoupanca(self, numConta,tipoDaConta):
        
        conta = dados.retornaConta(numConta,tipoDaConta)
        if isinstance(conta,db.Poupanca):
            conta.render(conta)
            return True
        else:
            return False
                

    
    def bonificar(self,numConta):
      for i in self.contas:
          if i.numero == numConta and isinstance(i, db.ContaBonificada):
              i.renderBonus()
              return True
      return False
    
    def buscarConta(self,numConta,tipoDaConta):
      for conta in self.contas:
        if conta.numero == numConta:
          return True
      else:
        return False
      
banco = Banco("gg")
num = banco.criarContas("contaBonificada")
saldo = banco.consultaSaldo(355,"contaBonificada")
print(num,saldo)
banco.depositar(355,20,"contaBonificada")
saldo = banco.consultaSaldo(355,"contaBonificada")
print(num,saldo)
banco.sacar(355,10,"contaBonificada")
saldo = banco.consultaSaldo(355,"contaBonificada")
print(num,saldo)