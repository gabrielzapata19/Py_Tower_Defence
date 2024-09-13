import pygame as pg
import constants as c 
from enemy import Enemy

#initilize
pg.init()

#create clock
clock = pg.time.Clock()

#screen game window
screen = pg.display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))
pg.display.set_caption(c.TOP_TITLE)

#Load images
enemy_image = pg.image.load('assets/images/enemies/enemy1.jpeg').convert_alpha()
enemy_image = pg.transform.scale(enemy_image,(10,10))

#create groups
enemy_group = pg.sprite.Group()

waypoints = [
    (100,100),
    (400,200),
    (400,100),
    (200,200)
]

enemy = Enemy(waypoints, enemy_image)
enemy_group.add(enemy)


#game loop
run = True 
while run:

    clock.tick(c.FPS)
    
    screen.fill("grey50")

    #draw enemy path
    pg.draw.lines(screen,"grey0",False, waypoints)

    #update groups
    enemy_group.update()

    #draw groups
    enemy_group.draw(screen)


    #event Handler
    for event in pg.event.get():
        #quit program
        if event.type == pg.QUIT:
            run = False

    #update display
    pg.display.flip()

pg.quit()

