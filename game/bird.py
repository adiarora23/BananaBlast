import pygame
import random


class Bird(pygame.sprite.Sprite):
    """ This class represents the Birds that the Monkey has to avoid while looking for Bananas. """

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/bird.png')  # citation for image can be found in txt file within the assignment folder.
        self.rect = self.image.get_rect() # same thing applies (from monkey, banana, and bird class)
        self.rect.x = 656
        self.rect.y = random.randint(300, 600)

    def update(self):
        """ update bird(s) in game. """
        self.rect.centerx -= 6
        if self.rect.x < 0:
            self.rect.x = 656
            self.rect.y = random.randint(100, 600)
