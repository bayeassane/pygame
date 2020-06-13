import pygame 


pygame.init()

screen = pygame.display.set_mode((640, 240))
GRAY = (127, 127, 127)
RED = (255, 0, 0)
running = True
start = (0, 0)
end = (0, 0)
size = (0, 0)
drawing = False
pygame.draw.rect(screen, RED, (10, 10, 20, 20))
pygame.display.update()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			print('nous avons pressé')
			start = event.pos
			size = (0, 0)
			drawing = True

		elif event.type == pygame.MOUSEBUTTONUP:
			print('nous avons relaché le bouton')
			end = event.pos
			size = end[0] - start[0] , end[1] - start[1]
			drawing = False

		elif event.type == pygame.MOUSEMOTION and drawing:
			end = event.pos
			size = end[0] - start[0] , end[1] - start[1]

	screen.fill(GRAY)
	pygame.draw.rect(screen, RED, (start, size), 2)
	pygame.display.update()
pygame.quit()