'''This module is created to keep track of score and display it on the right position of the screen
'''
import pygame
from pygame.sprite import Group
from ship import Ship

class Scoreboard:

    def __init__(self , ai_setting , screen , stats) -> None:
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_setting
        self.stats = stats

        self.text_color = (90,90,90)
        self.font = pygame.font.SysFont(None,23)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()


    #To create a display of level where we are creating an image of level number 
    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str , True , self.text_color , self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.top = self.score_rect.bottom +20
        self.level_rect.centerx = self.score_rect.centerx

    #creating a display of the current score and giving it co-ordinates to get drawn on screen
    def prep_score(self):
        score_str = str(int(self.stats.score))
        self.score_image = self.font.render(score_str , True , self.text_color,self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -30
        self.score_rect.top = 30
    
    #creating a display of high score with co-ordinates planted in this function
    def prep_high_score(self):
        #print(self.stats.high_score)
        high_score_str = str("High Socre: " + str( int(self.stats.high_score) ))

        self.high_score_image = self.font.render(high_score_str , True , self.text_color , self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    #displaying number of lives ie. ships left with the player before game over
    def prep_ship(self):
        self.ships = Group()
        for ship_n in range(self.stats.ship_left):
            ship = Ship(self.ai_settings,self.screen , 27 , 48)
            ship.rect.x = 10+ship_n *ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    #Now this function is to actually display the images we created in all previous functions
    def show_score(self):
        self.screen.blit(self.score_image , self.score_rect)
        self.screen.blit(self.high_score_image , self.high_score_rect)
        self.screen.blit(self.level_image , self.level_rect)
        self.ships.draw(self.screen)
        #self.screen.blit()


    
