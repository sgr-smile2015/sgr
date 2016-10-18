#! /usr/bin/python

import pygame
import math
import random
from pygame.locals import *

width,height = 640, 480

keys = [False, False, False, False]
playerpos = [100,100]

acc = [0,0]
arrows = []

badtimer = 100
badtimer1 = 0
badguys = [[640,100]]
healthvalue = 194

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("run bullt ^_^")

player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg = badguyimg1

while True:
    badtimer -= 1
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

    # Draw arrows
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0])*5
        vely = math.sin(bullet[0])*5
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] >640 or bullet[2] <-64 or bullet[2] > 480:
            arrows.pop(index)
            index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1,(projectile[1],projectile[2]))

    # Draw badgers
    if badtimer == 0:
        badguys.append([640,random.randint(50,430)])
        badtimer = 100 -(badtimer1)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5

    index = 0
    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)
        badguy[0] -= 7
        index += 1
    for badguy in badguys:
        screen.blit(badguyimg,badguy)

    # attack castle
    badrect = pygame.Rect(badguyimg.get_rect())
    badrect.top = badguy[1]
    badrect.left = badguy[0]
    if badrect.left < 64 :
        healthvalue -= random.randint(5,20)
        badguys.pop(index)

    # check for collisions
    index1 = 0
    for bullet in arrows:
        bullrect = pygame.Rect(arrow.get_rect())
        bullrect.left = bullet[1]
        bullrect.top = bullet[2]
        if badrect.colliderect(bullrect):
            acc[0] += 1
            badguys.pop(index)
            arrows.pop(index1)
        index1 += 1

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

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append([math.atan2(positon[1]-(playerpos1[1]+32),\
                    position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5

    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5

