''' This python Module will store number of different functions which will make the game work and prevent the main game file from getting too lengthy
    This module will hold most of the game logic
'''
import sys
import pygame
from Bullet import bullet
from Alien import Alien
from time import sleep
#from pygame.constants import K_w

#from Alien_Invasion.ship import Ship


'''
The following function is to check which key is pressed when a key is pressed and act accordingly
'''
def check_keydown_events(event,ai_settings, screen , ship , bullets):
    #if the right key or 'd' key is pressed keep moving the ship right
    if event.key == pygame.K_RIGHT  or event.key == pygame.K_d:
        ship.rect.centerx += 1
        ship.moving_right = True
    
    #if the left key or 'a' key is pressed keep moving the ship left
    if event.key == pygame.K_LEFT  or event.key == pygame.K_a:
        ship.rect.centerx -= 1
        ship.moving_left = True

    #if space is pressed fire a bullet ie. create a bullet and add it in bullets group
    if event.key == pygame.K_SPACE and len(bullets) < ai_settings.bullets_allowed:
        new_bullet = bullet(ai_settings , screen , ship)
        bullets.add(new_bullet)
    

'''
The keyup function is to stop the movement of the ship in that direction if its already on
'''
def check_keyup_events(event,ship):
    #stop movement to right if the right or d key is up
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False

    #stop movement to left if the left or d key is up
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False


#To check if the created play button is pressed by the player or not
def check_play_button(ai_settings,screen, stats , sb ,play_button , ship , aliens ,bullets , mouse_x , mouse_y):

    #Check whether the mouse pressed position collides with the play button position 
    if play_button.rect.collidepoint(mouse_x , mouse_y) and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        #initialize initial settings of the game
        pygame.mouse.set_visible(False)
        #set cursor visibility to off
        stats.reset_stats()
        #reset stats 
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        #emptying aliens and bullets group as a new start
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        #keeping the ship starting position to the middle
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_ship()
        sb.prep_level()
        #displaying the score ,high score ,Ship_lives and current_level


        

# this is to check key press or quit game event is triggered by the player
def check_events(ai_settings,screen,stats, play_button, ship , sb , aliens, bullets):

    for event in pygame.event.get():
        #Check whether the player closed the window and Quit then program in background also
        #pygame.quit is triggered when the player closes pygame window 
        if event.type == pygame.QUIT:
            sys.exit()

        #check if any key is pressed by using teh pygame.KEYDOWN which detects whether key is pressed
        elif (event.type == pygame.KEYDOWN):
            check_keydown_events(event,ai_settings,screen, ship , bullets)    

        #check if any key is up by using the pygame.KEYup which detects whether key press is undone
        elif (event.type == pygame.KEYUP):
            check_keyup_events(event,ship)

        #check if mouse button us pressed then get the position by pygame.mouse.get_pos() a pygame function and then make a call to check play button function 
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            mouse_x , mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen, stats , sb , play_button , ship , aliens ,bullets , mouse_x , mouse_y)
    

#updating screen with current situation of the screen 
def update_screen(ai_settings , screen ,stats,sb, ship , aliens, bullets ,play_button):
    screen.fill(ai_settings.bg_color)
    #Fill the Surface with a solid color. If no rect argument is given the entire Surface will be filled.

    #draw bullets on screen
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #if game is not active show Play button else show score , ship and aliens
    if not stats.game_active:
        play_button.draw_button()
    else:
        sb.show_score()
        ship.blitme()
        aliens.draw(screen)
    pygame.display.flip()
    #pygame.display.flip updates the entire screen

#check bullets position and situation whether its hit of out of bound
def update_bullets( ai_settings , screen ,stats , sb, ship,  aliens , bullets):
    bullets.update()
    #for bullet in bullets.copy():
    #check if bullet got out of bound 
    for bullet in bullets:
        if bullet.rect.bottom <0:
            bullets.remove(bullet)
    #print(len(bullets))

    #check if bullet collide with alien.
    #pygame.sprite.groupcollide(group1, group2, dokill1, dokill2) :- Find all sprites that collide between two groups. where dokill is to destroy both alien and bullet by setting true
    collisions = pygame.sprite.groupcollide(bullets,aliens,True , True)
    # It returns a dictionary where both the elements that colloided are stored


    if collisions:
        #print(collisions.values())
        #Just to be fair we are checking all the hits even if the are at exact same time by two different bullets
        
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points

        # if current score is greater than high score set that to the high score
        if stats.score > stats.high_score:
            stats.high_score = stats.score
            #print(stats.high_score)
        
        sb.prep_score()
        sb.prep_high_score()

    #if we get all the aliens from the screen 
    if len(aliens) == 0:
        #destroy all bullets from screen so it wont hit upcoming aliens
        bullets.empty()
        # increasing difficulty of the game 
        ai_settings.increase_speed()
        #create a new fleet of aliens
        create_fleet(ai_settings , screen , ship, aliens )
        stats.level+=1
        sb.prep_level()
        

# to check how many aliens we can fit onto the screen and return the number
def get_number_aliens_x(ai_settings , alien_width): 
    available_space_x = ai_settings.width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x

# to check how many aliens we can fit vertically 
def get_number_rows(ai_settings , ship_height , alien_height):
    available_space_y = (ai_settings.height - (3*alien_height))
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

#Creating a single alien 
def create_alien(ai_settings , screen , aliens , alien_number , row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    #aligning the alien in a sequentially numbered position 
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)
    #adding that alien to sprite_group


def update_aliens( ai_settings , stats , screen , ship ,sb , aliens , bullets):
    #aliens.update()
    check_fleet_edges(ai_settings , aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        print("Ship Hit!!!")
    #if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings , stats , screen , ship , sb, aliens , bullets)
    check_aliens_bottom(ai_settings , stats , screen , ship , sb , aliens , bullets)

#creating fleet of alien
def create_fleet(ai_settings, screen, ship, aliens ):
    alien = Alien(ai_settings , screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height , alien.rect.height)
    #creating an alien and getting the number of aliens we can fit horizontally and vertically

    #dual for loop to form a patern of creating aliens 
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number , row_number)
    
#checking edges of the aliens and changing direction if it's about to hit the edge of either side
def check_fleet_edges(ai_settings , aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

#changing the direction of fleet and dropping it by certain value
def change_fleet_direction(ai_settings , aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

#def update_aliens(ai_settings ,ship, aliens):
    

#when ship gets hit by an alien
def ship_hit(ai_settings, stats , screen , ship , sb ,aliens , bullets):
    stats.ship_left -= 1
    sb.prep_ship()
    #check if number of lives player has left is greater than zero
    if stats.ship_left >0:
        #reset bullets and aliens if lives are left 
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings ,screen , ship , aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        #if no lives set the game active parameter to False and show mouse cursor
        stats.game_active = False
        pygame.mouse.set_visible(True)

#check if alien hits the bottom
def check_aliens_bottom(ai_settings , stats , screen , ship , sb , aliens , bullets):
    screen_rect = screen.get_rect()
    #check for every alien
    for alien in aliens.sprites():
        #if an alien hits the bottom of the screen then call ship hit function as both needs to run same set of codes 
        if(alien.rect.bottom >= screen_rect.bottom):
            ship_hit(ai_settings , stats , screen , ship , sb ,aliens , bullets)
            break