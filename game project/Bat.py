import pygame
import math
import constants
from Player import *

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Bat(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        
    def move_to_player(self, player):
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx/dist, dy/dist

        self.rect.x += dx *self.speed
        self.rect.y += dy*self.speed
        
