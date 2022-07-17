import pygame
import random
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
        self.BG = pygame.image.load("assets/bg_sky__placeholder.jpg")

        self.BOARD = []
        self.BOARD_SIZE = 100
        self.VISIBLE_TILES = pygame.sprite.Group()
        self.COMBAT_SPRITES = pygame.sprite.Group()
        self.OTHER_SPRITES = pygame.sprite.Group()
        self.PLAYER = Player()
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

        for i in range(0, 15):
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
    def render_board_screen(self):
        screen = pygame.display.get_surface()
        screen.blit(self.BG, (0, 0))

        # draw each tile
        x_val = 94
        index = self.PLAYER.location
        for i in range(0, 7):
            tile = self.BOARD[index]
            tile.rect.centerx = x_val

            self.VISIBLE_TILES.add(tile)

            index += 1
            x_val += 182

        self.VISIBLE_TILES.draw(screen)
        self.VISIBLE_TILES.empty()

        self.OTHER_SPRITES.draw(screen)
        self.OTHER_SPRITES.update()

    def render_combat_UI(self):
        screen = pygame.display.get_surface()

        # background (color is placeholder)
        screen.blit(self.BG, (0, 0))

        self.COMBAT_SPRITES.draw(screen)




    def start_combat(self):
        pygame.display.set_caption("COMBAT")
        running = True

        current_enemy = Enemy(self.PLAYER.location, self.BOARD_SIZE)
        self.COMBAT_SPRITES.add(current_enemy)

        while running:
            self.CLOCK.tick(self.FPS)

            self.render_combat_UI()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print(current_enemy.name )
                        running = False

        self.COMBAT_SPRITES.empty()

    def run_game(self):
        self.initialize()
        pygame.display.set_caption("TITLE")

        self.OTHER_SPRITES.add(self.PLAYER)

        while True:
            self.CLOCK.tick(self.FPS)

            self.render_board_screen()

            pygame.display.update()

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
                    self.start_combat()
            self.STANDBY = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dice_result = roll_dice()
                        self.STANDBY = True
                        print("rolled a " + str(dice_result))
                        print(self.PLAYER.location)
                        self.PLAYER.location += dice_result
