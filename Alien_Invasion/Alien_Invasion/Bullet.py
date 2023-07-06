'''this module is to create and manage bullets.
'''
import pygame
from pygame.sprite import Sprite
class bullet(Sprite):
    def __init__(self, ai_settings , screen , ship ) :
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width , ai_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    #Updating bullet's position according to its speed factor
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    #this function is to draw the bullet onto the screen
    def draw_bullet(self):
        pygame.draw.rect(self.screen , self.color , self.rect)
