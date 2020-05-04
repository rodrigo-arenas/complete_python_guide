import pathlib2 as pathlib


my_file = open(pathlib.Path(__file__).parent/'data.txt','r')

my_file_content = [line.strip() for line in my_file.readlines()] 
#.strip remueve el \n del salto linea y espacios al final y principio de cada línea
my_file.close()

print(my_file_content)