import pygame
import random
from pygame import Vector2
import Menu
import Puntos
from os import listdir
from os.path import isfile, join

class SNAKE:
    def __init__(self, size, number, screen):
        self.screen = screen
        self.cell_number = number
        self.cell_size = size
        #Almacena las coordenadas de los cuadrados dentro de la lista
        self.body = [Vector2(5,10),Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x*self.cell_size)
            y_pos = int(block.y*self.cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, (126,111,114), snake_rect)

    def move_snake(self):

        self.body_copy = self.body[:-1]
        self.body_copy.insert(0, self.body_copy[0] + self.direction)
        self.body = self.body_copy[:]


class FRUIT:
    def __init__(self, size, number, screen):
        self.screen = screen
        self.cell_number = number
        self.cell_size = size
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        self.fruits = [f for f in listdir('Assets/') if isfile(join('Assets/', f))]
        self.choice = random.choice(self.fruits)
        self.path = f'Assets/{self.choice}'
        self.fruit_image = pygame.image.load(self.path).convert_alpha()
        self.fruit_image = pygame.transform.scale(self.fruit_image, (self.cell_size, self.cell_size))

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * self.cell_size), int(self.pos.y * self.cell_size), self.cell_size, self.cell_size)
        self.screen.blit(self.fruit_image, fruit_rect)
        #pygame.draw.rect(screen, (126,166,114), fruit_rect)

    def update_pos(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self, size, number, screen, puntos):
        self.screen = screen
        self.size = size
        self.number = number
        self.snake = SNAKE(self.size, self.number, self.screen)
        self.fruit = FRUIT(self.size, self.number, self.screen)
        self.puntos = puntos

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fails()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.snake.body[0] == self.fruit.pos:
            self.fruit.update_pos()
            self.snake.body.append(self.snake.body[-1]) #Agregamos el ultimo elemento en la ultima posicion para simular el efecto de que incrementamos el tamanio de la serpiente
            self.puntos.contador()

    def check_fails(self):
        #Saber si sale de la pantalla
        if not 0 <= self.snake.body[0].x < self.number or not 0 <= self.snake.body[0].y < self.number: 
            self.game_over()

        #Saber si choca con su propio cuerpo
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()


    def game_over(self):
        play = False
        Menu.main(play)

def principal():
    pygame.init()
    cell_size = 40
    cell_number = 20
    screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
    running = True
    bg = (175,215,70)
    clock = pygame.time.Clock()
    puntos = Puntos.puntos(screen, Vector2(0, 0), cell_size, cell_number)

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 80)

    main_game = MAIN(cell_size, cell_number, screen, puntos)

    while running:
        screen.fill(bg)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                #User input
                key = pygame.key.get_pressed()
                if key[pygame.K_w] and main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
                if key[pygame.K_s] and main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
                if key[pygame.K_a] and main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
                if key[pygame.K_d] and main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

        puntos.draw()
        main_game.draw_elements()
        pygame.display.flip()
        clock.tick(60)


    pygame.quit()

    
if __name__ == '__main__':  #Esto sirve para que el juego inicie solo si es abierto desde el archivo principal
    principal()