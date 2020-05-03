# Iterator -> next(), iterable -> recorrer todos los valores


class FirstHundredGenerator():
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        """
        Se define un iterable si tiene el método __iter__. Con esto se pueden hacer loops o sumas, etc
        """
        return self


print(sum(FirstHundredGenerator()))
for i in FirstHundredGenerator():
    print(i)

# Otra opción es definir un iterable con una clase que tenga los métodos:
# __len__ y __getitem__


class AnotherIterable:
    def __init__(self):
        self.cars = ['Ford','Fiesta']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]


for car in AnotherIterable():
    print(car)
