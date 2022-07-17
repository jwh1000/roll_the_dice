import random
import pygame.sprite


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.is_animating = False
        self.distance_to_move = 0

        self.identity = random.randrange(0, 3)
        # gold tile
        if self.identity == 0:
            self.image = pygame.image.load("assets/heart_tile.jpg")
        # combat tile
        elif self.identity == 1:
            self.image = pygame.image.load("assets/sword_tile.jpg")
        # plain tile
        elif self.identity > 1:
            self.image = pygame.image.load("assets/blank_tile.jpg")

        # make a rectangle around the sprite image (assigned above)
        self.rect = self.image.get_rect()
        self.rect.centerx = 93
        self.rect.top = 497

    def override_identity(self, type):
        if not type:
            self.image = pygame.image.load("assets/blank_tile.jpg")
            self.identity = 2
        else:
            self.image = pygame.image.load("assets/tile_placeholder_end.jpg")
            self.identity = -1

    def update(self):
        self.rect.left -= 2
