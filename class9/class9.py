# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:52:35 2020

@author: lucas
"""

"""
 Pygame 模板程式
 
"""
# 匯入pygame模組
import pygame
import random
from class11 import Snake,Food

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


        
# 初始化pygame
pygame.init()

# 創造一個pygame視窗並設定大小及標題
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("我的遊戲")

# 設定一個開關供迴圈使用
done = False

# 創造一個clock控制畫面更新速度
clock = pygame.time.Clock()
snake = Snake(5, size)
g = pygame.sprite.Group()
eat = False
def addFood():
     x = random.randrange(size[0])
     y = random.randrange(size[1])
     x -= x % 20
     y -= y % 20
     food = Food(WHITE, x, y)
     g.add(food)
    

# -------- 主要的程式迴圈 -----------
while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        

    # --- 程式的運算與邏輯
    if len(g) == 0:
        addFood()
    
    pressed = pygame.key.get_pressed()
    
    snake.move(pressed)
    
    snake.Foodeating(g)
    
    if snake.itsOutofRange() or snake.collideself():
        done = True
    
    #eatFood = pygame.sprite.groupcollide(snake.group, g, False, True)
    #if eatFood:
     #   snake.append(len(eatFood.values())*10)
    # --- 繪圖的程式碼
    #       先將畫面塗滿底色(將原有畫面清掉)
    #       繪圖的程式要寫在這行後面，不然會被這行清掉
    screen.fill(BLACK)
    g.draw(screen)
    snake.group.draw(screen)
    # --- 更新畫面
    pygame.display.flip()

    # --- 每秒鐘60個frame
    clock.tick(5)

# 關閉式窗並離開程式
pygame.quit()
exit()


