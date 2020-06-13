'''Edit text with the keyboard'''
import pygame
from pygame.locals import *
import time

w, h = 640, 240
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((w, h))

text = 'This text is editable'
font = pygame.font.SysFont(None, 24)
img = font.render(text, True, RED)

rect = img.get_rect()
rect.topleft = (20, 20)
cursor = Rect(rect.topleft, (3, rect.height))

running = True
cursor_show = False
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

		if event.type == KEYDOWN:
			cursor_show = True
			if event.key == K_BACKSPACE:
				text = text[:-1]
			else:
				text += event.unicode
			img = font.render(text, True, RED)
			rect.size = img.get_size()
			cursor.topleft = rect.topright

		elif event.type == KEYUP:
			cursor_show = False
	
	screen.blit(img, rect)
	if  not cursor_show:
		pygame.draw.rect(screen, RED, cursor)
	pygame.display.update()

pygame.quit()