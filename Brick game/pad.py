import pygame, random, math

class Ball(pygame.sprite.Sprite):
    dx = 0  #x位移量
    dy = 0  #y位移量
    x = 0  #球x坐標
    y = 0  #球y坐標
 
    def __init__(self, speed, srx, sry, radium, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([radium*2, radium*2])  #繪製球體
        self.image.fill((255,255,255))
        pygame.draw.circle(self.image, color, (radium,radium), radium, 0)
        self.rect = self.image.get_rect()  #取得球體區域
        self.rect.center = (srx,sry)  #初始位置
        direction = random.randint(20,70)  #移動角度
        radian = math.radians(direction)  #角度轉為弳度
        self.dx = speed * math.cos(radian)  #球水平運動速度
        self.dy = -speed * math.sin(radian)  #球垂直運動速度
 
    def update(self):
        self.x += self.dx  #計算球新餘標
        self.y += self.dy
        self.rect.x = self.x  #移動球圖形
        self.rect.y = self.y
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()):  #到達左右邊界
            self.dx *= -1  #水平速度變號
        elif(self.rect.top <= 5 or self.rect.bottom >= screen.get_height()-5):  #到達上下邊界
            self.dy *= -1  #垂直速度變號
 

    ball1.update()  #物件更新
    ball2.update()
    allsprite.draw(screen)
    self.rect.bottom >= screen.get_height()-5
    pygame.display.update()
pygame.quit()
