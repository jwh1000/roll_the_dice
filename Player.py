import pygame

BASE_HP = 20


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.location = 0
        self.health = BASE_HP
        self.money = 0

        self.sprites = []
        self.sprites.append(pygame.image.load("assets/cup_h1.png"))
        self.sprites.append(pygame.image.load("assets/cup_h2.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.left = -20
        self.rect.top = 260

    def update(self):
        self.current_sprite += 0.03

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
