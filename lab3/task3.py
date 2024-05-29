import pygame
from pygame.draw import (rect, line,
                         circle, ellipse, polygon)
from random import randint
import math

pygame.init()

house_coord = {
    "roof": [
        (-130, -60),
        (-110, -70),
        (140, -70),
        (160, -60)
    ],
    "windows": [
        (-105, -55)
    ],
    "balcony": [
        (-110, 0),
        (-115, 15)
    ],
    "windows2": [
        (-90, 45)
    ]
}


TICKRATE = 30
HEIGHT = 600
WIDTH = 1000


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((128, 128, 128))

CENTER = (WIDTH//2, HEIGHT//2)


def offset(point, offset):
    return (point[0] + offset[0], point[1] + offset[1])


def draw_factory(point):
    surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    rect(surface, (30, 30, 30), offset(point, (90, -80)) + (30, 80))
    rect(surface, (30, 30, 30), offset(point, (-90, -80)) + (30, 80))
    polygon(surface, (0, 0, 0),
            [offset(point, x) for x in house_coord["roof"]])
    rect(surface, (60, 38, 5), offset(point, (-110, -60)) + (250, 150))

    win1st = offset(point, house_coord["windows"][0])
    for i in range(6):
        rect(surface, (90, 68, 15), offset(win1st, (40.8 * i, 0)) + (35, 50))

    rect(surface, (30, 30, 30), offset(point, house_coord["balcony"][0])
         + (250, 5))
    rect(surface, (30, 30, 30), offset(point, house_coord['balcony'][1])
         + (260, 20))

    for i in range(7):
        wd = 10 if i % 6 == 0 else 5
        line(surface, (30, 30, 30), offset(point, (-115 + (43 * i), 20)),
             offset(point, (-115 + (43 * i), 5)), wd)
    win2_1st = offset(point, house_coord["windows2"][0])

    for i in range(3):
        col = (20, 8, 0) if i != 2 else (210, 180, 0)
        rect(surface, col, offset(win2_1st, (73 * i, 0)) + (63, 30))
    screen.blit(surface, (0, 0))


def draw_ghost(point: tuple[int, int], alpha: int = 255):
    surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    polygon(surface, (255, 255, 255, alpha),
            [point,
             offset(point, (-20, 100)),
             offset(point, (130, 100)),
             offset(point, (110, 0))])
    polygon(surface, (255, 255, 255, alpha), [offset(offset(point, (55, 0)),
                                              (math.cos(math.radians(x))
                                                  * 55,
                                              math.sin(math.radians(x))
                                                  * 55))
                                              for x in range(-180, 0)])
    circle(surface, (0, 0, 0), offset(point, (25, 0)), 15)
    circle(surface, (0, 0, 0), offset(point, (85, 0)), 15)
    polygon(surface, (0, 0, 0), [offset(offset(point, (55, 10)),
                                 (math.cos(math.radians(x)) * 15,
                                  math.sin(math.radians(x)) * 15))
                                 for x in range(0, 180)], 2)
    screen.blit(surface, (0, 0))


rect(screen, (45, 45, 45),
     offset(CENTER, (-CENTER[0], -15)) + (WIDTH, CENTER[1] + 15))
ellipse(screen, (210, 210, 210), (WIDTH - 140, 10, 130, 100))

for i in range(6):
    cloud = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    ellipse(cloud, [randint(60, 110)]*3 + [randint(100, 255)],
            offset(CENTER, (randint(-WIDTH//2, WIDTH//2),
                            -(160 + randint(0, 100))))
            + (300, 75))
    screen.blit(cloud, (0, 0))

draw_factory(offset(CENTER, (-350, 50)))
draw_factory(offset(CENTER, (0, 0)))
draw_factory(offset(CENTER, (350, -50)))
for _ in range(6):
    draw_ghost(offset(CENTER, (randint(-400, 400), randint(0, 200))),
               randint(128, 255))

for i in range(15):
    cloud = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    ellipse(cloud, [randint(60, 110)]*3 + [randint(50, 128)],
            offset(CENTER, (randint(-WIDTH//2, WIDTH//2),
                            randint(-200, 200)))
            + (300, 75))
    screen.blit(cloud, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(TICKRATE)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE] or pressed[pygame.K_SPACE]:
        finished = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
