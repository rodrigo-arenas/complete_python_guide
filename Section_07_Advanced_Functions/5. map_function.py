"""
map() toma un iterable y devuelve otro iterable
"""

friends = ['Juan', 'Carlos', 'Daniel', 'Ricardo', 'Jhon']

friends_lower = map(lambda x: x.lower(), friends)
print(next(friends_lower))
print(next(friends_lower))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


users = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'jhon', 'password': '245'}
]

users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users)  # Equivalente a la sintaxis anterior
