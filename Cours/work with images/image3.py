'''Rotate image'''
import pygame
from pygame.locals import *

w, h = 640, 240
angle, scale = 0, 1
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode((w, h))

# loads image
img0 = pygame.image.load('bird.png')
img0.convert()
rect0 = img0.get_rect()
# place the center
center = w//2, h//2
img = img0
rect = img.get_rect()
rect.center = center

running = True

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

		if event.type == KEYDOWN:
			if event.key == K_r:
				if event.mod and KMOD_SHIFT:
					angle -= 10
				else:
					angle += 10
				img = pygame.transform.rotozoom(img0, angle, scale)
			elif event.key == K_s:
				if event.mod and KMOD_SHIFT:
					scale /=1.1
				else:
					scale *= 1.1
				img = pygame.transform.rotozoom(img0, angle, scale)
			elif event.key == K_o:
				img = img0
				angle = 0
				scale = 1
			elif event.key == K_h:
				img = pygame.transform.flip(img, True, False)
			elif event.key == K_v:
				img = pygame.transform.flip(img, False, True)
			elif event.key == K_l:
				img = pygame.transform.laplacian(img)
			elif event.key == K_2:
				img = pygame.transform.scale2x(img)
			# transform the image with the mouse
				
			rect = img.get_rect()
			rect.center = center

	screen.fill(GRAY)
	screen.blit(img, rect)
	pygame.draw.rect(screen, GREEN, rect, 1)
	pygame.display.update()

pygame.quit()