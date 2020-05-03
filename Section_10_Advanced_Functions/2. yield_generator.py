"""
Con yield se crea un "Generador", con el cual se puede iterar sin almancenar todo
en memoria desde el inicio
"""


def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


g = hundred_numbers()
print(next(g))
print(next(g))
print(list(g))
