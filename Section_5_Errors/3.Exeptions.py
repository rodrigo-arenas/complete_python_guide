
class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    
    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars =[]

    def __len__(self):
        return len(self.cars)

    def add_car(self,cars):
        if not isinstance(cars,Car):
            raise TypeError(f'Tried to add a {cars.__class__.__name__} to garage, but you can only add \'Cars\' objects')
        self.cars.append(cars)


ford = Garage()
Fiesta= Car('Ford','Fiesta')

try:
    ford.add_car('Fiesta')
except TypeError: #Solo este tipo de error se controla
    print('Your car was not a Car')
except ValueError:
    print('Something weird happened')
finally: #Corre haya o no ocurrido un error
    print(f'The garage now has {len(ford)} cars')

