import pygame
import random
from pygame import Vector2

class SNAKE:
    def __init__(self):
        #Almacena las coordenadas de los cuadrados dentro de la lista
        self.body = [Vector2(5,10),Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (126,111,114), snake_rect)

    def move_snake(self):

        self.body_copy = self.body[:-1]
        self.body_copy.insert(0, self.body_copy[0] + self.direction)
        self.body = self.body_copy[:]


class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        self.fruit_image = pygame.image.load('Assets/30.png').convert_alpha()
        self.fruit_image = pygame.transform.scale(self.fruit_image, (cell_size, cell_size))

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(self.fruit_image, fruit_rect)
        #pygame.draw.rect(screen, (126,166,114), fruit_rect)

    def update_pos(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

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

    def check_fails(self):
        #Saber si sale de la pantalla
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number: 
            self.game_over()

        #Saber si choca con su propio cuerpo
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()


    def game_over(self):
        pygame.quit()

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
running = True
bg = (175,215,70)
clock = pygame.time.Clock()

fruit= FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 80)

main_game = MAIN()

while running:

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

    screen.fill(bg)

    main_game.draw_elements()
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
    