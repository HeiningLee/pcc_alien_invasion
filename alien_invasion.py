import pygame
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
from pygame.sprite import Group



def run_game():
    pygame.init()
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create a ship
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, aliens, ship, bullets)
            gf.update_fleet(ai_settings, stats, screen, aliens, ship, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
