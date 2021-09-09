import pygame
import os
import random
import time
from pygame.locals import *

pygame.init()

screen_width = 750
screen_height = 750

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

# load images
bg_img = pygame.image.load("img/star_background.jpeg")
bg_img = pygame.transform.scale(bg_img, (750, 1000))

run = True
while run:
    screen.blit(bg_img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
pygame.quit()