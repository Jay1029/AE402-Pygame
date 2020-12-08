import pygame
screen = pygame.display.set_mode((600, 400))
class Pad(pygame.sprite.Sprite):  #滑板角色
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pad.png")  #滑板圖片
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)  #滑板位置
        self.rect.y = screen.get_height() - self.rect.height - 20
 
    def update(self):  #滑板位置隨滑鼠移動
        pos = pygame.mouse.get_pos()  #取得滑鼠坐標
        self.rect.x = pos[0]  #滑鼠x坐標
        if self.rect.x > screen.get_width() - self.rect.width:  #不要移出右邊界
            self.rect.x = screen.get_width() - self.rect.width


