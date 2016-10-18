#! /usr/bin/python

import pygame
import math
from pygame.locals import *

width,height = 640, 480

keys = [False, False, False, False]
playerpos = [100,100]

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Run bullt ^_^")

player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

while True:
    screen.fill(0)

    for x in range(width/grass.get_width() + 1):
        for y in range(height/grass.get_height() + 1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345))

    positon = pygame.mouse.get_pos()
    angle = math.atan2(positon[1]-(playerpos[1]+32),positon[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1=(playerpos[0]-playerrot.get_rect().width/2,\
            playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit(0)
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == KEYUP:
            if event.key == K_w:
                keys[0] = False
            elif event.key == K_a:
                keys[1] = False
            elif event.key == K_s:
                keys[2] = False
            elif event.key == K_d:
                keys[3] = False

    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5

    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5

