import os
import time
def printf (text):
    print(text, end=" ")
    
#os.system('cls')
#time.sleep(2)

print("------------------------------------------------------------")
nome = input("Informe o seu nome: ")
os.system('cls')
print("------------------------------------------------------------")
print("Olá {}, Bem vindo(a) de volta.".format(nome.title().strip()))
printf("Um momento")

printf(".")
time.sleep(1)
printf(".")
time.sleep(1)
printf(".")

print("")
print("------------------------------------------------------------")
time.sleep(2)
os.system('cls')

saldo = 0
limite = 500
numero_saque = 0
limite_saque = 3
op = 1

while op != 3:
    print("------------------------------------------------------------")
    print("(0) DEPOSITAR")
    print("(1) SACAR")
    print("(2) EXTRATO")
    print("(3) SAIR")
    print("------------------------------------------------------------")
    op = int(input("Deseja fazer qual tipo de movimentação bancária: "))
    os.system('cls')

    if op == 0:
        valor = float(input("Informe a quantia de deposito: R$ "))
        if valor > 0:
            saldo += valor
            time.sleep(2)
            os.system('cls')
            print("Deposito realizado com sucesso.")
        else:
            os.system('cls')
            print("Não foi possivel depositar este valor")
            print("Tente novamente.")


    elif op == 1:
        while numero_saque >= limite_saque:
            print("Você excedeu o limite de saque diario")
            print("Tente novamente amanhã.")
            break

        if saldo > 0:
            while numero_saque < limite_saque:
                numero_saque += 1
                valor = float(input("Informe a quantia de Saque: R$ "))

                if saldo < valor:
                    os.system('cls')
                    print("O valor pedido no saque é maior \nque o valor disponivel no saldo da conta")
                    print("Tente novamente")
                    numero_saque -= 1
                    break

                else:
                    if valor <= 500:
                        saldo -= valor
                        time.sleep(2)
                        os.system('cls')
                        print("Saque realizado com sucesso.")
                        break
                    else:
                        os.system('cls')
                        print("O limite máximo é de R$ 500 por saque")
                        print("Tente novamente.")
                        numero_saque -= 1
                        break

        else:
            print("Você não tem saldo disponivel para saque")
            print("Deposite primeiro.")
                    

    elif op == 2:
        print("Extrato: R$ ",saldo)
        

    elif op == 3:
        os.system('cls')
        print("------------------------------------------------------------")
        print("Agradecemos a preferência, Volte sempre.")
        print("------------------------------------------------------------")
        time.sleep(2)
        break

    else:
        print("Opção inválida. Tente novamente")