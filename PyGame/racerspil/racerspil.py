import pygame
import time
import random
import math

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Super racer 0.1")
clock = pygame.time.Clock()

carImg = pygame.image.load("racer1.png")
car_width = carImg.get_rect().size[0]
car_height = carImg.get_rect().size[1]
car_speed = 10

global thing_color

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    textSurface = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(textSurface, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display("You Crashed!")

def crash_test(carx, cary, thingx, thingy, thing_width, thing_height):
    crashx = False
    crashy = False
    thing_color = blue

    if carx >= thingx and carx <= thingx + thing_width:
        crashx = True
    elif carx + car_width >= thingx and carx + car_width <= thingx + thing_width:
        crashx = True

    if cary >= thingy and cary <= thingy + thing_height:
        crashy = True
    elif cary + car_height >= thingy and cary + car_height <= thingy + thing_height:
        crashy = True
    
    return crashx and crashy

def q():
    pygame.quit()
    quit()

def game_loop():
    x = (display_width - car_width) / 2
    y = display_height * 0.8 #(display_height - car_height) / 2

    thing_speed = 5
    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(0, display_width - thing_width)
    thing_starty = -600
    thing_color = blue

    dodged = 0

    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x = x - car_speed
        if keys[pygame.K_RIGHT]:
            x = x + car_speed

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, thing_color)
        thing_starty = thing_starty + thing_speed
        
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()
            gameExit = True
            continue

        if thing_starty > display_height:
            dodged += 1
            thing_speed += 1
            #thing_width += (dodged * 1.2)
            thing_starty = -thing_width
            thing_startx = random.randrange(0, display_width - math.floor(thing_width))

        if crash_test(x, y, thing_startx, thing_starty, thing_width, thing_height):
            crash()
            gameExit = True
            continue

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
