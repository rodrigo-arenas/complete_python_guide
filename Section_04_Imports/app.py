#file_operations está por fuera de este folder, se tiene que hacer el import completo
#en la carpeta de utils se pone el __init__.py para volver al modulo un paquete
#Siempre hacer imports absolutos, no relativos con .
import Section_04_Imports.utils.file_operations as fo
import pathlib2 as pathlib


file = pathlib.Path(__file__).parent/'data.txt'
fo.save_to_file('Jhon', file)

