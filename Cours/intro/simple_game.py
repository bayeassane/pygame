import pygame 
from pygame.locals import *


width, height = 640, 320
size = (width, height)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode(size)
running = True

ball = pygame.image.load('ball.gif')
rect = ball.get_rect()
speed = [2, 2]

print(rect.left, rect.right, rect.bottom, rect.top)

while running:


    # if key_dict.get(K_RIGHT):
    #     rect = rect.move([1, 0])
    # elif key_dict.get(K_LEFT):
    #     rect = rect.move(-1, 0)
    # elif key_dict.get([])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # if event.type == KEYDOWN:
        #     key_dict[event.key] = True
        # elif event.type == KEYUP:
        #     key_dict[event.key] = False
    
    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]
    
    screen.fill(GREEN)
    pygame.draw.rect(screen, RED, rect, 1)
    screen.blit(ball, rect)
    pygame.display.update()
# rect = ball.get_rect()

pygame.quit()