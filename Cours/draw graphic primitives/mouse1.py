import pygame
from pygame.locals import *


pygame.init()

screen = pygame.display.set_mode((640, 240))
RED = (255, 0, 0)
GRAY = (127, 127, 127)
drawing = False
start = (0, 0)
end = (0, 0)
size = width, height = (0, 0) 
running = True

while running:
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			start = event.pos
			size = (0, 0)
			drawing = True

		elif event.type == MOUSEMOTION and drawing:
			end = event.pos
			size = end[0] - start[0], end[1] - start[1]

		elif event.type == MOUSEBUTTONUP:
			end = event.pos
			size = end[0] - start[0], end[1] - start[1]
			drawing = False

		if event.type == QUIT:
			running = False

	screen.fill(GRAY)
	pygame.draw.rect(screen, RED, (start, size), 2)
	pygame.display.update()


pygame.quit()