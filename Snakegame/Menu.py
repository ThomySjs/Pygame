import pygame
from pygame import Vector2
import Snakegame1

class Button():
    def __init__(self, cords,  img, scale, wich, size, number, screen):
        self.size = size
        self.number = number
        self.screen = screen
        self.identifier = wich
        self.width = img.get_width()
        self.height = img.get_height()
        self.img = pygame.transform.scale(img, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.img.get_rect()
        self.cords = cords
        self.x = (self.cords.x * self.size)
        self.y = (self.cords.y * self.size)
        self.rect.center = (self.x, self.y)
    
    def draw_button(self):

        #get mouse pos
        mouse = pygame.mouse.get_pos()
        
        #if clicks button
        if self.rect.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1:
                if self.identifier == 'start':
                    Snakegame1.principal()
                elif self.identifier == 'exit':
                    pygame.quit()

        self.screen.blit(self.img, (self.rect.x, self.rect.y))


def main():
    pygame.init()
    cell_size = 40
    cell_number = 20
    screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
    running = True
    bg = (175,215,70)
    clock = pygame.time.Clock()

    start_img = pygame.image.load('Botones/start_btn.png').convert_alpha()
    exit_img = pygame.image.load('Botones/exit_btn.png').convert_alpha()

    #create buttons instances
    start = Button(Vector2(10, 8), start_img, 0.7, 'start', cell_size, cell_number, screen)
    exitA =Button(Vector2(10, 11), exit_img, 0.7, 'exit', cell_size, cell_number, screen)
    while running:

        screen.fill(bg)

        start.draw_button()
        exitA.draw_button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            #mouse pressed


        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()