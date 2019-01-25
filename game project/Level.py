import pygame
#import platforms
from platforms import *
from Player import *
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Level():
    def __init__(self, player):
        self.platform_list = None
        #self.enemy_list = None
        self.background = None

        #world shift
        self.world_shift = 0
        self.world_shifty = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.player = player
        #self.enemy_list = pygame.sprite.Group()
        
    def update(self):
        self.platform_list.update()
        #self.enemy_list.update()

    def draw(self, screen):
        background = pygame.image.load("back.png").convert()
        screen.blit(background, [0,0])

        self.platform_list.draw(screen)

    def shift_world(self, shift_x):
        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x
        '''for enemy in self.enemy.list:
            enemy.rect.x += shift_x'''
        
    def shift_worldy(self, shift_y):
        self.world_shifty += shift_y

        for platform in self.platform_list:
            platform.rect.y += shift_y
            
