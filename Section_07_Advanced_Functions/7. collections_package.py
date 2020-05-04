"""
counter
defaultdict
ordereddict
namedtuple
dequeue
"""


# Counter
from collections import Counter

device_temperatures = [12, 14, 10, 14.3, 11.9, 14]
temperature_counter = Counter(device_temperatures)  # Regresa conteo de cada entrada
print(temperature_counter[14])
print(temperature_counter)

# Default Dict
from collections import defaultdict
coworkers = [
    ('Rolf', 'MIT'),
    ('Jen', 'Oxford'),
    ('Charlie', 'Manchester'),
    ('Rolf', 'Cambridge')
]

alma_maters = defaultdict(list)  # Cuando se acceda a un key que no exista, devuelve [] por defecto
for coworker, place in coworkers:
    alma_maters[coworker].append(place)


print(alma_maters)
print(alma_maters['Jesus'])  # Devuelve [] al ser el valor por defecto así no exista el key
alma_maters.default_factory = None  # Bajo esto, levanta un error al llama una key inexistente
# print(alma_maters['Jesus'])

# Ordered Dict
from _collections import OrderedDict
o = OrderedDict()
o['Rolf'] = 0
o['Jose'] = 6
o['Jen'] = 3

print(o)  # Preserva el orden enque fue insertado

# Named tupled
from collections import namedtuple
account = ('checking', 125.23)
Account = namedtuple('Account', ['name', 'balance'])
account = Account('checking', 125.23)
print(account.name)
print(account)


# Deque: Doubled ended queue
# Es más eficiente que list cuando se quiere agregar oquitar elementos del inicio y fin
# Es mejor compatible on threads
from collections import deque
friends = deque(('Rolf', 'Anna', 'Charlie', 'Jen'))
friends.append('Jose')
friends.appendleft('Antony')
friends.pop()
friends.popleft()

