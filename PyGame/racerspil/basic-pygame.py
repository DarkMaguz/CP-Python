#!/usr/bin/python

import pygame
import time

pygame.init()

displayWidth = 800
displayHeight = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Lidt hurtigt")
clock = pygame.time.Clock()

gameExit = False

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        
        print(event)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
