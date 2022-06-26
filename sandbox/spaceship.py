import os
import time
import random

import pygame


from src.conf import *
from src.spaceship import SpaceShip
from src.board import Board
from src.utils import *

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

pygame.font.init()  # you have to call this at the start,
my_font = pygame.font.SysFont("Comic Sans MS", 30)

# board
board = Board(bg_fn, font=my_font)

# spacesships
yellow = SpaceShip("y", y_spaceship_fn, board)
red = SpaceShip("r", r_spaceship_fn, board)


def main():
    """main function"""

    # display
    WIN = pygame.display.set_mode(WIN_SIZE)
    pygame.display.set_caption(("First Game!"))

    # clock
    clock = pygame.time.Clock()

    # main loop
    run = True
    while run:

        # tick
        clock.tick(FPS)

        for event in pygame.event.get():

            # quit
            if event.type == pygame.QUIT:
                run = False

            # fire
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:

                    yellow.fire()
                if event.key == pygame.K_RSHIFT:

                    red.fire()

        # update bullets
        red.update_bullets()
        yellow.update_bullets()

        # key_press Mooves
        keys_pressed = pygame.key.get_pressed()
        yellow.moove(keys_pressed)
        red.moove(keys_pressed)

        # collision
        manage_collistions(yellow, red, board)

        # window
        draw_window(board, WIN, yellow, red)

        # manage end_game
        run = manage_endgame(run, yellow, red)

    # quit
    pygame.quit()


if __name__ == "__main__":
    main()
