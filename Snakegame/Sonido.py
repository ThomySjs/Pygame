import pygame
from os import listdir
from os.path import isfile, join
import random

class sonidos():
    def __init__(self):
        self.volumeS = 0.5

    def load(self):
        file = [f for f in listdir('audio/') if isfile(join('audio/', f))] #Si f es un archivo entonces hola.append(f) (ignora carpetas)
        song = random.choice(file)
        path = f'audio/{song}'
        pygame.mixer.music.load(path)
        file.remove(song)

    def play(self):
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(self.volumeS)

    def volumeUP(self):
        if self.volumeS <= 0.9:
            self.volumeS += 0.1
        pygame.mixer.music.set_volume(self.volumeS)
    
    def volumeDOWN(self):
        if self.volumeS >= 0.1:
            self.volumeS -= 0.1
        pygame.mixer.music.set_volume(self.volumeS)