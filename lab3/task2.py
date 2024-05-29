import pygame
from pygame.draw import (rect, line,
                         circle, ellipse, polygon)
from random import randint
import math

pygame.init()

house_coord = {
    "roof": [
        (-180, -80),
        (-160, -120),
        (160, -120),
        (180, -80)
    ],
    "windows": [
        (-150, -80)
    ],
    "balcony": [
        (-175, 0),
        (-180, 30)
    ],
    "windows2": [
        (-120, 80)
    ]
}


TICKRATE = 30
HEIGHT = 600
WIDTH = 800


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((128, 128, 128))

clouds = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

CENTER = (WIDTH//2, HEIGHT//2)


def offset(point, offset):
    return (point[0] + offset[0], point[1] + offset[1])


def factory(point):
    scr = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    rect(scr, (30, 30, 30), offset(point, (80, -140)) + (30, 80))
    rect(scr, (30, 30, 30), offset(point, (-110, -140)) + (30, 80))
    polygon(scr, (0, 0, 0), [offset(point, x) for x in house_coord["roof"]])
    rect(scr, (60, 38, 5), offset(point, (-160, -80)) + (320, 260))

    win1st = offset(point, house_coord["windows"][0])
    for i in range(6):
        rect(scr, (90, 68, 15), offset(win1st, (51.6 * i, 0)) + (40, 100))

    rect(scr, (30, 30, 30), offset(point, house_coord["balcony"][0])
         + (350, 10))
    rect(scr, (30, 30, 30), offset(point, house_coord['balcony'][1])
         + (360, 25))
    for i in range(7):
        wd = 15 if i % 6 == 0 else 10
        line(scr, (30, 30, 30), offset(point, (-180 + (60 * i), 30)),
             offset(point, (-180 + (60 * i), 10)), wd)
    win2_1st = offset(point, house_coord["windows2"][0])
    for i in range(3):
        col = (20, 8, 0) if i != 2 else (210, 180, 0)
        rect(scr, col, offset(win2_1st, (85 * i, 0)) + (75, 50))
    screen.blit(scr, (0, 0))


def ghost(scr, point, flip: bool = False):
    polygon(scr, (255, 255, 255),
            [point,
             offset(point, (-20, 100)),
             offset(point, (130, 100)),
             offset(point, (110, 0))])
    polygon(scr, (255, 255, 255), [offset(offset(point, (55, 0)),
                                          (math.cos(math.radians(x)) * 55,
                                           math.sin(math.radians(x)) * 55))
                                   for x in range(-180, 0)])
    circle(scr, (0, 0, 0), offset(point, (25, 0)), 15)
    circle(scr, (0, 0, 0), offset(point, (85, 0)), 15)
    polygon(scr, (0, 0, 0), [offset(offset(point, (55, 10)),
                                    (math.cos(math.radians(x)) * 15,
                                     math.sin(math.radians(x)) * 15))
                             for x in range(0, 180)], 2)
    pass


rect(screen, (0, 0, 0), offset(CENTER, (-CENTER[0], -15)) + (WIDTH, CENTER[1]))
ellipse(screen, (210, 210, 210), (WIDTH - 140, 10, 130, 100))

for i in range(6):
    ellipse(clouds, [randint(60, 110)]*3 + [randint(100, 255)],
            offset(CENTER, (randint(-WIDTH//2, WIDTH//2),
                            -(160 + randint(0, 100))))
            + (300, 75))

screen.blit(clouds, (0, 0) + (WIDTH, HEIGHT))
factory(offset(CENTER, (-100, 0)))
ghost(screen, offset(CENTER, (120, 50)))

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
