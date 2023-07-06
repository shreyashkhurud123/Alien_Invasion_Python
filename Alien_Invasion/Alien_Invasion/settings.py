'''Instead of giving some hard coded values and changing it later in the entire code which will be very time consuming and troublesome
    we are going to create a class which will manage all the settings parameter so even if we have to change later we only need to make 
    changes in this file
'''
class settings:
    def __init__(self) -> None:
        #screen
        self.width = 1200
        self.height = 800
        self.bg_color = ("cyan")

        #ship
        self.ship_speed_factor= 2.0
        self.ship_limit = 3

        #Bullets
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 25,25,112
        self.bullets_allowed = 5

        #alien
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        #Amount by which difficulty of game should be increased
        self.speedup = 1.2

        self.initialize_dynamic_settings()

        self.alien_points = 50

    #These are the initial settings of game
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 2.0
        self.bullet_speed_factor = 2
        self.alien_speed = 0.5
        self.fleet_direction = 1
    
    #This function is called when player completes certain level . It increases the difficulty of the game 
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup
        self.bullet_speed_factor *= self.speedup
        self.alien_speed *= self.speedup 
        self.alien_points *= self.speedup
        print(self.alien_points)