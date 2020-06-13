'''Move the image with the mouse'''
import pygame
from pygame.locals import *


RED = (255, 0, 0)
GRAY = (150, 150, 150)
width, height = 640, 240

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Move the image with the mouse')

# loads image
img = pygame.image.load('bird.png')
img.convert()
rect = img.get_rect()
rect.center = width//2, height//2

running = True
moving = False

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

		elif event.type == MOUSEBUTTONDOWN:
			moving = True

		elif event.type == MOUSEBUTTONUP:
			moving = False

		elif event.type == MOUSEMOTION and moving:
			if rect.collidepoint(event.pos):
				rect.move_ip(event.rel)

	screen.fill(GRAY)
	screen.blit(img, rect)
	pygame.draw.rect(screen, RED, rect, 1)
	pygame.display.update()

pygame.quit()