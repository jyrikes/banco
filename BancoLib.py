import random


class Conta():
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0

    def deposite(self, valor):
        valor = valor * 0.999
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False


class Poupanca(Conta):

    def render(self):
        self.saldo = self.saldo + self.saldo*0.01

class ContaBonificada(Conta):
    
    def __init__(self,numConta):
        self.bonus = 0
        super().__init__(numConta)
    
    def calculaBonus(self,valor):
        bonus = valor * 0.0001
        self.bonus = self.bonus + bonus

    def deposite(self,valor):
        self.calculaBonus(valor)
        super().deposite(valor)

    def renderBonus(self):
        #poderia usar a função deposite da classe, mas seria descontado o valor 0.1%
        self.saldo = self.saldo + self.bonus
        self.bonus = 0




class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        c = Conta(num)
        self.contas.append(c)
        return num

    def criarPoupanca(self):
        num = random.randint(0, 1000)
        p = Poupanca(num)
        self.contas.append(p)
        return num

    def criarContaBonificada(self):
        num = random.randint(0, 1000)
        conta_bonificada = ContaBonificada(num)
        self.contas.append(conta_bonificada)
        return num

    def criarContas(self,opcao):
        if opcao == 1:
            numConta = self.criarConta()
            return numConta
        elif opcao == 2:
            numConta = self.criarPoupanca()
            return numConta
        elif opcao == 3:
            numConta = self.criarContaBonificada()
            return numConta
        else:
            return -1
        
        
        
    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.saldo
        return -1

    def depositar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                conta.deposite(valor)

    def sacar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.sacar(valor)

    def renderPoupanca(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Poupanca):
                i.render()
                return True
        return False
    
    def bonificar(self,numConta):
      for i in self.contas:
          if i.numero == numConta and isinstance(i, ContaBonificada):
              i.renderBonus()
              return True
      return False
    
    def buscarConta(self,numConta):
      for conta in self.contas:
        if conta.numero == numConta:
          return True
      else:
        return False
      
      
