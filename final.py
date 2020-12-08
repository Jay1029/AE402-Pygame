#AE402 Pygame 第十三週 期末測驗
#實作考題(25%)
#題目：移動的球，可以按鍵盤「左、右」來控制球移動，不能移動到超出螢幕。
#螢幕大小: 640x70
#螢幕底色:白色
#球:紅色
#球半徑:10

#匯入pygame模組
import pygame
#設定顏色
WHITE = (0,0,0)
RED = (255,0,0)
#pygame初始化
pygame.display.set._mode((640,70))
#設定螢幕
screen_width = 700
screen_height = 400
pygame.display.set._mode[(screen_width,screen_height)]
#設定視窗標題

#設定更新時鐘
clock = 
#設定迴圈開關

#設定球x原先座標

#主迴圈
while True
    #偵測關閉事件
    for Event in pygame.event.get():
        if event.type==pygame.QUIT

    #偵測鍵盤事件
    if keys = pygame.key.get_pressed()
    #判斷鍵盤是否為左右按鈕，若是則移動球位置
    if keys[pygame.K_RIGHT]
    #螢幕填色
    screen = pygame.screen(WHITE)
    #畫出球
    ball = pygame.draw.circle(RED,10)
    #螢幕更新
    
    #設定更新時間

#關閉pygame

#提示1:keys = pygame.key.get_pressed()可以回傳哪個按鍵被按
#提示2:if keys[pygame.K_RIGHT]: 可以判斷按下右方向鍵









nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo









































