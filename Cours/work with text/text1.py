import pygame
from pygame.locals import *
import time


w, h = 640, 240
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((w, h))
font = pygame.font.SysFont('consolas.ttf', 24)
img = font.render('Salut les amis', True, BLUE)
rect = img.get_rect()
rect.x, rect.y = 20, 20
pygame.draw.rect(screen, RED, rect, 1)

screen.blit(img, (20, 20))
pygame.display.update()

# fonts = pygame.font.get_fonts()
# print(len(fonts))
# for font in fonts:
# 	print(font)

running = True

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

pygame.quit()