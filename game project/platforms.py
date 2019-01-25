import pygame
from create_spritesheet import * #SpriteSheet

FLOOR_TL = (794, 794, 210, 171)
FLOOR_TM = (1070, 790, 209,172)
FLOOR_TR = (1339, 794, 210,172)
FLOOR_BL = (798, 1080, 209, 173)
FLOOR_BM = (1070, 1082, 209, 173)
FLOOR_BR = (1334, 1074, 209, 174)
FLOOR_ML = (819, 1415, 209, 173)
FLOOR_MR = (1375, 1419, 209, 173)
CLOUD_L = (941, 1324, 170, 63)
CLOUD_M = (1133, 1323, 201, 70)
CLOUD_R = (1343, 1331, 158, 58)
CLOUD_MOVE = (564, 1325, 324, 63)
KEYBOX = (1175, 1439, 123, 123)


BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        super().__init__()

        sprite_sheet = SpriteSheet("spritesheet1.png")
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
                                            
        """self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)"""

        self.rect = self.image.get_rect()
        
class MovingPlat(Platform):

     def __init__(self, sprite_sheet_data):
         super().__init__(sprite_sheet_data)
    
         self.change_x = 0
         self.change_y = 0

         self.bound_top = 0
         self.bound_bot = 0
         self.bound_left = 0
         self.bound_right = 0

         self.player = None
         self.level = None

     def update(self):
           #left/right  
           self.rect.x += self.change_x
           hit = pygame.sprite.collide_rect(self, self.player)
           if hit:
                if self.change_x <0:
                        self.player.rect.right = self.rect.left
                else:
                        self.player.rect.left = self.rect.right
           #up/down
           self.rect.y += self.change_y
           hit = pygame.sprite.collide_rect(self, self.player)
           if hit:
               if self.change_y < 0:
                       self.player.rect.bottom = self.rect.top
               else:
                       self.player.rect.top = self.rect.bottom

           if self.rect.bottom > self.bound_bot or self.rect.top < self.bound_top:
                   self.change_y *= -1
           cur_pos = self.rect.x - self.level.world_shift
           if cur_pos < self.bound_left or cur_pos > self.bound_right:
                   self.change_x *= -1
