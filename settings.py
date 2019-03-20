"""Store the settings the main function needs."""


class Settings:
    def __init__(self):
        """ Initializing game settings. """
        # settings of display
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = 130, 130, 230

        # settings of ship
        self.ship_speed_factor = 2
        self.ship_limit = 3

        # settings of bullets
        self.bullet_speed_factor = 2
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = 180, 225, 250
        self.bullets_allowed = 3

        # settings of alien fleet
        self.fleet_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

