# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:18:42 2020

@author: lucas
"""

import pygame
import random

def randomcolor():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return(r,g,b)
# 定義一些會用到的顏色
# 常數使用大寫
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
blue     = (   0,   0, 255)

class SnakeBody(pygame.sprite.Sprite):
    SIZE = 20
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([self.SIZE, self.SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Snake():
    def __init__(self,length):
        self.group = pygame.sprite.Group()
        self.queue = []
        self.x = 0
        self.y = 0
        self.dir = 0
        self.eatFood = 0
        
        for i in range(length):
            self.x += SnakeBody.SIZE
            body = SnakeBody(RED, self.x, self.y)
            
            self.group.add(body)
            self.queue.append(body)
            
    def move(self, pressed=None):
        self.changeDir(pressed)
        
        if self.dir == 0:
            self.x += SnakeBody.SIZE
        elif self.dir == 1:
            self.y += SnakeBody.SIZE
        elif self.dir == 2:
            self.x -= SnakeBody.SIZE
        else:
            self.y -= SnakeBody.SIZE
        head = SnakeBody(RED, self.x, self.y)
        self.group.add(head)
        self.queue.append(head)
        if self.eatFood > 0:
            self.eatFood -= 1
        else:
            tail = self.queue.pop(0)
            self.group.remove(tail)
        
        
    def changeDir(self, pressed):
        if not pressed: return
        
        if pressed[pygame.K_UP]:
            self.dir = 3
        elif pressed[pygame.K_LEFT]:
            self.dir = 2
        elif pressed[pygame.K_DOWN]:
            self.dir = 1
        elif pressed[pygame.K_RIGHT]:
            self.dir = 0
    def append(self,num):
        self.eatFood += num
    def Foodeating(self, foodGroup):
        eatFood = pygame.sprite.groupcollide(self.group, foodGroup, False, True)
        if eatFood:
            self.append(len(eatFood.values())*10)
        
class Food(pygame.sprite.Sprite):
    SIZE = 20
    def __init__(self, color, x, y, ):
        super().__init__()
        self.image = pygame.Surface([self.SIZE,self.SIZE])
        self.image.fill(color)                            
        self.rect = self.image.get_rect()                    
        self.rect.x = x
        self.rect.y = y                          
                                  
                                  
                                    
                                            
        
        
        