import os
import time
import random
import logging

import pygame


from src.conf import *

logging.basicConfig(
    filename="example.log",
    level=logging.DEBUG,
    filemode="w",
    format="%(levelname)s - %(message)s",
)

from src.apple import Apple
from src.board import Board
from src.snake import Snake
from src.window import *

#
from src.game import Game


def main():
    """main"""

    game = Game(WIN, SCREEN, "m")
    game.run()


if __name__ == "__main__":
    main()
