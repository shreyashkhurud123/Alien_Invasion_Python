'''This module is for creating and managing aliens
'''
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings , screen ) :
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('Alien_Invasion\Alien_Ship1.png')
        self.image=pygame.transform.scale(self.image , (60,60))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    #function to display alien on screen
    def blitme(self):
        self.screen.blit(self.image , self.rect)

    #function to check if alien is about to hit the edge.If yes return true 
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False
    
    #moving the alien to either right or left direction
    def update(self):
        self.x += (self.ai_settings.alien_speed * self.ai_settings.fleet_direction)
        self.rect.x = self.x

