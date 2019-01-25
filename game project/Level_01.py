import pygame
from Level import *
import platforms #from platforms import *
from Bat import *

class Level_01(Level):
    def __init__(self, player):

        Level.__init__(self, player)
        self.level_limit = -1000

        level = [[platforms.FLOOR_TL, -75, 600],
                 [platforms.FLOOR_TM, 131, 600],
                 [platforms.FLOOR_ML, 340, 600],
                 [platforms.FLOOR_TL, 340, 437],
                 [platforms.FLOOR_BM, 548, 600],
                 [platforms.FLOOR_ML, 548, 437],
                 [platforms.FLOOR_TL, 548, 274],
                 [platforms.FLOOR_TR, 754, 274],
                 [platforms.FLOOR_BR, 754, 437],
                 [platforms.FLOOR_MR, 754, 600],
                 [platforms.FLOOR_TM, 962, 600],
                 [platforms.FLOOR_TR, 1170, 600],
                 [platforms.CLOUD_MOVE, 1000, 120],
                 [platforms.CLOUD_L, 1280, -10],
                 [platforms.CLOUD_M, 1400, -10],
                 [platforms.CLOUD_R, 1590, -10]
                 ]
                
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        
            """block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)"""
            
        block = platforms.MovingPlat(platforms.CLOUD_MOVE)
        block.rect.x = 1800
        block.rect.y = -40
        block.bound_left = 1800
        block.bound_right = 2100
        block.change_x = 6
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        """bat1 = Bat(40,40)
        bat1.rect.x = 700
        bat1.rect.y = 400
        self.platform_list.add(bat1)"""
                
