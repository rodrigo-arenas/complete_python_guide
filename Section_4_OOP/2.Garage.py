class Garage:
    def __init__(self):
        self.cars =[]

    def __len__(self):
        #Se denomina Dunder method, se puede llamar una función predefinida
        #https://www.geeksforgeeks.org/dunder-magic-methods-python/
        return len(self.cars)
    
    def __getitem__(self,i):
        #Regresa una posición
        return self.cars[i]
    
    def __repr__(self):
        return f'<Garage {self.cars}>' #Representa la clase

    def __str__(self):
        return f'Garage with {len(self)} cars' #String para describir la clase

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(len(ford)) #Usando el dunder method __len__
print(ford[0]) #Usando el dunder method __getitem__

for car in ford:
    print(car) #Toma las propiedades de la lista por haber defindo los dunder methods

print(ford) #Usa __repr__


