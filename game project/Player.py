import pygame
from platforms import *
from constants import *
from create_spritesheet import SpriteSheet
"""SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600"""

class Player(pygame.sprite.Sprite) :
        #stuff!!
        def __init__(self):
            super().__init__()

            """#change this later to use sprites
            width = 40
            height = 60
            self.image = pygame.image.load("player.png").convert()

            self.rect = self.image.get_rect()"""
        #def load_images(self):
            #set speed vector
            self.change_x = 0
            self.change_y = 0

            #create walking frame arrays
            self.walk_frames_l = []
            self.walk_frames_r = []
            self.jump_frames = []
            self.attack_frame = []

            self.direction = "R"

            #List sprites we can bump against
            self.level = None

            sprite_sheet = SpriteSheet("spritesheet1.png")
            #all left facing walking stuff
            #stand
            image = sprite_sheet.get_image(1257, 221, 163, 226)
            self.walk_frames_l.append(image)
            #walk 1
            image = sprite_sheet.get_image(1075, 221, 161, 226)
            self.walk_frames_l.append(image)
            #walk 2
            image = sprite_sheet.get_image(890, 220, 163, 226)
            self.walk_frames_l.append(image)
            #walk 3
            image = sprite_sheet.get_image(699, 220, 167, 225)
            self.walk_frames_l.append(image)
            #walk 2
            image = sprite_sheet.get_image(890, 220, 163, 226)
            self.walk_frames_l.append(image)
            #walk 1
            image = sprite_sheet.get_image(1075, 221, 161, 226)
            self.walk_frames_l.append(image)

                #same as above but flip it
            for frame in self.walk_frames_l:
                    image = pygame.transform.flip(frame, True, False)
                    self.walk_frames_r.append(image)
            #attack left
            image = sprite_sheet.get_image(502, 222, 163, 225)
            self.attack_frame.append(image)
            #attack right
            image = sprite_sheet.get_image(502, 222, 163, 225)
            image = pygame.transform.flip(image, True, False)    
            self.attack_frame.append(image)
            

            #jump left
            image = sprite_sheet.get_image(1439, 220, 222, 218)
            self.jump_frames.append(image)
            #jump right
            image = sprite_sheet.get_image(1439, 220, 222, 218)
            image = pygame.transform.flip(image, True, False)
            self.jump_frames.append(image)
            
            

            #set direction
            #self.frame_index = 0
            #self.image = self.walk_frames_r[self.frame_index]
            self.image = self.walk_frames_r[0]
            

            self.rect = self.image.get_rect()

        def update(self):
            self.calc_grav()

            self.rect.x += self.change_x
            
                #if you are jumping or falling
            if self.change_y != 0:
                    if self.direction == "R":
                            self.image = self.jump_frames[1]
                    elif self.direction == "L":
                            self.image = self.jump_frames[0]
                        
            # See if we hit anything
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:
                # If we are moving right,
            # set our right side to the left side of the item we hit
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                    self.rect.left = block.rect.right

            #up/down
            self.rect.y += self.change_y

            # Check and see if we hit anything
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom
                    
                #if you're on a block, walk!
                self.rect.x += self.change_x
                pos = self.rect.x + self.level.world_shift
                if self.direction == "R":
                    frame = (pos//30) % len(self.walk_frames_r)
                    self.image = self.walk_frames_r[frame]

                else:
                    frame = (pos//30) % len(self.walk_frames_l)
                    self.image = self.walk_frames_l[frame]
                    
            # Stop our vertical movement
                self.change_y = 0
                #check for moving platform
                if isinstance(block, MovingPlat):
                        self.rect.x += block.change_x
                #see if we hit anything

        def calc_grav(self):
            #calculate gravity
            if self.change_y == 0:
                self.change_y = 1
            else:
                self.change_y += .7

            if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = SCREEN_HEIGHT - self.rect.height

        def jump(self):
                #see if there is a platfrom below us
            self.rect.y += 2
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y -= 2
                
            if len(platform_hit_list) >0 or self.rect.bottom >= SCREEN_HEIGHT:
                self.change_y = -16
        

        def go_left(self):
            self.change_x = -6
            self.direction = "L"
        def go_right(self):
            self.change_x = 6
            self.direction = "R"
        def stop(self):
            self.change_x = 0
