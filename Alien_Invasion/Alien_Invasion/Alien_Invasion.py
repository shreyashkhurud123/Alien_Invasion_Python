import pygame
from button import Button
from Bullet import bullet
from ship import Ship
from pygame.sprite import Group  #Group is a subclass of pygame sprite class which acts as  A container class to hold and manage multiple Sprite objects.
import game_function as gf # Module creates by us to get the functions which will make the game work
from settings import settings 
from Alien import Alien
from game_stats import GameStats
from Scoreboard import Scoreboard

'''we are creating a function named run_game from where the game execution will start.
    we dont need to run other python files but this to run the game
'''
def run_game():

    pygame.init()
    '''it is the initialize function of pygame which initializes background settings that Pygame needs to work properly
    '''

    ai_settings = settings()
    ''' Creating an instance of settings.py after importing it'''

    screen = pygame.display.set_mode((ai_settings.width , ai_settings.height))
    '''when we call pygame.display.set_mode it creates a window which takes a tupple as an arguments and create a window accordingly to the given width and hight into the tupple'''

    pygame.display.set_caption("Alien_Invasion")
    ''' So instead of keeping the window nameless we are naming the window by our game_name'''

    play_button = Button(ai_settings,screen,"Play")
    '''Creating an instance of Button class from button.py . Used to create a play button before staring the game'''
    
    stats = GameStats(ai_settings)
    ''''creating an instance of Gamestats class from game_stats.py . Used for creating game stats '''

    sb = Scoreboard(ai_settings,screen,stats)
    '''creating an instance of scoreboard class from scoreboard.py. Used to keep scores and high_scores of the game'''

    ship = Ship(ai_settings, screen)
    '''Creating an instance of Ship from ship.py. Used to create a player ship which will later shoot bullets to destroy alien ships'''

    bullets = Group()
    '''Group is a subclass of pygame sprite class which acts as  A container class to hold and manage multiple Sprite objects.
        We are going to use this group to keep track of all the bullets on the screen and destroy those who left the screen
    '''

    aliens = Group()
    ''' 
        we are going to create a sprite group to keep track of all the alien_ships on the screen and give them movement
        and destroy those ship which got hit by the player's bullet
    '''

    #alien = Alien(ai_settings,screen)
    '''creating an instance of alien class from Alien.py. Used to create alien which later is used to create fleet'''

    gf.create_fleet(ai_settings,screen,ship ,aliens)
    ''' A function from game_function which will create a fleet of alien_ships  '''

    
    while True:
        '''In this while loop we are writing certain lines of codes which will run every frame ie. screen updates'''
        
        gf.check_events(ai_settings,screen,stats, play_button, ship ,sb , aliens ,bullets)
        '''Function for managing events in game like  key-presses'''

        if(stats.game_active):
        #This if loop is to check whether the game is active ie whether the player has pressed the play button or not
            ship.update()
            '''This function is from the ship function which lets us position the ship when controlled by the player'''

            gf.update_bullets(ai_settings, screen , stats ,sb , ship , aliens ,bullets)
            '''This function is from Game_function to update bullets position from bullets group and delete those bullets which hit alien or got out of range'''

            gf.update_aliens(ai_settings, stats , screen ,  ship, sb , aliens , bullets)
            '''this function is to update aliens position whether they get hit by bullets '''

        gf.update_screen(ai_settings,screen, stats, sb ,ship, aliens ,bullets,play_button)
        '''WHether the game is active or not this function runs either way as this function is display the current situation of the game'''


run_game()


