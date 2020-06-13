'''Déplacer automatiquement un rectangle'''
import pygame
from pygame.locals import *

width, height = 500, 200
SIZE = (width, height)
RED = (255, 0, 0)
GRAY = (150, 150, 150)

# initialise les modules de pygame
pygame.init()
# création du fenêtre 
screen = pygame.display.set_mode(SIZE)
# titre de la fenêtre
pygame.display.set_caption('Déplacer un rectangle')

rect = Rect(100, 100, 50, 50)
v = [2, 2]
running = True

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

	rect.move_ip(v)
	pygame.time.delay(30)
	if rect.left < 0:
		v[0] *= -1
	if rect.right > width:
		v[0] *= -1
	if rect.top < 0:
		v[1] *= -1
	if rect.bottom > height:
		v[1] *= -1

	screen.fill(GRAY)
	pygame.draw.rect(screen, RED, rect)
	pygame.display.flip()

pygame.quit()