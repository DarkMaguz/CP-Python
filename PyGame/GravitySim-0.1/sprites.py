import pygame

from settings import *

class SpritePhysics():
    def __init__(self):
        super(SpritePhysics, self).__init__()
        self.speedX = 0
        self.speedY = 0
        #self.mass = 1

    def update(self):
        # Apply gravity
        self.speedY += GRAVITY / FPS

class Rocket(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Rocket, self).__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill((255,255,255))

        self.rect = self.image.get_rect()

        self.phys = SpritePhysics()
        self.acceleration = 2

    def update(self):
        self.phys.update()
        self.rect.x += self.phys.speedX
        self.rect.y += self.phys.speedY

    def moveRight(self):
        self.phys.speedX += self.acceleration

    def moveLeft(self):
        self.phys.speedX -= self.acceleration

    def moveUp(self):
        self.phys.speedY -= self.acceleration

    def moveDown(self):
        self.phys.speedY += self.acceleration
