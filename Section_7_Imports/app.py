#file_operations está por fuera de este folder, se tiene que hacer el import completo
#en la carpeta de utils se pone el __init__.py para volver al modulo un paquete
#Siempre hacer imports absolutos, no relativos con .
import utils.file_operations as FO
import pathlib2 as pathlib


FO.save_to_file('Kelly',pathlib.Path(__file__).parent/'data.txt')