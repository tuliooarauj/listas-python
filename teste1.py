import pygame
from pygame.locals import *

#define fps
clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 800

player_position_x = screen_width / 2
player_position_y = screen_height - 100

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

run = True
while run:

    clock.tick(fps) #limiting to 60 fps

    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    player = pygame.draw.rect(screen, (255, 0, 0), (player_position_x, player_position_y, 50, 50))
    throttle = pygame.draw.rect(screen, (0, 255, 0), (300, 100, 20, 20))


    pygame.display.update()

pygame.quit()