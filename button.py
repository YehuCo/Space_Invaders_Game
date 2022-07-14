import pygame.font

class Button:

    def __init__(self, si_game, msg):
        """Initialize button attributes"""
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()

        # Dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 230, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build button rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button text needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
