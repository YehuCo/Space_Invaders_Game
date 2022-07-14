import json

class GameStats:
    """Track statistics for Space Invaders"""

    def __init__(self, si_game):
        """Initialize statistics"""
        self.settings = si_game.settings
        self.reset_stats()

        # Start the game in an inactive state
        self.game_active = False

        # Store high score in a file
        file = "high_score.json"
        with open(file, 'r+') as f:
            self.high_score = json.load(f)


    def reset_stats(self):
        """Initialize statistics that can change  during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
