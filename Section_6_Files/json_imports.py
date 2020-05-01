import pathlib2 as pathlib
import json


my_file = open(pathlib.Path(__file__).parent/'data.json','r')
file_contents = json.load(my_file) #Lo convierte en diccionario

my_file.close()

print(file_contents['friends'][0])

#Guardando en archivo .json

cars =[
    {"made":"ford","model":"Fiesta"},
    {"made":"ford","model":"Focus"}
]

with open(pathlib.Path(__file__).parent/'cars.json', 'w', encoding='utf-8') as f:
    json.dump(cars, f)
