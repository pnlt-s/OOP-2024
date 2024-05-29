from pygame.draw import circle, ellipse
import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


def draw_body(surface, x, y, width, height, color):
    '''
    Рисует тело зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_head(surface, x, y, size, color):
    '''
    Рисует голову зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    size - диаметр головы
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    circle(surface, color, (x, y), size // 2)


def draw_ear(surface, x, y, width, height, color):
    '''
    Рисует ухо зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_leg(surface, x, y, width, height, color):
    '''
    Рисует ногу зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_hare(surface, x, y, width, height, color):
    '''
    Рисует зайца на экране
    surface - объект pygame.Surface
    x, y - координаты левого верхнего края изображения
    width, height - ширина и высота изображения
    color - цвет кролика
    '''
    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2
    draw_body(surface, x, body_y, body_width, body_height, color)

    head_size = height // 4
    draw_head(surface, x, y - head_size // 2, head_size, color)

    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    for ear_x in (x - head_size // 4, x + head_size // 4):
        draw_ear(surface, ear_x, ear_y, width // 8, ear_height, color)

    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    for leg_x in (x - width // 4, x + width // 4):
        draw_leg(surface, leg_x, leg_y, width // 4, leg_height, color)


draw_hare(screen, 200, 200, 200, 200, (200, 200, 200))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

event_handlers = dict()  # каждый обработчик события следует добавлять сюда


while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type in event_handlers.keys():
            event_handlers[event.type](event)
    deltaTime = clock.tick(FPS)
pygame.quit()
