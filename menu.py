# each menu has its OWN game loop
# I also yoinked this from a tutorial
import pygame, sys

from GameLoop import GameLoop
from Button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/start_screen.png")


def get_font(size):
    # temporary font
    return pygame.font.Font("assets/font.ttf", size)


def options_menu():
    pygame.display.set_caption("Options")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("OPTIONS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        BACK_BUTTON = Button(image=pygame.image.load("assets/quit_button_placeholder.jpg"), pos=(640, 600),
                             text_input="BACK", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [BACK_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.check_for_input(MENU_MOUSE_POS):
                    start_menu()

        pygame.display.update()


def pause_menu():
    # this does nothing for now
    return


def play_screen():
    new_game = GameLoop()
    new_game.run_game()


def start_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/play_button_placeholder.jpg"), pos=(960, 430),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        # OPTIONS_BUTTON = Button(image=pygame.image.load("assets/options_button_placeholder.jpg"), pos=(640, 400),
        #                         text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("assets/quit_button_placeholder.jpg"), pos=(960, 575),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    play_screen()
                # if OPTIONS_BUTTON.check_for_input(MENU_MOUSE_POS):
                #     options_menu()
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
