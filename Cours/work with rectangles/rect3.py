'''Move rectangle with keys'''
import pygame
from pygame.locals import *

key_dict = {
	K_LEFT: (-5, 0),
	K_RIGHT: (5, 0),
	K_UP: (0, -5),
	K_DOWN: (0, 5),
}
GRAY = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init() # initialise  les modules de pygame
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption('Move rectangle with keys')

rect0 = Rect(50, 60, 200, 80)
rect = rect0.copy()
running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

		if event.type == KEYDOWN:
			if event.key in key_dict:
				v = key_dict[event.key]
				rect.move_ip(v)

	screen.fill(GRAY)
	pygame.draw.rect(screen, RED, rect0, 1)
	pygame.draw.rect(screen, BLUE, rect, 4)
	pygame.display.flip()

pygame.quit()

