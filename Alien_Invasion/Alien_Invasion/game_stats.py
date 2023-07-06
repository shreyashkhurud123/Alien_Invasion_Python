'''
This module keeps track of basic game stats and resets it when game is over 
'''
class GameStats:
    def __init__(self , ai_settings) -> None:
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.ship_left = self.ai_settings.ship_limit
        self.high_score = 0

    #function to reset stat usually when game is over
    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

