from pygame.draw import circle
from random import randint, choice

import pygame
import math

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    '''
    Класс, представляющий мячики
    '''
    def __init__(self, x, y, r):
        self.pos_x = x
        self.pos_y = y
        self.radius = r
        self.color = choice(COLORS)
        self.angle = randint(0, 359)
        self.vec_x = math.cos(math.radians(self.angle))
        self.vec_y = math.sin(math.radians(self.angle))

    def check_in_bounds(self, x, y):
        '''
        Проверяет, находятся ли данные координаты в круге
        x - координата x
        y - координата y
        '''
        dst = (
            (x - self.pos_x)**2 +
            (y - self.pos_y)**2
            )**(0.5)
        return dst <= self.radius

    def draw(self, surface):
        '''
        Отрисовывает круг на заданной поверхности
        surface - объект класса pygame.Surface
        '''
        circle(
            surface,
            self.color,
            (self.pos_x, self.pos_y),
            self.radius
        )

    def move(self, speed):
        self.pos_x += self.vec_x * speed
        self.pos_y += self.vec_y * speed

        if (self.pos_y - self.radius <= 0 or
                self.pos_y + self.radius >= WINDOW_HEIGHT):
            self.vec_y = -self.vec_y
        if (self.pos_x - self.radius <= 0 or
                self.pos_x + self.radius >= WINDOW_WIDTH):
            self.vec_x = -self.vec_x

        self.pos_x = max(
            self.radius,
            min(WINDOW_WIDTH - self.radius, self.pos_x))
        self.pos_y = max(
            self.radius,
            min(WINDOW_HEIGHT - self.radius, self.pos_y))


class Game:
    def __init__(self):
        self.points = 0
        self.balls = list()

    def new_ball(self):
        x = randint(100, WINDOW_WIDTH - 100)
        y = randint(100, WINDOW_HEIGHT - 100)
        r = randint(10, 100)
        ball = Ball(x, y, r)
        self.balls.append(ball)

    def move_balls(self, timestep):
        for ball in self.balls:
            ball.move(0.1 * timestep)

    def draw(self, surface):
        surface.fill(BLACK)
        for ball in self.balls:
            ball.draw(surface)

    def on_click(self, mouse_pos):
        for ball in self.balls:
            if ball.check_in_bounds(mouse_pos[0], mouse_pos[1]):
                self.points += 1
                self.balls.remove(ball)


pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 24)
game = Game()
finished = False

time_to_spawn = 1000

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.on_click(pygame.mouse.get_pos())

    timestep = clock.tick(FPS)

    time_to_spawn -= timestep
    game.move_balls(timestep)

    if time_to_spawn <= 0:
        time_to_spawn = 1000
        game.new_ball()

    game.draw(screen)
    text = font.render(f"Счёт: {game.points}", True, WHITE)

    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
