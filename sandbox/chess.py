import pygame
from itertools import product


SCREEN_SIZE = 12
screen_width, screen_height = SCREEN_SIZE, SCREEN_SIZE

WIN_SIZE = 20
win_width, win_height = WIN_SIZE, WIN_SIZE

scaling_factor = 100

x, y = 0, 0
rect_width, rect_height = 1, 1
vel = 2
black = (0, 0, 0)
white = (255, 255, 255)
green = "#73965C"
# pygame.init()
win = pygame.display.set_mode(
    (screen_width * scaling_factor, screen_height * scaling_factor)
)

screen = pygame.Surface((screen_width, screen_height))

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(green)

    for x in range(0, SCREEN_SIZE, 2):
        for y in range(0, SCREEN_SIZE, 2):
            pygame.draw.rect(screen, white, (x, y, rect_width, rect_height))
    for x in range(1, SCREEN_SIZE, 2):
        for y in range(1, SCREEN_SIZE, 2):
            pygame.draw.rect(screen, white, (x, y, rect_width, rect_height))

    win.blit(pygame.transform.scale(screen, win.get_rect().size), (0, 0))
    pygame.display.update()
pygame.quit()
