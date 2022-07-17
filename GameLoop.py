import sys

import pygame
import random

from Button import Button
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
        self.BOARD_SIZE = 10
        self.VISIBLE_TILES = pygame.sprite.Group()
        self.COMBAT_SPRITES = pygame.sprite.Group()
        self.ANIMATED_SPRITES = pygame.sprite.Group()
        self.PLAYER = Player()
        self.DICE = Dice()
        self.TURN_COUNT = 0
        self.STANDBY = False

        self.CLOCK = pygame.time.Clock()
        self.FONT = pygame.font.Font("assets/font.ttf", 35)

        self.PLAYER_HP_BAR_SURFACE = self.FONT.render("PLAYER HP: " + str(self.PLAYER.health),
                                                      True, pygame.Color("white"))
        self.ENEMY_HP_BAR_SURFACE = self.FONT.render("ENEMY HP: " + str(0),
                                                     True, pygame.Color("white"))

        self.MESSAGE = ""
        self.MESSAGE_SURFACE = self.FONT.render(self.MESSAGE, True, pygame.Color("white"))

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
        self.PLAYER = Player()

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
        self.DICE.rect.top = 20

        screen = pygame.display.get_surface()
        screen.blit(self.BG, (0, 0))

        self.PLAYER_HP_BAR_SURFACE = self.FONT.render("PLAYER HP: " + str(self.PLAYER.health),
                                                      True, pygame.Color("white"))
        screen.blit(self.PLAYER_HP_BAR_SURFACE, (5, 5))

        self.MESSAGE_SURFACE = self.FONT.render(self.MESSAGE, True, pygame.Color("white"))
        message_rect = self.MESSAGE_SURFACE.get_rect(center=(640, 360))
        screen.blit(self.MESSAGE_SURFACE, message_rect)

        self.VISIBLE_TILES.draw(screen)
        self.ANIMATED_SPRITES.draw(screen)
        self.ANIMATED_SPRITES.update()

    def move_tiles(self, amount_to_move):
        screen = pygame.display.get_surface()

        while amount_to_move > 0:
            screen.blit(self.BG, (0, 0))
            screen.blit(self.PLAYER_HP_BAR_SURFACE, (5, 5))

            self.VISIBLE_TILES.draw(screen)
            self.ANIMATED_SPRITES.draw(screen)
            self.VISIBLE_TILES.update()
            self.ANIMATED_SPRITES.update()
            amount_to_move -= 2
            pygame.display.update()

    def render_combat_UI(self):
        screen = pygame.display.get_surface()

        # background (color is placeholder)
        screen.blit(self.BG, (0, 0))

        self.PLAYER_HP_BAR_SURFACE = self.FONT.render("PLAYER HP: " + str(self.PLAYER.health),
                                                      True, pygame.Color("white"))
        screen.blit(self.PLAYER_HP_BAR_SURFACE, (5, 5))

        screen.blit(self.ENEMY_HP_BAR_SURFACE, (860, 5))

        self.MESSAGE_SURFACE = self.FONT.render(self.MESSAGE, True, pygame.Color("white"))
        message_rect = self.MESSAGE_SURFACE.get_rect(center=(640, 360))
        screen.blit(self.MESSAGE_SURFACE, message_rect)

        self.COMBAT_SPRITES.draw(screen)

        self.ANIMATED_SPRITES.draw(screen)
        self.ANIMATED_SPRITES.update()

    def start_combat(self):
        pygame.display.set_caption("COMBAT")
        running = True
        enemy_attack = False

        current_enemy = Enemy(self.PLAYER.location, self.BOARD_SIZE)
        self.COMBAT_SPRITES.add(current_enemy)

        self.DICE.rect.bottom = 700

        self.ENEMY_HP_BAR_SURFACE = self.FONT.render("ENEMY HP: " + str(current_enemy.health),
                                                     True, pygame.Color("white"))

        self.MESSAGE = "An enemy appeared!"

        while running:
            self.CLOCK.tick(self.FPS)

            self.render_combat_UI()

            pygame.display.update()

            if not enemy_attack:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if current_enemy.health >= 0:
                                self.DICE.animate()

                                dice_result = self.DICE.roll()

                                self.MESSAGE = "Dealt " + str(dice_result) + " damage!"

                                current_enemy.health -= dice_result
                                self.ENEMY_HP_BAR_SURFACE = self.FONT.render("ENEMY HP: " + str(current_enemy.health),
                                                                             True, pygame.Color("white"))
                                enemy_attack = True
            else:
                pygame.event.wait()
                pygame.event.clear()
                pygame.event.wait()
                damage = current_enemy.fight()
                self.PLAYER.health -= damage
                self.MESSAGE = "Enemy dealt " + str(damage) + " damage!"
                enemy_attack = False
                print(self.PLAYER.health)

            if current_enemy.health <= 0:
                self.MESSAGE = "Defeated the enemy!"
                running = False

            if self.PLAYER.health <= 0:
                self.game_over()

            self.render_combat_UI()

        self.COMBAT_SPRITES.empty()

    def game_over(self):
        screen = pygame.display.get_surface()

        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            self.DICE.rect.top = 20

            screen = pygame.display.get_surface()
            screen.blit(pygame.image.load("assets/bg_placeholder.jpg"), (0, 0))

            self.MESSAGE_SURFACE = self.FONT.render("Game Over...", True, pygame.Color("white"))
            message_rect = self.MESSAGE_SURFACE.get_rect(center=(640, 360))
            screen.blit(self.MESSAGE_SURFACE, message_rect)

            BACK_BUTTON = Button(image=pygame.image.load("assets/quit_button_placeholder.jpg"), pos=(640, 600),
                                 text_input="RETRY (doesnt work)", font=self.FONT, base_color="#d7fcd4", hovering_color="White")

            for button in [BACK_BUTTON]:
                button.change_color(MENU_MOUSE_POS)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.check_for_input(MENU_MOUSE_POS):
                        self.run_game()

            pygame.display.update()

            pygame.display.update()

    def run_game(self):
        self.initialize()
        pygame.display.set_caption("On The Roll!")

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
                    heal = self.PLAYER.heal()
                    self.MESSAGE = "Healed " + str(heal) + "!"
                    self.PLAYER.health += heal


                # combat tile
                elif self.BOARD[self.PLAYER.location].identity == 1:
                    self.start_combat()
                    pass
            self.STANDBY = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:

                        self.DICE.animate()

                        dice_result = self.DICE.roll()

                        self.MESSAGE = "Rolled a " + str(dice_result) + "!"

                        self.move_tiles(dice_result * 180)

                        self.STANDBY = True

                        self.PLAYER.location += dice_result

            if self.PLAYER.health <= 0:
                self.game_over()

            if self.PLAYER.location > self.BOARD_SIZE:
                self.MESSAGE = "You win!"
                self.update_board_screen()
                pygame.display.update()
                pygame.event.wait()
                pygame.event.clear()
                pygame.event.wait()
                sys.exit()

            self.update_board_screen()
            pygame.display.update()
