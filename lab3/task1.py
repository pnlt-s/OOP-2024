import pygame
from pygame.draw import (rect, line, circle)

pygame.init()

TICKRATE = 30
HEIGHT = 300
WIDTH = 300


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((128, 128, 128))

CENTER = (WIDTH//2, HEIGHT//2)


def offset(point, offset):
    return (point[0] + offset[0], point[1] + offset[1])


def circleOutline(scr, center, color, radius):
    circle(scr, color, center, radius)
    circle(scr, (0, 0, 0), center, radius, 1)


EYE1 = offset(CENTER, (-45, -25))
EYE2 = offset(CENTER, (43, -25))

MOUTH = offset(CENTER, (-50, 40)) + (100, 25)

BROW1 = offset(EYE1, (20, -20))
BROW2 = offset(EYE2, (-20, -20))
# make smiley face here
circleOutline(screen, CENTER, (255, 255, 0), 100)
circleOutline(screen, EYE1, (255, 0, 0), 20)
circle(screen, (0, 0, 0), EYE1, 10)

circleOutline(screen, EYE2, (255, 0, 0), 18)
circle(screen, (0, 0, 0), EYE2, 7)

rect(screen, (0, 0, 0), MOUTH)

line(screen, (0, 0, 0), BROW1, offset(BROW1, (-75, -25)), 10)
line(screen, (0, 0, 0), BROW2, offset(BROW2, (75, -25)), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(TICKRATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
