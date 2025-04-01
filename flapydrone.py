#little videogame Drone In the City
#import pygame
#created by Ada Catucci, images by Canva
import pygame
import random

#start build game
pygame.init ()

#import images
sky = pygame.image.load ('/home/lace/Documents/Drone/game/sky.png')
drone = pygame.image.load ('/home/lace/Documents/Drone/game/drone.gif')
base = pygame.image.load ('/home/lace/Documents/Drone/game/base.png')
gameover = pygame.image.load ('/home/lace/Documents/Drone/game/gameover.png')
building_down = pygame.image.load ('/home/lace/Documents/Drone/game/building.png')
building_up = pygame.transform.flip (building_down, False, True)

#global const
DISPLAY = pygame.display.set_mode ((288,512)) #display size with pixels
FPS = 60
VEL_AVANZ = 3
FONT = pygame.font.SysFont ('Thaoma', 50, italic=True)


class building_class:
        def  __init__(self):
            self.x = 300
            self.y = random.randint (-75, 150)
        def go_and_draw(self):
            self.x -= VEL_AVANZ
            DISPLAY.blit (building_down, (self.x, self.y+210))
            DISPLAY.blit (building_up, (self.x, self.y-210))
        def collision (self, drone, dronex, droney):
            tollerance = 5
            drone_right = dronex+drone.get_width () -tollerance
            drone_left = dronex+tollerance
            building_left = self.x + building_down.get_width ()
            building_right = self.x
            drone_up = droney+tollerance
            drone_down = droney+drone.get_height ()-tollerance
            building_up_side = self.y + 110
            building_down_side = self.y + 210
            if drone_right > building_right and drone_left < building_left:
                   if drone_up < building_up_side or drone_down > building_down_side:
                        game_over ()
        def bet_buildings (self, drone, dronex):
            tollerance = 5
            drone_right = dronex+drone.get_width () -tollerance
            drone_left = dronex+tollerance
            building_left = self.x + building_down.get_width ()
            building_right = self.x
            if drone_right > building_right and drone_left < building_left:
                   return True
            


def draw_objects ():
        DISPLAY.blit (sky, (0, 0))
        for t in buildings:
               t.go_and_draw()
        DISPLAY.blit (drone, (dronex, droney))
        DISPLAY.blit (base, (basex, 400))
        points_render = FONT.render(str(points), 1, (0, 0, 0))
        DISPLAY.blit (points_render, (144,0))



def update ():
        pygame.display.update ()
        pygame.time.Clock().tick(FPS)

def initialize ():
        global dronex, droney, drone_vely
        global basex
        global buildings
        global points
        global bet_buildings
        dronex, droney = 60, 150
        drone_vely = 0
        basex = 0
        points = 0
        buildings = []
        buildings.append (building_class())
        bet_buildings = False


def game_over ():
        DISPLAY.blit (gameover, (50, 180))
        update()
        restart = False
        while not restart:
               for event in pygame.event.get ():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                             initialize ()        
                             restart = True
                    if event.type == pygame.QUIT:
                             pygame.quit ()

#initialize variables
initialize ()

#principal cycle
while True:
        basex -= VEL_AVANZ
        if basex < -45: basex = 0
        #gravity
        drone_vely += 1
        droney += drone_vely
        #comands
        for event in pygame.event.get():
                if ( event.type == pygame.KEYDOWN
                    and event.key == pygame.K_UP):
                    drone_vely = -10
                if event.type == pygame.QUIT:
                    pygame.quit ()
        if buildings [-1] .x < 150: buildings.append (building_class ())
        for t in buildings:
               t.collision (drone, dronex, droney)

        if not bet_buildings:
               for t in buildings:
                      if t.bet_buildings (drone, dronex):
                             bet_buildings = True
                             break
        if bet_buildings: 
                bet_buildings = False
                for t in buildings:
                      if t.bet_buildings (drone, dronex):
                             bet_buildings = True
                             break
                if not bet_buildings:
                      points += +1


        if droney > 380:
               game_over()

        #update display
        draw_objects ()
        update ()
