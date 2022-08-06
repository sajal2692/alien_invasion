import json
class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialise the statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an active state
        self.game_active = False
        # Reading highscore from json file
        try:
            with open('high_score.json', 'r') as file:
                high_score = json.load(file)
                self.high_score = int(high_score['HighScore'])
        except:
            self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1