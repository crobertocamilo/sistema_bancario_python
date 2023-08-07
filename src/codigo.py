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
os.system('clear')

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

    opcao = int(input('Selecione a operação desejada: '))
    os.system('clear')

    if opcao == 1:
        
        while True:
            print('Opção selecionada: DEPÓSITO \n')
            valor = float(input('Informe o valor a ser depositado: '))

            if valor <= 0:
                print('Valor de depósito inválido! \n')
                continue
            else:
                while True:
                    confirmacao = int(input(f'''
  Confirma o depósito de R$ {valor:.2f}?

     [1] Sim
     [0] Não

  '''))
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
                valor = float(input('Informe o valor a ser sacado: '))

                if valor <= 0:
                    print('Valor de saque inválido! \n')
                    continue
                elif valor > 500:
                    print('Valor inválido! O limite de saque por operação é de R$ 500 \n')
                    continue            
                else:
                    while True:
                        confirmacao = int(input(f'''
  Confirma o saque de R$ {valor:.2f}?

     [1] Sim
     [0] Não

    '''))
                        if (confirmacao == 1):
                            
                            #O cliente tem saldo suficiente para o saque?
                            if (CLIENTE['saldo'] - valor) >= 0:
                                CLIENTE['saldo'] -= valor
                                CLIENTE['qtd_saques_dia'] += 1
                                os.system('clear')
                                print('Opção selecionada: SIM \n')
                                print(f'Saque efetuado! \n')
                                print(f'Novo saldo da conta: R$ {CLIENTE["saldo"]:.2f} \n')
                                extrato.append(f'Saque...........R$  {valor:0.2f}')

                            else:
                                print('Não é possível efetuar o saque: Saldo insuficiente!')
                                print(f'Saldo da conta: R$ {CLIENTE["saldo"]:.2f} \n')
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
        for item in range(len(extrato)):
            print(extrato[item])
        print(f'Saldo atual:    R$ {CLIENTE["saldo"]:0.2f}\n')
        print('===========================\n\n')

    if opcao == 0:
        print('\nAgradecemos por utilizar os nossos serviços! Tenha um bom dia! \n')
        print('=== Sessão Encerrada === = \n')
        break

    print('\nDeseja realizar outra operação?\n')
        

        


            


        

        
      