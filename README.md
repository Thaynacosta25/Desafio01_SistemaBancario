# sistema-bancario
menu = """
=============== MENU ================
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair 
=====================================

=> """ 

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(f" {menu} Escolha uma opção: ")
    
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
    
        if valor > 0:
         saldo += valor 
         extrato += f"Depósito: R$ {valor: .2f}\n"
         print(f"\n Depósito de R$ {valor:.2f} realizado!")
    
        else: 
           print("Valor inválido!")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))

        if valor <= 0:
           print("Valor inválido!")
        elif valor > saldo:
           print("Saldo insuficiente!")
        elif valor > limite:
           print(f"O limite máximo por saque é R$ {limite: .2f}\n")
        elif numero_saques >= LIMITE_SAQUES:
           print("Número máximo de saques diarios atingido!") 

        else:
           saldo -= valor
           extrato += f"Saque: R$ {valor: .2f}\n"
           numero_saques += 1
           print(f"\n Saque de R$ {valor:.2f} realizado! ")

    elif opcao == "3":
        print("\n======== EXTRATO ========")
        if extrato == "" :
           print("Não foram realizadas movimentações. ")
        else:
             print(extrato)
        print(f"Saldo atual R$ {saldo:.2f}")
        print("===========================\n")

    elif opcao == "0":
        print("Obrigado por usar nosso banco. Até mais!")
        break
    else: 
         print("Opção inválida. Tente novamente. ")
