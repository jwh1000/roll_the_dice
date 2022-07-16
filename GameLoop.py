import pygame
import random
from Tile import Tile
from Player import Player


def roll_dice():
    return random.randrange(1, 7)


class GameLoop:
    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.FPS = 30
        self.BG = pygame.image.load("assets/bg_sky__placeholder.jpg")

        self.BOARD = []
        self.BOARD_SIZE = 100
        self.VISIBLE_SPRITES = pygame.sprite.Group()
        self.PLAYER = Player()
        self.TURN_COUNT = 0
        self.ANIMATING = False;

    def build_board(self):
        board = []

        tile = Tile()
        tile.override_identity(False)
        board.append(tile)

        for i in range(0, self.BOARD_SIZE - 2):
            tile = Tile()
            board.append(tile)

        for i in range(0, 10):
            tile = Tile()
            tile.override_identity(True)
            board.append(tile)

        return board

    def initialize(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.BOARD = self.build_board()

    def render_static_screen(self):
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
        self.VISIBLE_SPRITES.empty()

    def render_animating_screen(self):
        screen = pygame.display.get_surface()

        # background (color is placeholder)
        screen.blit(self.BG, (0, 0))

        # draw each tile
        x_val = 94
        index = self.PLAYER.location

        for i in range(0, 7):
            tile = self.BOARD[index]
            tile.rect.centerx = x_val

        self.VISIBLE_SPRITES.draw(screen)

    def start_combat(self):
        pygame.display.set_caption("COMBAT")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dice_result = roll_dice()

    def run_game(self):
        self.initialize()
        pygame.display.set_caption("TITLE")

        while True:
            if not self.ANIMATING:
                # check current tile's identity:
                # blank tile
                if self.BOARD[self.PLAYER.location].identity == 2:
                    pass
                # gold tile
                elif self.BOARD[self.PLAYER.location].identity == 0:
                    pass
                # combat tile
                elif self.BOARD[self.PLAYER.location].identity == 1:
                    pass

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            dice_result = roll_dice()
                            print("rolled a " + str(dice_result))
                            print(self.PLAYER.location)
                            self.PLAYER.location += dice_result

                self.render_static_screen()

                pygame.display.update()
            else:
                self.render_animating_screen()
