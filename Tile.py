import random
import pygame.sprite


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.identity = random.randrange(0, 4)
        # blank tile
        if self.identity == 0:
            self.image = pygame.image.load("assets/tile_placeholder1.jpg")
        # combat tile
        elif self.identity == 1:
            self.image = pygame.image.load("assets/tile_placeholder2.jpg")
        # plain tile
        elif self.identity > 1:
            self.image = pygame.image.load("assets/tile_placeholder3.jpg")

        # make a rectangle around the sprite image (assigned above)
        self.rect = self.image.get_rect()
        self.rect.centerx = 93
        self.rect.top = 497

    def tile_effect(self):
        if self.identity == 0:
            pass
        elif self.identity == 1:
            pass
