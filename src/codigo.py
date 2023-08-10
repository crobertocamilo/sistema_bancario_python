import os

# Recebe os dados do cliente a partir de seu login no sistema
CLIENTE = {
    'nome': 'Arthur',
    'agencia': 1234,
    'conta': '0001-1',
    'saldo': 400,
    'limite_diario_saques': 3,
    'limite_valor_por_saque': 500,
    'qtd_saques_dia': 0,
    'valor_sacado_dia': 0
}

extrato = [f'Saldo anterior: R$ {CLIENTE["saldo"]:0.2f}']

#Limpa a tela do terminal
os.system('clear')

#O menu deve ser exibido até que o usuário digite 0 (zero)
while True:
        
    print('''
  === Menu de Operações ===
        
      [1] Depósito
      [2] Saque
      [3] Extrato
      [0] Sair
        
  =========================      
    '''
    )

    while True:
        try:
            opcao = int(input('Selecione a operação desejada: '))
            break
        except:
            print('Opção inválida! \n')
            continue
    
    os.system('clear')

    if opcao == 1:
        
        while True:
            print('Opção selecionada: DEPÓSITO \n')

            while True:
                try:
                    valor = float(input('Informe o valor a ser depositado: '))
                    break
                except:
                    print('Valor de depósito inválido! \n')
                    continue

            if valor <= 0:
                print('Valor de depósito inválido! \n')
                continue
            else:
                while True:
                    print(f'''
  Confirma o depósito de R$ {valor:.2f}?

     [1] Sim
     [0] Não

  ''')
                    while True:
                        try:
                            confirmacao = int(input('Confirmação: '))
                            break
                        except:
                            print('Opção inválida! \n')
                            continue

                    if (confirmacao == 1):
                        CLIENTE['saldo'] += valor
                        os.system('clear')
                        print('Opção selecionada: SIM \n')
                        print(f'Depósito confirmado! \n')
                        print(f'Novo saldo da conta: R$ {CLIENTE["saldo"]:.2f} \n')
                        extrato.append(f'Depósito........R$  {valor:0.2f}') 
                        break
                    
                    elif (confirmacao == 0):
                        print('\nOpção selecionada: NÃO \n')
                        break
                    else:
                        print('\nOpção inválida! \n')
                        continue
            
                break

    if opcao == 2:
        
        #Cliente já excedeu o limite de saques no dia?
        if (CLIENTE['qtd_saques_dia'] >= CLIENTE['limite_diario_saques']):
            print(f'Limite de saque diário ({CLIENTE["qtd_saques_dia"]}) excedido!')
            print('Não é possível fazer a operação! Por favor, tente novamente amanhã.')

        else:
            while True:
                print('Opção selecionada: SAQUE \n')

                while True:
                    try:
                        valor = float(input('Informe o valor a ser sacado: '))
                        break
                    except:
                        print('Valor de saque inválido! \n')
                        continue
                
                if valor <= 0:
                    print('Valor de saque inválido! \n')
                    continue
                elif valor > CLIENTE['limite_valor_por_saque']:
                    print('Valor inválido! O limite de saque por operação é de R$ 500 \n')
                    continue            
                else:
                    while True:
                        print(f'''
  Confirma o saque de R$ {valor:.2f}?

     [1] Sim
     [0] Não

    ''')
                        while True:
                            try:
                                confirmacao = int(input('Confirmação: '))
                                break
                            except:
                                print('Opção inválida! \n')
                                continue

                        if (confirmacao == 1):
                            
                            #O cliente tem saldo suficiente para o saque?
                            if (CLIENTE['saldo'] - valor) >= 0:
                                CLIENTE['saldo'] -= valor
                                CLIENTE['qtd_saques_dia'] += 1
                                os.system('clear')
                                print('Opção selecionada: SIM \n')
                                print(f'Saque efetuado! \n')
                                print(f'Novo saldo da conta: R$ {CLIENTE["saldo"]:.2f} \n')
                                input('Pressione qualquer tecla para continuar.')
                                extrato.append(f'Saque...........R$  {valor:0.2f}')

                            else:
                                print('\nNão é possível efetuar o saque: Saldo insuficiente!')
                                print(f'Saldo da conta: R$ {CLIENTE["saldo"]:.2f} \n')
                                input('Pressione qualquer tecla para continuar.')
                            break
                        
                        elif (confirmacao == 0):
                            print('\nOpção selecionada: NÃO \n')
                            break
                        else:
                            print('\nOpção inválida! \n')
                            continue
                
                    break
            

    if opcao == 3:
        print('Opção selecionada: EXTRATO \n')
        print('==== Extrato da Sessão ====\n')

        #Houve alguma movientação durante a seção?
        if len(extrato) == 1:
            print(extrato[0])
            print('Não foram realizadas movimentações.')
        
        else:
            for item in range(len(extrato)):
                print(extrato[item])
            print(f'Saldo atual:    R$ {CLIENTE["saldo"]:0.2f}\n')
        print('===========================\n\n')
        input('Pressione qualquer tecla para continuar.')

    if opcao == 0:
        print('\nAgradecemos por utilizar os nossos serviços! Tenha um bom dia! \n')
        print('=== Sessão Encerrada === \n')
        break

    print('\nDeseja realizar outra operação?\n')
        

        


            


        

        
      