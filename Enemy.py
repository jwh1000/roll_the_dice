import random
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, location, board_size):
        pygame.sprite.Sprite.__init__(self)

        if location < board_size / 4:
            rand_num = random.randrange(0, 10)
            if rand_num < 5:
                self.health = 10
                self.attack = 1
                self.name = "easy enemy"
                self.image = pygame.image.load("assets/rock.png")
            elif rand_num < 8:
                self.health = 15
                self.attack = 1
                self.name = "medium enemy"
                self.image = pygame.image.load("assets/rock.png")
            else:
                self.health = 6
                self.attack = 2
                self.name = "hard enemy"
                self.image = pygame.image.load("assets/rock.png")
        elif location < board_size / 2:
            rand_num = random.randrange(0, 10)
            if rand_num < 3:
                self.health = 10
                self.attack = 1
                self.name = "easy enemy"
                self.image = pygame.image.load("assets/rock.png")
            elif rand_num < 7:
                self.health = 15
                self.attack = 1
                self.name = "medium enemy"
                self.image = pygame.image.load("assets/rock.png")
            else:
                self.health = 6
                self.attack = 2
                self.name = "hard enemy"
                self.image = pygame.image.load("assets/rock.png")
        else:
            rand_num = random.randrange(0, 10)
            if rand_num < 2:
                self.health = 10
                self.attack = 1
                self.name = "easy enemy"
                self.image = pygame.image.load("assets/rock.png")
            elif rand_num < 5:
                self.health = 15
                self.attack = 1
                self.name = "medium enemy"
                self.image = pygame.image.load("assets/rock.png")
            else:
                self.health = 6
                self.attack = 2
                self.name = "hard enemy"
                self.image = pygame.image.load("assets/rock.png")

        self.message = ""

        self.rect = self.image.get_rect()
        self.rect.right = 1276
        self.rect.top = 260

    def fight(self):
        if self.attack == 1:
            return random.randrange(0, 3)
        elif self.attack == 2:
            return random.randrange(1, 4)

