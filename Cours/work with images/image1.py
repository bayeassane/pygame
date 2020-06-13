'''Load simple image'''
import pygame
from pygame.locals import *


RED = (255, 0, 0)
GRAY = (150, 150, 150)
width, height = 500, 300

pygame.init()
screen = pygame.display.set_mode((width, height))

# loads image
img = pygame.image.load('bird.png')
img.convert()
rect = img.get_rect()
rect.center = width//2, height//2

running = True

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

	screen.fill(GRAY)
	screen.blit(img, rect)
	pygame.draw.rect(screen, RED, rect, 1)
	pygame.display.update()

pygame.quit()