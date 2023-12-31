'''This module is to create button and draw that button o screen when necessary
'''
import pygame

class Button:
    def __init__(self , ai_settings , screen , msg) -> None:
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width , self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,52)
        
        self.rect = pygame.Rect(0,0,self.width , self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    #creating function to create a rect image of the button
    def prep_msg(self,msg):
        #font.render is used to create an image where the image is created which surrounds text 
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    #drawing that button on screen
    def draw_button(self):
        self.screen.fill(self.button_color , self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
    
