import pygame
from os import path

class sonidos():
    def __init__(self):
        self.volumeS = 0.5

    def load(self, title):
        path.basename('audio/')
        self.music = pygame.mixer.music.load(title)

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