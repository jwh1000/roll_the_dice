import pygame

BASE_HP = 20


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.location = 0
        self.health = BASE_HP
        self.money = 0
