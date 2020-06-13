import pygame
from pygame.locals import *

pygame.init()

# define colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

screen = pygame.display.set_mode((640, 240))
background = GRAY
screen.fill(background)

key_dict = {
    K_k: BLACK,
    K_r: RED,
    K_g: GREEN,
    K_c: CYAN,
    K_m: MAGENTA,
    K_b: BLUE,
    K_w: WHITE,
}
print(key_dict)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
                
                caption = 'Background color = '+ str(background)
                pygame.display.set_caption(caption)

        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(background)
    pygame.display.update()

pygame.quit()