class FirstHundredGenerator():
    def __init__(self):
        self.number = 0

    def __next__(self): #Permite hacer next(object)
        if self.number < 100:
            current = self.number
            self.number += 1 # Incrementa pero devuelve el anterior
            return current
        else:
            raise StopIteration() # Para especificar que ya se acabó el generador


my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen))