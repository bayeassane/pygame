import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((640, 240))

RED = (255, 0, 0)
GRAY = (127, 127, 127)
BLUE = (0, 0, 255)
drawing = False
start = (0, 0)
end = (0, 0)
rect_list = []
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
			rect = pygame.Rect(start, size)
			rect_list.append(rect)
			drawing = False

		if event.type == QUIT:
			running = False

	screen.fill(GRAY)
	for rect in rect_list:
		pygame.draw.rect(screen, RED, rect, 2)
	pygame.draw.rect(screen, BLUE, (start, size), 1)
	pygame.display.update()


pygame.quit()