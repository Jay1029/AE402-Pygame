import pygame
import random 
black = (0,0,0)
red = (255,0,0)
WHITE = (255,255,255)
pygame.init()
windowSize = (400, 300)
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

count = 0
click = False 
limit = 30 
pos = (0, 0)

done = False
while not done:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click = True
            count = 0
        if event.type == pygame.QUIT:
            done = True
    if click and count < limit:
        if windowSize < (200,150):
            pygame.draw.circle(screen, red, pos, count) 
        else:    
            pygame.draw.circle(screen,black , pos, count)
            count += 1
        if count >= limit:
            click = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


