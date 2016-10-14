# -*-coding:utf-8-*-

import pygame
from sys import exit
from random import *

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('bullet.png').convert_alpha()
        self.active = False
    def move(self):
        if self.active:
            self.y -= 3
        if self.y < 0:
            self.active = False

    def restart(self):
        mousex,mousey = pygame.mouse.get_pos()
        self.x = mousex - self.image.get_width()/2
        self.y = mousey - self.image.get_height()/2
        self.active = True

class Enemy:
    def restart(self):
        self.x = randint(50,220)
        self.y = randint(-200,-20)
        self.speed = random() + 0.02
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('enemy.png').convert_alpha()
    def move(self):
        if self.y < 420:
            self.y += self.speed
        else:
            self.restart()

class Plane:
    def restart(self):
        self.x = 200
        self.y = 600
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('play.png').convert_alpha()
    def move(self):
        x,y = pygame.mouse.get_pos()
        x -= self.image.get_width()/2
        y -= self.image.get_height()/2
        self.x = x
        self.y = y


def checkhit(e,b):
    if(b.x> e.x and b.x<e.x + e.image.get_width() \
            and b.y>e.y and b.y< e.y +e.image.get_height()):
        e.restart()
        b.active = False
        return True
    return False

def checkcrash(e,p):
    if (p.x +0.7*p.image.get_width()> e.x)and \
            (p.x+0.3*p.image.get_width() <e.x+e.image.get_width())and\
            (p.y+0.7*p.image.get_height() > e.y) and \
            (p.y+0.3*p.image.get_height() < e.y + e.image.get_height()):
        return True
    return False

pygame.init()

screen = pygame.display.set_mode((320, 420), 0, 32)
pygame.display.set_caption("Fu*ko,Game!")

background = pygame.image.load('bg.jpg').convert()

bullet = [] 
for i in range(4):
    bullet.append(Bullet())
count_b = len(bullet)
index_b = 0 
interval_b = 0

enemy = []
for i in range(5):
    enemy.append(Enemy())


plane = Plane()

score = 0
gameover = False
while True:
    for event in pygame.event.get():
#        if event.type == pygame.MOUSEBUTTONDOWN:
#            background = pygame.image.load('play.jpg').convert()
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background,(0,0))

    interval_b -= 1
    if interval_b < 0:
        bullet[index_b].restart()
        interval_b = 100
        index_b = (index_b + 1) % count_b
    for b in bullet:
        if b.active:
            for e in enemy:
                if checkhit(e,b):
                    score += 10
            b.move()
            screen.blit(b.image,(b.x, b.y))
    
    for e in enemy: 
        e.move()
        screen.blit(e.image,(e.x, e.y))

    plane.move()
    screen.blit(plane.image,(plane.x,plane.y))
    pygame.display.update()
