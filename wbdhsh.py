import pygame
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# player的初始位置
player_x = 0
player_y = 0
player_w = 50
player_h = 50

# block的初始位置
block_w = 50
block_h = 50
block_x = random.randrange(screen_width-block_w)
block_y = random.randrange(screen_height-block_h)

collision = False

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
            
    # 判斷是否碰撞到了
    xin = block_x<=player_x<=block_x+block_w or block_x<=player_x+player_w<=block_x+block_w
    yin = block_y<=player_y<=block_y+block_h or block_y<=player_y+player_h<=block_y+block_h
    if  xin and yin and not collision:
        collision = True
        
    screen.fill(WHITE)

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            if pygame.event.Key():
            done = True 
    
    # 畫出player
    
    # 如果沒有碰撞取得滑鼠座標block方塊

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


