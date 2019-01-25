import pygame
import random
import constants
from Player import *
from Bullet import *
from platforms import *
from Level import *
from Level_01 import *

def main():
    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Witches!!")

    player = Player()

    level_list = []
    level_list.append(Level_01(player))

    current_level_no= 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    
    player.level = current_level

    #player.rect.x = -10
    #player.rect.y = 400
    player.rect.x = 760
    player.rect.y = 270
    active_sprite_list.add(player)

    done = False

    clock = pygame.time.Clock()

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #player movement    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_w:
                    player.jump()
                if event.key == pygame.K_SPACE: 
                   bullet = Bullet()
                   #location of the bullet
                   bullet.rect.x = player.rect.x + 117
                   bullet.rect.y = player.rect.y + 90
                   active_sprite_list.add(bullet)
                   bullet_list.add(bullet)
            #have the player stop moving       
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_d and player.change_x > 0:
                    player.stop()

        active_sprite_list.update()
        current_level.update()

        if player.rect.right >= 500:
                diff = player.rect.right - 500
                player.rect.right = 500
                current_level.shift_world(-diff)

        if player.rect.left <= 120:
                diff = 120 - player.rect.left
                player.rect.left = 120
                current_level.shift_world(diff)
        #re-implement when you figure out how to keep her from falling
        if player.rect.top <= 120:
                diff = 120 - player.rect.top
                player.rect.top = 120
                current_level.shift_worldy(diff)

        if player.rect.bottom >= 600:
                diff = player.rect.bottom - 600
                player.rect.bottom = 600
                current_level.shift_worldy(-diff)
            #next level

        current_level.draw(screen)
        active_sprite_list.draw(screen)

        clock.tick(40)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
