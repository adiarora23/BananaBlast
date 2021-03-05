import pygame
import random


class Monkey(pygame.sprite.Sprite):
    """ This class represents the Monkey (Player) in the game. """

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/monkey.png')  # citation for image can be found in txt file within the assignment folder.
        self.jump = False  # initialize if the Monkey is jumping
        self.rect = self.image.get_rect()  # allows to get x and y points for image
        self.rect.x = 70  # this is arbitrary (positions the monkey in correct place)
        self.velocity = 21  # initialize velocity

    def collides_with(self, sprite):
        """ used to check if the Monkey collides with a certain sprite (could be a bird, banana, or leopard). """
        return self.rect.colliderect(sprite.rect)

    def do_jump(self, velocity):
        """ lets the Monkey jump in the game. """
        if self.jump is True:
            self.rect.y -= self.velocity  # lets the Monkey jump up
            self.velocity -= 1
            if self.velocity < -velocity:  # when the Monkey reaches the highest point of the jump, change direction (fall)
                self.jump = False
                self.velocity = velocity  # reset velocity to initial amount

    def update(self):
        """ update Monkey in game. """
        position = pygame.key.get_pressed()

        if (position[pygame.K_SPACE] or position[pygame.K_UP]) and self.jump is False:
            self.jump = True

        self.do_jump(21)  # call function here
