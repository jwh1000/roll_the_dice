import pygame
import random
from Tile import Tile
from Player import Player


class GameLoop:
    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.FPS = 30
        self.BG = pygame.image.load("assets/bg_sky__placeholder.jpg")

        self.BOARD = []
        self.TILE_SPRITES = pygame.sprite.Group()
        self.VISIBLE_SPRITES = pygame.sprite.Group()
        self.PLAYER = Player()

    def build_board(self):
        board = []

        for i in range(0, 30):
            tile = Tile()
            board.append(tile)
            self.TILE_SPRITES.add(tile)

        return board

    def initialize(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.BOARD = self.build_board()

    def render_screen(self):
        screen = pygame.display.get_surface()

        # background (color is placeholder)
        screen.blit(self.BG, (0, 0))

        # draw each tile
        x_val = 94
        index = self.PLAYER.location

        for i in range(0, 7):
            tile = self.BOARD[index]
            tile.rect.centerx = x_val

            self.VISIBLE_SPRITES.add(tile)

            index += 1
            x_val += 182

        self.VISIBLE_SPRITES.draw(screen)

    def run_game(self):
        self.initialize()

        pygame.display.set_caption("TITLE")

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pass

            self.render_screen()

            pygame.display.update()
