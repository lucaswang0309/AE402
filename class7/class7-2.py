# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:58:26 2020

@author: lucas
"""

"""
 Pygame 模板程式
 
"""
# 匯入pygame模組
import pygame
import random
# 定義一些會用到的顏色
# 常數使用大寫
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        
class Ball(pygame.sprite.Sprite):
    def __init__(self,speed, x, y, r, color):
        super().__init__()
        self.image = pygame.Surface([r*2, r*2])
        pygame.draw.circle(self.image, color, (r, r), r)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
# 初始化pygame
pygame.init()
# 創造一個pygame視窗並設定大小及標題
size = (700, 500)
screen = pygame.display.set_mode(size)
score = 0
pygame.display.set_caption("得分" + str(score))

# 設定一個開關供迴圈使用
done = False

# 創造一個clock控制畫面更新速度
clock = pygame.time.Clock()

allSprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()
for i in range(100):
    for j in range(500):
        color = RED
        if (i+j) % 3 == 1:
            color = WHITE
        elif (i+j) % 3 == 2:
            color = RED
        else:
            color = BLUE
       
        block = Block(color, 10, 15)
        block.rect.x = i*10
        block.rect.y = 15*j
        blocks.add(block)
        allSprites.add(block)
    
player = Block(WHITE, 100, 100)  
allSprites.add(player) 
ball = Ball(0, 300, 300, 30, WHITE)
allSprites.add(ball)
# -------- 主要的程式迴圈 -----------
while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get(): # 從事件list中抓取事件
        if event.type == pygame.QUIT: # 當使用者按下結束
            done = True # 將done變數設為True-->while迴圈將會結束

    # --- 程式的運算與邏輯
    

    # --- 繪圖的程式碼
    #       先將畫面塗滿底色(將原有畫面清掉)
    #       繪圖的程式要寫在這行後面，不然會被這行清掉
    screen.fill(BLACK)
    
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]
    
    hits = pygame.sprite.spritecollide(player, blocks, True)
    if len(hits) > 0:
        score += len(hits)
        print("增加"+str(len(hits))+"分")
    allSprites.draw(screen)
        
        
    pygame.display.set_caption("得分" + str(score))
    # --- 更新畫面
    pygame.display.flip()

    # --- 每秒鐘60個frame
    clock.tick(240)

# 關閉式窗並離開程式
pygame.quit()
exit()


