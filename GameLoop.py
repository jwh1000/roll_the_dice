import pygame
import random

from Dice import Dice
from Tile import Tile
from Player import Player
from Enemy import Enemy


def roll_dice():
    return random.randrange(1, 7)


class GameLoop:
    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.FPS = 60
        self.BG = pygame.image.load("assets/bg.png")

        self.DISTANCE_TO_MOVE = 0
        self.BOARD = []
        self.BOARD_SIZE = 100
        self.VISIBLE_TILES = pygame.sprite.Group()
        self.COMBAT_SPRITES = pygame.sprite.Group()
        self.ANIMATED_SPRITES = pygame.sprite.Group()
        self.PLAYER = Player()
        self.DICE = Dice()
        self.TURN_COUNT = 0
        self.STANDBY = False

        self.CLOCK = pygame.time.Clock()

    def build_board(self):
        board = []

        tile = Tile()
        tile.override_identity(False)
        board.append(tile)

        for i in range(0, self.BOARD_SIZE - 2):
            tile = Tile()
            board.append(tile)

        for i in range(0, 20):
            tile = Tile()
            tile.override_identity(True)
            board.append(tile)

        return board

    def initialize(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.BOARD = self.build_board()

    # draws the whole board (off screen)
    def init_board_screen(self):
        screen = pygame.display.get_surface()
        screen.blit(self.BG, (0, 0))

        # draw each tile
        x_val = 0
        index = self.PLAYER.location
        for i in range(0, self.BOARD_SIZE):
            tile = self.BOARD[index]
            tile.rect.left = x_val

            self.VISIBLE_TILES.add(tile)

            index += 1
            x_val += 180

        self.VISIBLE_TILES.draw(screen)

        self.ANIMATED_SPRITES.draw(screen)
        self.ANIMATED_SPRITES.update()

    def update_board_screen(self):
        screen = pygame.display.get_surface()
        screen.blit(self.BG, (0, 0))

        self.VISIBLE_TILES.draw(screen)
        self.ANIMATED_SPRITES.draw(screen)
        self.ANIMATED_SPRITES.update()

    def move_tiles(self, amount_to_move):
        screen = pygame.display.get_surface()

        while amount_to_move > 0:
            self.VISIBLE_TILES.draw(screen)
            self.VISIBLE_TILES.update()
            amount_to_move -= 2
            pygame.display.update()

    def render_combat_UI(self):
        screen = pygame.display.get_surface()

        # background (color is placeholder)
        screen.blit(self.BG, (0, 0))

        self.COMBAT_SPRITES.draw(screen)

        self.ANIMATED_SPRITES.draw(screen)
        self.ANIMATED_SPRITES.update()

    def start_combat(self):
        pygame.display.set_caption("COMBAT")
        running = True

        current_enemy = Enemy(self.PLAYER.location, self.BOARD_SIZE)
        self.COMBAT_SPRITES.add(current_enemy)

        while running:
            self.CLOCK.tick(self.FPS)

            self.render_combat_UI()

            pygame.display.update()

            while self.DICE.is_animating:
                print("Waiting...")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print(current_enemy.name)
                        running = False

        self.COMBAT_SPRITES.empty()

    def run_game(self):
        self.initialize()
        pygame.display.set_caption("TITLE")

        self.ANIMATED_SPRITES.add(self.PLAYER)
        self.ANIMATED_SPRITES.add(self.DICE)

        self.init_board_screen()

        while True:
            self.CLOCK.tick(self.FPS)

            # check current tile's identity:
            # blank tile
            if self.STANDBY:
                if self.BOARD[self.PLAYER.location].identity == 2:
                    pass
                # gold tile
                elif self.BOARD[self.PLAYER.location].identity == 0:
                    pass
                # combat tile
                elif self.BOARD[self.PLAYER.location].identity == 1:
                    # self.start_combat()
                    pass
            self.STANDBY = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.DICE.animate()

                        dice_result = self.DICE.value

                        self.move_tiles(dice_result * 180)

                        self.STANDBY = True

                        self.PLAYER.location += dice_result

            self.update_board_screen()

            pygame.display.update()
