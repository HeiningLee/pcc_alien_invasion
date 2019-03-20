import pygame

class Ship:
    def __init__(self, screen, ai_settings):
        """ To initialize the ship image,
            and give the surface(screen) where it's posted on"""
        self.screen = screen
        self.ai_settings = ai_settings

        # To load ship image and get it's surrounding rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # To put every ship in the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

        self.centerx = float(self.rect.centerx)

    def blitme(self):
        """ Draw the ship in position. """
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.centerx <= self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.centerx >= self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor

        # To adjust self.rect.centerx according to self.centerx
        self.rect.centerx = self.centerx

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
