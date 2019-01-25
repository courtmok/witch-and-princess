import pygame
import constants

BLACK = (0,0,0)

class SpriteSheet(object):
    
    def __init__(self, file_name):
        #constructor, load sprite sheet
        self.sprite_sheet = pygame.image.load(file_name).convert()

    #get the image out of the sheet
    def get_image(self, x, y, width, height):
        #new blank image
        image = pygame.Surface([width,height]).convert()

        image.blit(self.sprite_sheet, (0,0), (x,y, width, height))

        #transparent color
        image.set_colorkey(BLACK)
        """image = pg.tranform.scale(image,
                                  (int(rect.width*constants.SIZE_MULTIPLIER),
                                   int(rect.height*c.SIZE_MULTIPLIER)))"""

        return image
        
