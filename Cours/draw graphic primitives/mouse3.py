import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((640, 240))

RED = (255, 0, 0)
GRAY = (127, 127, 127)
drawing = False

running = True

while running:
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			pass

		elif event.type == MOUSEMOTION and drawing:
			pass

		elif event.type == MOUSEBUTTONUP:
			pass

		if event.type == QUIT:
			running = False

	screen.fill(GRAY)
	pygame.display.update()


pygame.quit()