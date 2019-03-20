import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """ To update the screen and show it. """
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    aliens.draw(screen)
    pygame.display.flip()


def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


# bullets functions
def update_bullets(ai_settings, screen, aliens, ship, bullets):
    manage_bullets(bullets)
    check_collision(bullets, aliens)
    if len(aliens) == 0:
        create_fleet(ai_settings, screen, aliens, ship)
    bullets.update()


def check_collision(bullets, aliens):
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)


def manage_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


# to create alien fleet
def create_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(ai_settings, screen)
    nx = get_nx(ai_settings, alien)
    ny = get_ny(ai_settings, alien, ship)
    # print(number_aliens)
    for j in range(ny):
        for i in range(nx):
            alien = Alien(ai_settings, screen)
            alien.rect.x = alien.rect.width + i * 2 * alien.rect.width
            alien.rect.y = alien.rect.height + j * 2 * alien.rect.height
            alien.x = float(alien.rect.x)
            alien.y = float(alien.rect.y)
            aliens.add(alien)


def get_nx(ai_settings, alien):
    x_valid = ai_settings.screen_width - 2 * alien.rect.width
    nx = int(x_valid / (2 * alien.rect.width))
    return nx


def get_ny(ai_settings, alien, ship):
    y_valid = ai_settings.screen_height \
                        - 3 * alien.rect.height - ship.rect.height
    ny = int(y_valid / (3 * alien.rect.height))
    return ny


# to update alien fleet
def update_fleet(ai_settings, stats, screen, aliens, ship, bullets):
    check_fleet_edge(ai_settings, aliens)
    check_fleet_bottom(ai_settings, stats, screen, aliens, ship, bullets)
    check_ship_collision(ai_settings, stats, screen, aliens, ship, bullets)
    aliens.update()


def check_fleet_edge(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            fleet_change_direction(ai_settings, aliens)
            break


def fleet_change_direction(ai_settings, aliens):
    ai_settings.fleet_direction *= -1
    for alien in aliens.sprites():
        alien.y += ai_settings.fleet_drop_speed
        alien.rect.y = alien.y


# functions that cause failure
def check_fleet_bottom(ai_settings, stats, screen, aliens, ship, bullets):
    for alien in aliens.sprites():
        if alien.rect.bottom >= alien.screen_rect.bottom:
            print("The alien fleet has passed!")
            ship_hit(ai_settings, stats, screen, aliens, ship, bullets)
            break


def check_ship_collision(ai_settings, stats, screen, aliens, ship, bullets):
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship crash!")
        ship_hit(ai_settings, stats, screen, aliens, ship, bullets)


def ship_hit(ai_settings, stats, screen, aliens, ship, bullets):
    if stats.ship_left <= 0:
        stats.reset_stats()
    else:
        aliens.empty()
        bullets.empty()
        ship.center_ship()
        create_fleet(ai_settings, screen, aliens, ship)
        sleep(0.5)
        stats.ship_left -= 1
        # print("ship left:" + str(stats.ship_left))
        # print("Game active:" + str(stats.game_active))
