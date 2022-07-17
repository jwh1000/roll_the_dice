import random

import pygame


class Dice(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.is_animating = False
        self.loops = 2
        self.value = 0

        self.number_sprites = []
        self.number_sprites.append(pygame.image.load("assets/1.png"))
        self.number_sprites.append(pygame.image.load("assets/2.png"))
        self.number_sprites.append(pygame.image.load("assets/3.png"))
        self.number_sprites.append(pygame.image.load("assets/4.png"))
        self.number_sprites.append(pygame.image.load("assets/5.png"))
        self.number_sprites.append(pygame.image.load("assets/6.png"))

        self.animation_sprites = []
        self.animation_sprites.append(pygame.image.load("assets/dice_roll_1.png"))
        self.animation_sprites.append(pygame.image.load("assets/dice_roll_2.png"))
        self.animation_sprites.append(pygame.image.load("assets/dice_roll_3.png"))
        self.animation_sprites.append(pygame.image.load("assets/dice_roll_4.png"))
        self.animation_sprites.append(pygame.image.load("assets/dice_roll_5.png"))
        self.animation_sprites.append(pygame.image.load("assets/dice_roll_6.png"))
        self.animation_sprites.append(pygame.image.load("assets/dice_roll_7.png"))

        for image in range(len(self.number_sprites)):
            self.number_sprites[image] = pygame.transform.scale(self.number_sprites[image], (200, 200))
        for image in range(len(self.animation_sprites)):
            self.animation_sprites[image] = pygame.transform.scale(self.animation_sprites[image], (200, 200))

        self.current_sprite = 0
        self.image = self.number_sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.centerx = 640
        self.rect.top = 20

    def animate(self):
        self.is_animating = True
        self.loops = 2

    def roll(self):
        self.value = random.randrange(1, 7)
        return self.value

    def update(self):
        if self.is_animating and self.loops > 0:
            self.current_sprite += 0.5

            if self.current_sprite >= len(self.animation_sprites):
                self.current_sprite = 0
                self.loops -= 1

            self.image = self.animation_sprites[int(self.current_sprite)]

        else:
            self.image = self.number_sprites[self.value - 1]
            self.is_animating = False
