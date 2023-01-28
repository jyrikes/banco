import sqlite3
import dataBase as db
import BancoLib as b

s = db.DataBase()

s.insert(90,10,"contaBonificada")
conta = s.retornaConta(90,"contaBonificada")
a =isinstance(conta,b.ContaBonificada)
if a :
    print("ssssss")
s.updateConta(conta)
s.close()

# cursor.execute("""
#                 CREATE TABLE contas (numeroDaConta INTEGER NOT NULL, tipoDaConta VARCHAR(20) NOT NULL, PRIMARY KEY(numeroDaConta))
# """)
# cursor.execute("""
#                     CREATE TABLE contaCorrente (
#                     numeroDaConta INTEGER NOT NULL,
#                     saldo REAL,
#                     FOREIGN KEY(numeroDaConta) REFERENCES contas(numeroDaConta))
# """)
# cursor.execute("""
#                 CREATE TABLE contaPoupanca(
#                     numeroDaConta INTEGER NOT NULL,
#                     saldo REAL,
#                     FOREIGN KEY(numeroDaConta) REFERENCES contas(numeroDaConta))
# """)

# cursor.execute("""
#                 CREATE TABLE contaBonificada(
#                     numeroDaConta INTEGER NOT NULL,
#                     saldo REAL,
#                     bonus REAL,
#                     FOREIGN KEY(numeroDaConta) REFERENCES contas(numeroDaConta))
# """)
# def insert(numeroDaConta, saldo, tipoDaConta):
#     cursor.execute("""INSERT INTO contas VALUES(?,?)""",(numeroDaConta,tipoDaConta))
#     cursor.execute("INSERT INTO "+tipoDaConta+" VALUES (?,?)",(numeroDaConta,saldo))

# insert(3,10,"contaCorrente")
# cursor.execute("""
#                 SELECT numeroDaConta, tipoDaConta , saldo FROM contas LEFT JOIN contaCorrente  USING (numeroDaConta)
# """)
# result = cursor.fetchall()
# print(result)
# def a (i,b):
#     cursor.execute("SELECT c.numeroDaConta, c.tipoDaConta , e.saldo FROM contas AS c LEFT JOIN "+b+" AS e USING (numeroDaConta) WHERE c.numeroDaConta = ?",str(i))
# a(2,"contaCorrente")
