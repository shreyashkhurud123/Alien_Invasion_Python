'''this module is of the ship and is used for ship movements and to create a boundary beyond which the ship cant move
'''
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self , ai_settings , screen ,height = 54 , width = 96) -> None:
        self.screen = screen
        self.ai_settings = ai_settings

        super(Ship,self).__init__()

        self.image = pygame.image.load("Alien_Invasion\Spaceship1.png")
        self.image=pygame.transform.scale(self.image , (height ,width))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
    
    #displaying the ship onto the screen
    def blitme(self):
        #blit:-draw one image onto another
        self.screen.blit(self.image , self.rect)

    #updating ships position and checking whether ship is not moving it's boundary
    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            #adding ships speed to its moving direction 
            self.center += self.ai_settings.ship_speed_factor
            #self.rect.centerx+=1
        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed_factor
            #self.rect.centerx-=1
        self.rect.centerx = self.center

    #setting the ship's center to the screen center when called which is at the start of game
    def center_ship(self):
        self.center = self.screen_rect.centerx

