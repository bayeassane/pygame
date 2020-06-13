import pygame
from pygame.locals import *

width, height = 500, 200
GRAY = (150, 150, 150)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((width, height))
rect = Rect(50, 60, 200, 80)

running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

		if event.type == KEYDOWN:
			if event.key == K_l:
				rect.left = 0
			elif event.key == K_c:
				rect.centerx = width // 2
			elif event.key == K_r:
				rect.right = width

			elif event.key == K_t:
				rect.top = 0
			elif event.key == K_m:
				rect.centery = height // 2
			elif event.key == K_b:
				rect.bottom = height

	screen.fill(GRAY)
	pygame.draw.rect(screen, BLUE, rect)
	pygame.display.flip()

pygame.quit()