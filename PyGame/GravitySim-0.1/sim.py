#!/usr/bin/python3

import pygame
import time

from settings import *
from sprites import Rocket

pygame.init()

## initialize pygame and create a window
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Spice Sim 0.1")
clock = pygame.time.Clock()

# Load sprites
myRocket = Rocket(5, 5)
myRocket.rect.x = displayWidth / 2
myRocket.rect.y = displayHeight / 1.3

## group all the sprites together for ease of update
allSprites = pygame.sprite.Group()
allSprites.add(myRocket)

gameExit = False
while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        myRocket.moveRight()
    if keys[pygame.K_LEFT]:
        myRocket.moveLeft()
    if keys[pygame.K_UP]:
        myRocket.moveUp()
    if keys[pygame.K_DOWN]:
        myRocket.moveDown()

    gameDisplay.fill(black)
    allSprites.update()
    allSprites.draw(gameDisplay)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
