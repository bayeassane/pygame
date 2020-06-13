import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(Color('green'))
        self.rect = self.image.get_rect()
        self.rect.center = (w // 2, h // 2)
    
    def update(self):
        self.rect.x += 5
        if self.rect.left > w:
            self.rect.right = 0


class PlayerImage(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/img.png')
        self.rect = self.image.get_rect()
        self.rect.center = (w//2, h//2)

    def updateg(self):
        self.rect.x += 5
        if self.rect.left > w:
            self.rect.right = 0

    def move_right(self):
        self.rect.x += 5
    
    def move_left(self):
        self.rect.x -= 5

w, h = 640, 480


# initialisation des modules de pygame
pygame.init()
screen = pygame.display.set_mode((w, h))


clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() # un groupe de sprites pour contenir l'ensemble de notre sprites de jeu

# création du joueur
player = Player()
player_image = PlayerImage()
# print(pygame.sprite.spritecollide(player, all_sprites, True))


all_sprites.add(player_image)

pressed = {}


running = True

while running:
    # fps
    clock.tick(30)

    # gestion des évenements
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            pressed[event.key] = True
        if event.type == KEYUP:
            pressed[event.key] = False
    
    # déplacements 
    if pressed.get(K_LEFT):
        player_image.move_left()
    elif pressed.get(K_RIGHT):
        player_image.move_right()
    

    # mise à jour des sprites
    all_sprites.update()
    
    screen.fill(Color('blue'))
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()