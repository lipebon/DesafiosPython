
intro = '''

# BEM VINDO AO SISTEMA BANCARIO TESTE (1 USER) #
'''

menu = ("""

##########################################
#                                        #
#     [d] Depositar                      #
#     [s] Sacar                          #
#     [e] Extrato                        #
#     [a] Solicitar Mais Saques          #
#     [z] Visualizar Saldo               #
#     [q] Sair                           #
#                                        #
##########################################

=>""")

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
limite_saques = 3
aumeto_limite_saque = 2
solicitacao_limite_saque = 0

print(intro)

while True:

    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação Inválida!")

    elif opcao == "s" or opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_valor_saque

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação inválida! Não há saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! o valor máximo de saque é de R$500,00. ")

        elif excedeu_saques:
            if solicitacao_limite_saque == 0:
                print("Você pode solicitar saque extra para hoje, se necessário.")
            else:
                print("Operação inválida! Para sua SEGURANÇA, não é permitido novos saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e" or opcao == "E":
        print("\n________________ EXTRATO _______________")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("________________________________________")
        
    elif opcao == "a" or opcao == "A":
        if solicitacao_limite_saque == 0:
            print('''
                    Você pode acrescentar 2 saques extras à sua conta.
                    Lembramos que o limite de saque serve para sua SEGURANÇA.
                  
                  ''')
            opcao = input("\n Deseja acrescentar 2 saques extras à sua conta?  (s/n)")
            if opcao == "s" or opcao == "S" or opcao == "sim" or opcao == "Sim" or opcao == "sIM" or opcao == "SIM":
               limite_saques += aumeto_limite_saque
               solicitacao_limite_saque += 1
               print("\n\n\n\n\n\n\n\nVocê possui mais 2 saques para hoje.")
            else:
                print("\n\n\n\n\n\n\n\nOperação Cancelada.")
        else:
            print("Você não pode solicitar novos saques hoje.")
            print("\nCaso tenha dúvidas, entre em contato com seu gerente.")
    
    elif opcao == "z" or opcao == "Z":
        print("\n_____________ SALDO _______________")
        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        print("\n___________________________________")

    elif opcao == "q" or opcao == "Q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print ("\n\n\n\n\n\n\n\n\n\n\nObrigado pela Confiança\n\n\n\n\n\n\n\n")