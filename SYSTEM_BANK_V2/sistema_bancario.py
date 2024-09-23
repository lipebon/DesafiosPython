
def menu():
    menu = """
     #####################################
     #                                   #
     #        [d]Depositar               #
     #        [s]Sacar                   #
     #        [e]Extrato                 #
     #        [a]Solicitar Mais Saque    #
     #        [nc]Nova conta             #
     #        [lc]Listar contas          #
     #        [nu]Novo usuário           #
     #        [q]Sair                    #
     #                                   #
     #####################################

    ->"""
    return input(menu)

#funções relacionadas as movimentações na conta

def solicita_aumento_limite_saque(aumeto_limite_saque, solicitacao_limite_saque, limite_saque):
    if solicitacao_limite_saque == 0:
        print('''
                    Você pode acrescentar 2 saques extras à sua conta.
                    Lembramos que o limite de saque serve para sua SEGURANÇA.
                  
                  ''')
        opcao_int = input("\n Deseja acrescentar 2 saques extras à sua conta?  (s/n)")
        if opcao_int == "s" or opcao_int == "S" or opcao_int == "sim" or opcao_int == "Sim" or opcao_int == "sIM" or opcao_int == "SIM":
               limite_saque += aumeto_limite_saque
               solicitacao_limite_saque += 1
               print("\n\n\n\n\n\n\n\nVocê possui mais 2 saques para hoje.")
        else:
                print("\n\n\n\n\n\n\n\nOperação Cancelada.")
    else:
        print("Você não pode solicitar novos saques hoje.")
        print("\nCaso tenha dúvidas, entre em contato com seu gerente.")
    return solicitacao_limite_saque , limite_saque


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\nOperação Inválida - Tente novamente")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, saques_realizados, limite_saque):

    sem_saldo = valor > saldo
    limite_no_saque = valor > limite
    excedeu_saques = saques_realizados >= limite_saque

    if sem_saldo:
        print("\nVocê não possui saldo suficiente.")

    elif limite_no_saque:
        print("\nO valor máximo para saque é de R$ 500,00 - Favor tentar novamente.")

    elif excedeu_saques:
        print("\nOperação Bloqueada para sua segurança.")
        print ("\nO limite diário de saques foi atingido")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        saques_realizados += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
        print(f"""\n
              ----------------------------------

              Saldo Atual de: R$ {saldo:.2f} .
              
              ----------------------------------
              """)

    else:
        print("\nOperação inválida.")

    return saldo, extrato, saques_realizados

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

#funções relacionadas a criação de usuário e conta

def criar_usuario(usuarios):
    cpf = input("Por favor, insira o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nAtenção! Usuário já cadastrado no sistema.")
        return

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Insira a data de nascimento no formato (DD-MM-AAAA) - incluindo traços: ")
    endereco = input("Informe o endereço completo (logradouro, número - bairro - cidade/estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("\nUsuário registrado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do titular da conta: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nNova conta criada com sucesso!")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }

    print("\nNão foi possível encontrar o usuário, criação da conta cancelada.")
    

def listar_contas(contas):
    for conta in contas:
        detalhes_conta = f"""
        Agência:\t{conta['agencia']}
        Conta Corrente:\t{conta['numero_conta']}
        Nome do Titular:\t{conta['usuario']['nome']}
        """
        print("__" * 20)
        print(detalhes_conta)

#Aqui está a função programa, que usará todas as funções anteriormente declaradas

def program():
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    saques_realizados = 0
    limite_saque = 3
    aumeto_limite_saque = 2
    solicitacao_limite_saque = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == "a" or opcao == "A":
           solicitacao_limite_saque, limite_saque = solicita_aumento_limite_saque(aumeto_limite_saque, solicitacao_limite_saque, limite_saque)
           print ("\t\nEm caso de duvidas, entre em contato com seu Gerente.")

        if opcao == "d" or opcao == "D":
            print("""\n
                  
                  Obs.1:
                  Se houver centavos a ser depositado, usar . como separação.
                  Exemplo: R$ 00.
                  
                  Obs.2:
                  Não são aceitos depositos negativos, apenas valores positivos devem ser inseridos.
                  

                  """)
            valor = float(input("Valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s" or opcao == "S":
            print(f"\nVocê já realizou {saques_realizados} saque(s) hoje!")
            valor = float(input("\t\nInforme o valor do saque: "))

            saldo, extrato, saques_realizados = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                saques_realizados=saques_realizados,
                limite_saque=limite_saque,
            ) 

        elif opcao == "e" or opcao == "E" :
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc" or opcao == "NC" or opcao =="Nc" or opcao == "nC" :
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc" or opcao == "LC" or opcao =="Lc" or opcao == "lC" :
            listar_contas(contas)

        elif opcao == "q" or opcao == "Q" or opcao =="quit" or opcao == "exit" or opcao == "clear" :
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


program()