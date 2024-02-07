from operations import menu, deposit, withdraw, show_statement
from checks import balance_withdraw_check, amount_withdraw_check, limit_of_withdrawals_check

system = True
balance = 0
number_of_withdrawals = 0
statement = ''

print('Bem vindo ao DefaultBank!')

while system:
    option = input(menu)
    
    if option == 'd':
        deposit_amount = float(input('Informe o valor do depósito: '))
        
        if deposit_amount > 0:
            balance, statement = deposit(deposit_amount, balance, statement)
            print('Operação realizada com sucesso!')
        
        else:
            print('Falha na operação! O valor informado é inválido.')
    
    elif option == 's':
        withdraw_amount = float(input('Informe o valor do saque: '))
        
        if balance_withdraw_check(withdraw_amount, balance):
            print('Falha na operação! Saldo insuficiente.')
        
        elif amount_withdraw_check(withdraw_amount):
            print('Falha na operação! O valor excede o limite por saque!')
        
        elif limit_of_withdrawals_check(number_of_withdrawals):
            print('Falha na operação! Número máximo de saques excedido.')
        
        elif withdraw_amount > 0:
            balance, statement = withdraw(withdraw_amount, balance, statement)
            number_of_withdrawals += 1
            print('Operação realizada com sucesso!')
        
        else:
            print('Falha na operação! O valor informado é inválido.')
    
    elif option == 'e':
        print('______________EXTRATO______________')
        show_statement(statement, balance)
        print('___________________________________')
    
    elif option == 'q':
        system = False
    
    else:
        print('Opção inválida! Por favor selecione uma operação valida.')