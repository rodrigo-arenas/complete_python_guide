
friends_last_seen = {
    'Rolf': 8,
    'Ann': 5,
    'Jen': 10
}

print(id(friends_last_seen))  # Dirección en memoria RAM

friends_last_seen = {
    'Rolf': 8,
    'Ann': 5,
    'Jen': 10
}

print("_"*5, 'dict', "_"*5)
print(id(friends_last_seen)) #  Aunque tenga el mismo contenido, es otro objeto

friends_last_seen['Rolf'] = 0

print(id(friends_last_seen)) #  El objeto es mutable, se puede cambiar y permanece su dirección

print("_"*5, 'int', "_"*5)
my_int = 5
print(id(my_int))
my_int = my_int + 1
print(id(my_int))  # Cambia debido a que los enteros son inmutables


"""
Ejemplos 
inmutables:
    int
    float
    strings
    tuples
mutables:
    dict
    list
    
"""