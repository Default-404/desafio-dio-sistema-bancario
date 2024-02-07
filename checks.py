LIMIT_ON_AMOUNT = 500
LIMIT_OF_WITHDRAWALS = 3

def balance_withdraw_check(withdraw_amount, balance):
    return withdraw_amount > balance

def amount_withdraw_check(withdraw_amount):
    return withdraw_amount > LIMIT_ON_AMOUNT

def limit_of_withdrawals_check(number_of_withdrawals):
    return number_of_withdrawals >= LIMIT_OF_WITHDRAWALS