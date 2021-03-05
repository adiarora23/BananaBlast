"""
Use this class when running the Banana Blast game!
"""

import pygame
from game import *

if __name__ == "__main__":
    g = Game()
    print("Starting game...")
    g.run()
    print("Thanks for playing! Shutting down...")
    pygame.quit()
