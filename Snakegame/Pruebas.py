from os import listdir
from os.path import isfile, join
import random

hola = [f for f in listdir('audio/') if isfile(join('audio/', f))] #Si f es un archivo entonces hola.append(f) (ignora carpetas)
pepe = random.choice(hola)

print(pepe)