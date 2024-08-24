import pygame


class puntos():
    def __init__(self, screen, cords, size, number):
        self.screen = screen
        self.color = (255, 255, 255)
        self.x = cords.x * size
        self.y = cords.y * size
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        self.font = pygame.font.SysFont('arialblack', 20)
        self.puntos = 0


    def draw(self):
        self.img = self.font.render(f'Puntos: {self.puntos}', True, self.color)

        key = pygame.key.get_pressed()
        if key[pygame.K_TAB]:
            self.screen.blit(self.img, self.rect)
    
    def contador(self):
        self.puntos+=1


