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


transactions =[
    (125, 'checking'),
    (129, 'savings'),
    (125, 'checking'),
    (2347, 'savings'),
    (2356, 'checking'),
    (-2362, 'savings'),
]

for t in transactions:
    # add_balance(t[0], t[1])
    add_balance(*t)  # Toma cada elemento de t como un argumento


# Unpacking dictionaries


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    #@classmethod
    #def from_dict(cls, data):
    #    return cls(data['username'], data['password'])


users = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'jhon', 'password': '245'}
]

users_objects = [User(username = data['username'], password = data['password']) for data in users]
# De manera equivalente:
users_objects = [User(**data) for data in users]  # ** toma cada llave del dict como argmento


