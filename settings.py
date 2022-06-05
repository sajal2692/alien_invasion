class Settings():
    """A class to store all settings for Alient Invasion"""

    def __init__(self):
        """Initialize the game settings."""
        
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        self.fleet_direction = 1 # 1 == right, -1 == left
        
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5