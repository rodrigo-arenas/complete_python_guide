class FixedFloat:
    def __init__(self,amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixexFloat {self.amount:.2f}>'

    ##Si se necesita reciclar la funcinalidad se podría hacer algo como:
    """
    def from_sum(self,value1,value2):
        return FixedFloat(value1 + value2)
    """
    ##Sin embargo se estaría creando 2 veces el objeto innecesariamente
    #con @classmethod podemos especificarle que es un método que requiere el uso de la clase
    #En vez de self, se pasa cls
    @classmethod
    def from_sum(cls,value1,value2):
        return cls(value1 + value2)


number = FixedFloat(18.43673)
print(number)

new_number = FixedFloat.from_sum(16.433,43.346)
print(new_number)