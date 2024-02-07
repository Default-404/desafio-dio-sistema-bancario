menu = '''
[d] Depositar
[s] Sacar
[e] Mostrar Extrato
[q] Sair

Informe a operação desejada => '''

def deposit(deposit_amount, balance, statement):
    balance += deposit_amount
    statement += f'Depósito: R$ {deposit_amount:.2f}\n'
    return balance, statement

def withdraw(withdraw_amount, balance, statement):
    balance -= withdraw_amount
    statement += f'Saque: R$ {withdraw_amount:.2f}\n'
    return balance, statement

def show_statement(statement, balance):
    print('Não foram realizadas movimentações.' if not statement else statement)
    print(f'\nSaldo: R$ {balance:.2f}')