def starts_with_j(friend):
    return friend.startswith("J")


friends = ['Juan', 'Carlos', 'Daniel', 'Ricardo', 'Jhon']
# filter() toma como argumentos una función que regrese True/False
# y lo que se quiere filtrar como un iterable

friends_j = filter(starts_with_j, friends) # Regresa un generador
print(list(friends_j))

another_friend_j = (f for f in friends if f.startswith('J')) # Generador

#Otra opción es usar directamente lambda
another_friend_c = (lambda friend: friend.starswith('C'), friends)
print(list(another_friend_c))
