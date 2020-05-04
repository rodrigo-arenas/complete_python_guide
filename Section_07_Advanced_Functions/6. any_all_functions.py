
friends = [
    {'name': 'rolf', 'location': 'USA'},
    {'name': 'Jhon', 'location': 'Argentina'},
    {'name': 'Alex', 'location': 'Mexico'},
    {'name': 'Jenny', 'location': 'Canada'},
]

your_location = input("Where are you right now?")
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):  # True si hay algo en el iterador
    print("You are not alone!")

print(all([1, 3, 4, 5]))
print(all([0, 1, 3, 4, 5]))

"""
objetos vacíos, el número 0, se evalua como False
se puede evaluar con bool()
"""


