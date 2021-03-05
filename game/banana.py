import pygame
import random


class Banana(pygame.sprite.Sprite):
    """ This class represents the Bananas that the Monkey collects in the game. """

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/banana.png')  # citation for image can be found in txt file within the assignment folder.
        self.rect = self.image.get_rect()  # allows to get x and y points for image
        self.rect.x = 656
        self.rect.y = random.randint(300, 600)  # can spawn anywhere between this range

    def reset(self):
        """ reset's the banana and its position in the game. """
        self.rect.x = 656
        self.rect.y = random.randint(300, 600)

    def update(self):
        """ update banana(s) in game. """
        self.rect.centerx -= 4
        if self.rect.x < 0:
            self.reset()
