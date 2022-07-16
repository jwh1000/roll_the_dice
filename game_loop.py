import pygame
import random
from Tile import Tile
from Player import Player

WIDTH = 1280
HEIGHT = 720
FPS = 30
BG = pygame.image.load("assets/bg_placeholder.jpg")

BOARD = []


def initialize():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    BOARD = build_board()


def build_board():
    board = []

    for i in range(0, 30):
        tile = Tile()
        board.append(tile)

    return board


def render_screen():
    # background (color is placeholder)
    pygame.display.get_surface().blit(BG, (0, 0))


def run_game():
    initialize()

    pygame.display.set_caption("TITLE")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

        render_screen()

        pygame.display.update()
