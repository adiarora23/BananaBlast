"""
    Assignment 2: Pygame Arcade Game
    Game Name: Banana Blast (inspired by Google's Dinosaur run game)
    CCT 211
    Aditya Arora
"""

from monkey import *
from banana import *
from cherry import *
from bird import *
from leopard import *


class Game:
    """
    This class represents the actual game. This contains all the game objects created.

    Credit to TA for format used to structure this class (follows lab 05's format!)

    Please run the game from the main.py file!
    """

    def __init__(self):
        # === initialize the PyGame ===
        pygame.init()

        # === set screen width and height ===
        self.screen_width = 656
        self.screen_height = 875
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # === set booleans ===
        self.running = False
        self.game_over = False
        self.game_start = True

        # === create sprite groups ===
        self.all_sprites_list = pygame.sprite.Group()
        self.leopard_list = pygame.sprite.Group()
        self.bird_list = pygame.sprite.Group()
        self.banana_list = pygame.sprite.Group()
        self.cherry_list = pygame.sprite.Group()

        # === arbitrary: used for scrolling background ===
        self.x = 0
        self.y = random.randint(0, 600)

        # === create Monkey object ===
        self.monkey = Monkey()
        self.all_sprites_list.add(self.monkey)

        # === create "obstacles" (Bird and Leopard objects) ===
        self.bird = Bird()
        self.bird_list.add(self.bird)
        self.all_sprites_list.add(self.bird)

        self.leopard = Leopard()
        self.leopard_list.add(self.leopard)
        self.all_sprites_list.add(self.leopard)

        # arbitrary: setting the position of the leopard correctly for the game
        self.leopard.rect.y = self.screen_height - self.leopard.rect.height * 3

        # === create banana object(s) ===
        self.banana = Banana()

        self.banana.rect.x = random.randrange(self.screen_width)
        self.banana.rect.y = random.randrange(self.screen_height)

        self.banana_list.add(self.banana)
        self.all_sprites_list.add(self.banana)

        # === create cherry object(s) ===
        self.cherry = Cherry()

        self.cherry.rect.x = random.randrange(self.screen_width)
        self.cherry.rect.y = random.randrange(self.screen_height)

        self.cherry_list.add(self.cherry)
        self.all_sprites_list.add(self.cherry)

        # === initialize total score and total distance ===
        self.total_score = 0
        self.total_distance = 0

        # This is arbitrary so that the position of the monkey looks correct on the scrolling background
        self.monkey.rect.y = self.screen_height - self.monkey.rect.height * 3

    def reset_game(self):
        """ resets the game when a certain command is pressed (the r key in this case)"""
        self.game_over = False
        self.total_distance = 0
        self.total_score = 0

        # === set objects back in initial positions ===
        self.monkey.rect.x = 70
        self.bird.rect.x = 656
        self.leopard.rect.x = 656

    def start_game_screen(self):
        """ shows the start game screen before pressing the space key to play the game. """
        self.total_score = 0
        self.total_distance = 0
        self.bird.rect.x = 656
        self.leopard.rect.x = 656
        self.banana.rect.x = 656
        self.cherry.rect.x = 656

        # === showing the words used on the screen before playing ===
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        sg_text = font.render("Banana Blast", True, (255, 100, 0))
        cmd_text = font.render("Press the space bar to begin!", True, (255, 100, 0))
        self.screen.blit(sg_text,
                         (self.screen_width / 3, self.screen_height / 2))  # arbitrary: needed to get spacing correct
        self.screen.blit(cmd_text, (
            self.screen_width / 6, (self.screen_height / 2) + 50))  # arbitrary: needed to get spacing correct
        pygame.display.flip()

    def game_over_screen(self):
        """ displays the game over screen until the player decides to reset the game. """
        self.bird.rect.x = 656
        self.leopard.rect.x = 656
        self.banana.rect.x = 656
        self.cherry.rect.x = 656
        font = pygame.font.Font(pygame.font.get_default_font(), 25)
        go_text = font.render("Game Over. Press R to play again or Q to quit!", True, (255, 0, 0))
        self.screen.blit(go_text, (
            self.screen_width / 11, self.screen_height / 2))  # arbitrary: needed to get the spacing correct
        pygame.display.flip()

    def __reset_banana(self):
        """ resets the banana's position when the monkey collides with the banana (private method). """
        if self.monkey.collides_with(self.banana):
            self.banana = Banana()

            self.banana.rect.x = 656
            self.banana.rect.y = random.randint(100, 600)

            self.banana_list.add(self.banana)
            self.all_sprites_list.add(self.banana)

    def __reset_cherry(self):
        if self.monkey.collides_with(self.cherry):
            self.cherry = Cherry()

            self.cherry.rect.x = 656
            self.cherry.rect.y = random.randint(100, 600)

            self.cherry_list.add(self.cherry)
            self.all_sprites_list.add(self.cherry)

    def __reset_bird(self):
        """ resets the bird's position when the game restarts (private method). """
        if self.monkey.collides_with(self.bird):
            self.bird = Bird()

            self.bird.rect.x = 656
            self.bird.rect.y = random.randint(100, 600)

            self.bird_list.add(self.bird)
            self.all_sprites_list.add(self.bird)

    def __reset_leopard(self):
        """ resets the leopard's position when the game restarts (private method). """
        if self.monkey.collides_with(self.leopard):
            self.leopard = Leopard()

            self.leopard.rect.y = self.screen_height - self.leopard.rect.height * 3

            self.leopard_list.add(self.leopard)
            self.all_sprites_list.add(self.leopard)

    def __score(self, x, y):
        """ displays score for amount of bananas collected (private method). """
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        score = font.render("Bananas Collected: " + str(self.total_score), True, (255, 100, 0))
        self.screen.blit(score, (x, y))

    def __distance(self, x, y):
        """ displays distance for how long the monkey has survived (private method). """
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        distance = font.render("Score: " + str(self.total_distance), True, (255, 100, 0))
        self.screen.blit(distance, (x, y))

    def poll(self):
        """ event handling method. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and self.game_over is True:
                if event.key == pygame.K_r:
                    self.reset_game()
                if event.key == pygame.K_q:
                    self.running = False
            if event.type == pygame.KEYDOWN and self.game_start is True:
                if event.key == pygame.K_SPACE:
                    self.game_start = False

    def update(self):
        """ updates game with all the sprites included. """
        self.all_sprites_list.update()

        if not self.game_over:
            self.total_distance += 1

            banana_hit_list = pygame.sprite.spritecollide(self.monkey, self.banana_list, True)

            for each_banana in banana_hit_list:
                self.__reset_banana()  # private method used here!
                self.banana_list.remove(each_banana)
                self.all_sprites_list.remove(each_banana)
                self.total_score += 1

            cherry_hit_list = pygame.sprite.spritecollide(self.monkey, self.cherry_list, True)

            for each_cherry in cherry_hit_list:
                self.__reset_cherry()  # private method used here!
                self.cherry_list.remove(each_cherry)
                self.all_sprites_list.remove(each_cherry)
                self.total_score += 2

            leopard_hit_list = pygame.sprite.spritecollide(self.monkey, self.leopard_list, False)

            for each_leopard in leopard_hit_list:
                self.__reset_leopard()  # private method used here!
                self.leopard_list.remove(each_leopard)
                self.all_sprites_list.remove(each_leopard)
                self.game_over = True

            bird_hit_list = pygame.sprite.spritecollide(self.monkey, self.bird_list, False)

            for each_bird in bird_hit_list:
                self.__reset_bird()  # private method used here!
                self.bird_list.remove(each_bird)
                self.all_sprites_list.remove(each_bird)
                self.game_over = True

    def draw(self):
        """ draws game onto the screen. """
        jungle_img = pygame.image.load('images/jungle resized.jpg')
        rel_x = self.x % jungle_img.get_rect().width  # credit to https://www.youtube.com/watch?v=US3HSusUBeI&ab_channel=code.Pylet for helping with scrolling background

        self.screen.blit(jungle_img, (rel_x - jungle_img.get_rect().width, 0))

        if rel_x < self.screen_width:
            self.screen.blit(jungle_img, (rel_x, 0))
        self.x -= 2.5

        if self.game_over or self.game_start:
            self.screen.blit(jungle_img, (0, 0))

        self.__score(5, 5)
        self.__distance(540, 5)

        self.all_sprites_list.draw(self.screen)

    def run(self):
        """ runs the game. """
        self.running = True

        clock = pygame.time.Clock()

        while self.running:

            if self.game_start:
                self.start_game_screen()

            if self.game_over:
                self.game_over_screen()

            self.poll()

            self.update()

            self.draw()

            pygame.display.flip()

            pygame.display.set_caption('Banana Blast')

            clock.tick(60)
