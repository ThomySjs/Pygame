import pygame
from pygame import Vector2
import Game_logic
import Puntos
import Sonido

class Button():
    def __init__(self, cords,  img, scale, size, number, screen):
        self.size = size
        self.number = number
        self.screen = screen
        self.width = img.get_width()
        self.height = img.get_height()
        self.img = pygame.transform.scale(img, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.img.get_rect()
        self.cords = cords
        self.x = (self.cords.x * self.size)
        self.y = (self.cords.y * self.size)
        self.rect.center = (self.x, self.y)
        self.clicked = False
    
    def draw_button(self):
        action = False
        #Toma la posicion del mouse
        mouse = pygame.mouse.get_pos()
        
        #Si hacemos click en algun boton
        if self.rect.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        self.screen.blit(self.img, (self.rect.x, self.rect.y))

        return action

def main(music):

        pygame.init()
        cell_size = 40
        cell_number = 20
        screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
        running = True
        bg = (175,215,70)
        sonido = Sonido.sonidos()
        if music == True:
            sonido.load()
            sonido.play()
        
        NEXT = pygame.USEREVENT + 1
        pygame.mixer_music.set_endevent(NEXT)

        start_img = pygame.image.load('Botones/start_btn.png').convert_alpha()
        exit_img = pygame.image.load('Botones/exit_btn.png').convert_alpha()

        #create buttons instances
        start = Button(Vector2(10, 8), start_img, 0.7, cell_size, cell_number, screen)
        exitA =Button(Vector2(10, 11), exit_img, 0.7, cell_size, cell_number, screen)

        over = False

        while running:

            screen.fill(bg)

            if start.draw_button():
                over = True
                running = False
            if exitA.draw_button():
                running = False

            for event in pygame.event.get():
                if event.type == NEXT:
                    sonido.load()
                    sonido.play()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4: #Hacia arriba
                        sonido.volumeUP()
                    if event.button == 5:
                        sonido.volumeDOWN()
                if event.type == pygame.QUIT:
                    running = False
                

            pygame.display.flip()
        if over:
            Game_logic.principal() #Esto es para salir del bucle antes de llamar a la nueva ventana.

        pygame.quit()


if __name__ == '__main__':
    play = True
    main(play)