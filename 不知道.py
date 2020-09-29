# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:19:17 2020

@author: User
"""


import pygame, random

# 定義一些會用到的顏色
# 常數使用大寫
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
snow_list = []



pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("下雪動畫")


x = random.randrange(0, 400)
y = random.randrange(0, 400)



done = False   
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

  
    screen.fill(BLACK)
    snowStart = pygame.draw.circle(screen, WHITE, (x,y), 2)
    y = y + 1
    if y > 400:
        y = 0
        x = random.randrange(0, 400)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


