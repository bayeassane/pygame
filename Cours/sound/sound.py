# pour gérer le son, pygame dispose deux modules Mixer et Music pour le gérer de façon séparée
# Music est un sous-module de Mixer
import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((640, 240))

sound = pygame.mixer.Sound('rpg.ogg')

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_d:
                sound.play()
            elif event.key == K_p:
                pygame.mixer.pause()
            elif event.key == K_u:
                pygame.mixer.unpause()
            elif event.key == K_s:
                sound.stop()
        
    screen.fill(Color('gray'))
    pygame.display.flip()


pygame.quit()