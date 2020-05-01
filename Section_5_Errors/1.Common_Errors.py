
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

    def add_car(self,car):
        #NotImplementedError Error para especificar que este método aún no se ha implementado
        raise NotImplementedError("We can't add cars to garage yet")

    def add_cars(self,cars):
        #isinstance(x,y) mira si x es de la clase de Y
        if not isinstance(cars,Car):
            raise TypeError(f'Tried to add a {cars.__class__.__name__} to garage, but you can only add \'Cars\' objects')
        self.cars.append(cars)


ford = Garage()
#ford.add_car('Fiesta') <-NotImplementedError
print(len(ford))
#ford.add_cars('Volvo') <- TypeError
car= Car('Ford','Fiesta')
ford.add_cars(car)
print(len(ford))
