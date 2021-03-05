import pygame
import random


class Cherry(pygame.sprite.Sprite):
    """ This class represents the cherries the Monkey can collect to increase their jump velocity. """

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/cherry.png')  # citation for image can be found in txt file within the assignment folder.
        self.rect = self.image.get_rect()
        self.rect.x = 656
        self.rect.y = random.randint(400, 600)  # can spawn anywhere between this range
        self.velocity = 35

    def update(self):
        """ update the cherries in game. """
        self.rect.centerx -= 8
        if self.rect.x < 0:
            self.rect.x = 656
            self.rect.y = random.randint(300, 600)
