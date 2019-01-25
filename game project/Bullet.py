import pygame
import constants
from create_spritesheet import SpriteSheet

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

class Bullet(pygame.sprite.Sprite):
        def __init__(self):
             super().__init__()

             sprite_sheet = SpriteSheet("spritesheet1.png")
             image = sprite_sheet.get_image(1528, 734, 89, 33)
             self.image = pygame.transform.flip(image, True, False)
           
             self.rect = self.image.get_rect()
        def update(self):
             self.rect.x += 6 
