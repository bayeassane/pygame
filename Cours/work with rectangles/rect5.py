'''Move a rectangle with mouse'''
import pygame
from pygame.locals import *


SIZE = (500, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

rect = Rect(50, 60, 200, 80)
moving = False
running = True

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

		elif event.type == MOUSEBUTTONDOWN:
			if rect.collidepoint(event.pos):
				print("vous avez cliqué")
				moving = True
				print(moving)
		elif event.type == MOUSEBUTTONUP:
			moving = False
			print(moving)
		elif event.type == MOUSEMOTION and moving:
			# event.rel : la postion relative
			rect.move_ip(event.rel)

	screen.fill(GRAY)
	pygame.draw.rect(screen, RED, rect)
	if moving:
		pygame.draw.rect(screen, BLUE, rect, 4)
	pygame.display.update()

pygame.quit()