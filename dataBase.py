import sqlite3

class DataBase():

    def __init__(self):

        self.dataBase = sqlite3.connect('dataBase.db')
        self.cursor = self.dataBase.cursor()
   

    def insert(self, numeroDaConta,saldo,tipoDaConta):
        
    
        try:
            if tipoDaConta != "contaBonificada":
                self.cursor.execute("""INSERT INTO contas VALUES(?,?)""",(numeroDaConta,tipoDaConta))
                self.cursor.execute("INSERT INTO "+tipoDaConta+" VALUES (?,?)",(numeroDaConta,saldo))
                self.dataBase.commit()
                return True
            else:
                self.cursor.execute("""INSERT INTO contas VALUES(?,?)""",(numeroDaConta,tipoDaConta))
                self.cursor.execute("INSERT INTO "+tipoDaConta+" VALUES (?,?,?)",(numeroDaConta,saldo,0))
                self.dataBase.commit()
                return True
        except:
            return False
        
    def insertConta(self,conta):
        try:
            numeroDaConta = conta.getNumeroDaConta()
            saldo = 0
            tipoDaConta = conta.getTipoDaConta()
            self.insert(numeroDaConta,saldo,tipoDaConta)
            return True
        except:
            return False

    def updateSaldo(self,numeroDaConta,saldo,tipoDaConta):
        try:
            self.cursor.execute("UPDATE " +tipoDaConta+ " SET saldo = ? WHERE numeroDaConta = ?""",(saldo,numeroDaConta))
            self.dataBase.commit()
            return True
        except:
            return False
    def updateBonus(self,numeroDaconta,bonus):
       
        try:
            self.cursor.execute("""UPDATE contaBonificada  SET bonus = ? WHERE numeroDaConta = ?""",(bonus,numeroDaconta))
            self.dataBase.commit()
            return True
        except:
            return False

    def updateConta(self,conta):
        numeroDaConta = conta.getNumeroDaConta()
        saldo = conta.saldo
        tipoDaConta = conta.getTipoDaConta()

        if not isinstance(conta,ContaBonificada):
            self.updateSaldo(numeroDaConta,saldo,tipoDaConta)
        else:
            bonus = conta.bonus
            self.updateSaldo(numeroDaConta,saldo,tipoDaConta)
            self.updateBonus(numeroDaConta,bonus)
            


    def retornaSaldo(self,numeroDaConta,tipoDaConta):
        resultado = self.buscarConta(numeroDaConta,tipoDaConta)
        if resultado is not None:
            return resultado[2]

    

    def show(self):

        self.cursor.execute("""SELECT * FROM contaPoupanca""")
        self.dataBase.commit()
        resul = self.cursor.fetchall()
        print(resul)

    def buscarConta(self,numeroDaConta,tipoDaConta):

        try:
            if tipoDaConta != "contaBonificada":
                self.cursor.execute("""SELECT c.numeroDaConta, c.tipoDaConta , e.saldo
                FROM contas AS c LEFT JOIN """+tipoDaConta+""" AS e USING (numeroDaConta)
                WHERE c.numeroDaConta =""" +str(numeroDaConta))
            else:
                self.cursor.execute("""SELECT c.numeroDaConta, c.tipoDaConta , e.saldo, e.bonus
                FROM contas AS c LEFT JOIN """+tipoDaConta+""" AS e USING (numeroDaConta)
                WHERE c.numeroDaConta =""" +str(numeroDaConta))
            self.dataBase.commit()
            result = self.cursor.fetchone()
            return result
        except:
            return None

    def retornaConta(self,numeroDaConta,tipoDaConta):
        try:
            resul = self.buscarConta(numeroDaConta,tipoDaConta)
            match tipoDaConta:
                case "contaCorrente":
                    conta = Conta(numeroDaConta)
                case "contaPoupanca":
                    conta = Poupanca(numeroDaConta)
                case "contaBonificada":
                    conta = ContaBonificada(numeroDaConta)
                    conta.bonus = resul[3]
                   
            
            conta.saldo = resul[2]
            conta.tipo  = resul[1]
            return conta

        except:
            return None

    
        

    def close(self):
        self.cursor.close()
        self.dataBase.close()

    #preciso salvar a conta
    #preciso buscar a conta 



    def t(self,conta):

        print(conta.sacar(1))

dados = DataBase()

class Conta():
 
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0
        self.tipo = "contaCorrente"

    def deposite(self, valor,conta):
        valor = valor * 0.999
        conta.saldo = conta.saldo + valor
        dados.updateConta(conta)


    def sacar(self, valor,conta):

        if conta.saldo >= valor:
            conta.saldo = conta.saldo - valor
            dados.updateConta(conta)
            return True
        else:
            return False
    def getNumeroDaConta(self):
        return self.numero
    def getTipoDaConta(self):
        return self.tipo
    

class Poupanca(Conta):
    def __init__(self, numConta):
        
        super().__init__(numConta)
        self.tipo = "contaPoupanca"

    def render(self,conta):
        conta.saldo = conta.saldo + conta.saldo*0.01
        dados.updateConta(conta)

class ContaBonificada(Conta):
    
    def __init__(self,numConta):
       
        self.bonus = 0
        super().__init__(numConta)
        self.tipo = "contaBonificada"
    
    def calculaBonus(self,valor,conta):
        bonus = valor * 0.0001
        conta.bonus = conta.bonus + bonus

    def deposite(self,valor,conta):
        self.calculaBonus(valor,conta)
        super().deposite(valor,conta)

    def renderBonus(self):
        #poderia usar a função deposite da classe, mas seria descontado o valor 0.1%
        self.saldo = self.saldo + self.bonus
        self.bonus = 0

