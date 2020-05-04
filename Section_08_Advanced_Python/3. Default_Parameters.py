accounts = {
    'checking': 1923.3,
    'savings': 15324.2
}


def add_balance(amount: float, name: str = 'savings') ->float:
    """
    Update balance of account an return balance
    :param amount:
    :param name:
    :return:
    """
    accounts[name] += amount
    return accounts[name]


add_balance(1000)
print(accounts['savings'])

#

def create_account(name: str, holder: str, account_holders = []):
    # Los parámetros por defecto se crean cuando la función es definida, no cuando se llama
    print(id(account_holders))
    account_holders.append(holder)

    return {
        'name': name,
        'main_accoun_holder': holder,
        'account_holders': account_holders
    }

a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Jen')

print(a2)  #Agrega a Rolf porque ya se tenía del llamado anterior

# Para solventarlo, se puede poner por defecto el valor None


def create_account(name: str, holder: str, account_holders = None):
    if not account_holders:
        account_holders = []
    print(id(account_holders))
    account_holders.append(holder)

    return {
        'name': name,
        'main_accoun_holder': holder,
        'account_holders': account_holders
    }