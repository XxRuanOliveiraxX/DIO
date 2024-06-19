import os
import time

op = 10
nome = input("Informe o seu nome: ")
os.system('cls')
print("----------------------------------------")
print("Olá {}, Bem vindo(a) de volta.".format(nome.title().strip()))
print("----------------------------------------")
time.sleep(2)
os.system('cls')

while op != 0:

    valor = 0
    Extrato = 1200
    
    print("----------------------------------------")
    print("(0) SAIR")
    print("(1) SAQUE")
    print("(2) DEPOSITO")
    print("(3) EXTRATO")
    print("----------------------------------------")
    op = int(input("Deseja fazer qual tipo de movimentação bancária: "))
    
    for i in range(4):
        while i != 3 and "n":
            if op == 1:
                os.system('cls')
                valor = int(input("Informe a quantia de Saque: R$ "))
                if valor > Extrato:
                    print("Valor de saque maior que o Extrato, tente novamente!")
                else:
                    Extrato -= valor
                    os.system('cls')
                    print("Saque feito\nAgora o seu Extrato é de ",Extrato)
                    i = str(input("""Deseja fazer outro saque? 
                          [s] [n]:"""))

            elif op == 2:
                os.system('cls')
                valor = int(input("Informe a quantia de deposito: R$ "))
            if valor > 0:

                Extrato += valor
                os.system('cls')
                print("Deposito efetuado\nSeu Extrato é de R$",Extrato)
            
        else:
            print("Valor de deposito invalido.")
            print("Retornando ao menu.")
            time.sleep(2)
            os.system('cls')

    ##elif op == 3:
       # os.system('cls')
        #print("O seu Extrato atual é de R$",Extrato)
    



