#import the pygame module, and the
#sys module for exiting the window we create
import sys
import pygame
import random

#import some useful constants
from pygame.locals import *


#initialise the pygame module
pygame.init()

#add a font for our inventory
INVFONT = pygame.font.Font('FreeSansBold.ttf', 18)

#give the window a caption
pygame.display.set_caption('Monopoly')

DISPLAYSURF = pygame.display.set_mode((800,600))

while True:

    #get all the user events
    for event in pygame.event.get():
        #~ print(event)
        #if the user wants to quit
        if event.type == QUIT:
            #and the game and close the window
            pygame.quit()
            sys.exit()
        #if a key is pressed
        elif event.type == KEYDOWN:
            #if the right arrow is pressed
            if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH - 1:
                #change the player's x position
                playerPos[0] += 1
            elif (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT - 1:
                #change the player's y position
                playerPos[1] += 1
            elif (event.key == K_UP) and playerPos[1] > 0:
                #change the player's y position
                playerPos[1] -= 1
            elif (event.key == K_LEFT) and playerPos[0] > 0:
                #change the player's y position
                playerPos[0] -= 1
            elif event.key == K_SPACE:
                #what resource is the player standing on?
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                #player now has 1 more of this resource
                inventory[currentTile] += 1
                #the player is now standing on rock
                tilemap[playerPos[1]][playerPos[0]] = ROCK
                #~ print(inventory
            
            elif (event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
   

    

    #update the display
    pygame.display.update()
