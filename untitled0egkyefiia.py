import pygame
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        


hit_group = pygame.sprite.Group()
all_group = pygame.sprite.Group()

for i in range(10):
    block = Block(BLACK,20 ,15)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    all_group.add(block)
    hit_group.add(block)

player = Block(RED,20 ,15)
all_group.add(player)

score = 0

font = pygame.font.Font(None, 50)

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        
    screen.fill(WHITE)
    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    score_group = pygame.sprite.spritecollide(player, hit_group, True)

    for block in score_group:
        score+=1
        
    all_group.draw(screen)        
      
    message = str(score)+' point'
    text = font.render(message, 10, BLACK)
    screen.blit(text, (10,10))
    
    all_group.draw(screen)
    pygame.display.flip()

    clock.tick(60)
pygame.quit()


