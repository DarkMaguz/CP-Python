import pygame
import time
import random

pygame.init()

displayWidth = 800
displayHeight = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Rock Paper Scissor")
clock = pygame.time.Clock()

handsImage = pygame.image.load("hands.png").convert_alpha()
handsImage = pygame.transform.scale(handsImage, (displayWidth, displayHeight))

thumbImage = pygame.image.load("thumb.png").convert_alpha()
thumbImage = pygame.transform.scale(thumbImage, (displayWidth, displayHeight))

handOptions = {"Rock":1,"Paper":2,"Scissor":3}
handPowers = {1:3, 2:1, 3:2}
handImageRect = {"Rock":(540, 100, 260, 190), "Paper":(120, 320, 350, 280), "Scissor":(0, 0, 350, 220)}

npcScore = 0
playerScore = 0

def end_game():
    pygame.quit()
    quit()

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def draw_text(text, size, textColor):
    font = pygame.font.Font("freesansbold.ttf", size)
    TextSurf, TextRect = text_objects(text, font, textColor)
    TextRect.center = ((displayWidth/2), (displayHeight/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def splash_screen(text, size, textColor, bgColor, displayTime):
    gameDisplay.fill(bgColor)
    draw_text(text, size, textColor)
    
    time.sleep(displayTime)
    gameDisplay.fill(black)
    pygame.display.update()

def draw_score():
    global npcScore, playerScore
    #print("The score is now %d to you and %d to the NPC." % (playerScore, npcScore))
    text = "%d - %d" % (playerScore, npcScore)
    font = pygame.font.Font("freesansbold.ttf", 50)
    TextSurf, TextRect = text_objects(text, font, blue)
    TextRect.center = ((displayWidth-100), (50))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def clear_screen(color=black):
    gameDisplay.fill(black)
    draw_score()

def draw_hands():
    clear_screen()
    gameDisplay.blit(handsImage, (0, 0))

def choose_hand():
    draw_hands()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print("mouse pressed at: %d,%d" % event.pos)
                x, y = event.pos
                for hand, rect in handImageRect.items():
                    if x >= rect[0] and x <= rect[0] + rect[2]:
                        if y >= rect[1] and y <= rect[1] + rect[3]:
                            return hand
        pygame.display.update()
        clock.tick(30)

def draw_hand_vs(player, npc):
    #print ("%s vs. %s" % (player, npc))
    clear_screen()
    gameDisplay.blit(handsImage, (0, 0), handImageRect[player])
    pygame.display.update()
    time.sleep(0.5)
    
    draw_text("VS.", 150, white)
    time.sleep(0.5)
    
    x = displayWidth - handImageRect[npc][2]
    y = displayHeight - handImageRect[npc][3]
    gameDisplay.blit(handsImage, (x, y), handImageRect[npc])
    pygame.display.update()
    time.sleep(2)

def draw_outcome(player, npc):
    global playerScore, npcScore
    clear_screen()
    if playerChoice == npcChoice:
        #print("Draw!")
        draw_text("Draw!", 250, white)
    else:
        image = thumbImage
        if handPowers[handOptions[playerChoice]] == handOptions[npcChoice]:
            #print("You won this hand!")
            playerScore += 1
        else:
            #print("You lost this hand!")
            npcScore += 1
            image = pygame.transform.flip(image, False, True)
        gameDisplay.blit(image, (0, 0))
    pygame.display.update()
    time.sleep(1)

splash_screen("Welcome!", 120, white, black, 1)
splash_screen("Lets play Rock Paper Scissor!", 50, white, black, 2)

while True:
    playerChoice = choose_hand()
    
    npcChoice = random.choice(handOptions.keys())
    
    draw_hand_vs(playerChoice, npcChoice)
    
    draw_outcome(playerChoice, npcChoice)
        
    clear_screen()
    

end_game()
