import pygame
import random


class Leopard(pygame.sprite.Sprite):
    """ This class represents the Obstacle(s) the Monkey encounters while looking for Bananas. """

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/leopard.png')  # citation for image can be found in txt file within the assignment folder.
        self.rect = self.image.get_rect()  # same thing applies from other classes
        self.rect.x = 656

    def update(self):
        """ update leopard(s) in game. """
        self.rect.centerx -= 5
        if self.rect.x < 0:
            self.rect.x = 656
