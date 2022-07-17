import random
import pygame.sprite


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.is_animating = False

        self.identity = random.randrange(0, 3)
        # gold tile
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

    def override_identity(self, type):
        if not type:
            self.image = pygame.image.load("assets/tile_placeholder3.jpg")
            self.identity = 2
        else:
            self.image = pygame.image.load("assets/tile_placeholder_end.jpg")
            self.identity = -1

    def animate(self):
        self.is_animating = True

    def update(self):
        print("updated tiles")