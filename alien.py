import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to represent a single alien in the fleet"""

    def __init__(self, si_game):
        """Initialize alien and set its starting position"""
        super().__init__()
        self.clock = pygame.time.Clock()
        self.screen = si_game.screen
        self.settings = si_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("C:/Users/yehud/Documents/Space_Invaders/images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each alien at top left of the screen
        self.rect.x = self.rect.width/2
        self.rect.y = self.rect.height/2

        # Store the aliens's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left"""
        self.rect.x += (self.settings.alien_speed * self.settings.fleet_direction)
        #self.rect.x = self.x
