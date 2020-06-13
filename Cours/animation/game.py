import pygame 
from pygame.locals import *


class Animation(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        self.images.append(pygame.image.load('images/walk1.png'))
        self.images.append(pygame.image.load('images/walk2.png'))
        self.images.append(pygame.image.load('images/walk3.png'))
        self.images.append(pygame.image.load('images/walk4.png'))
        self.images.append(pygame.image.load('images/walk5.png'))
        self.images.append(pygame.image.load('images/walk6.png'))
        self.images.append(pygame.image.load('images/walk7.png'))
        self.images.append(pygame.image.load('images/walk8.png'))
        self.images.append(pygame.image.load('images/walk9.png'))
        self.images.append(pygame.image.load('images/walk10.png'))

        self.index = 0

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

    
    def move(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.rect.x += 10


class Game:

    def __init__(self):
        pygame.init()
        Game.screen = pygame.display.set_mode((640, 400))

        # fps
        self.clock = pygame.time.Clock()

        # animation
        self.anim = Animation()

        # groupe pour animation
        self.all_anim = pygame.sprite.Group()
        self.all_anim.add(self.anim)

        self.running = True

        self.pressed = {}

    def run(self):
        while self.running:
            # fps
            self.clock.tick(30)

            Game.screen.fill(Color('black'))

            # mise à jour 
            self.all_anim.update()

            # dessine 
            self.all_anim.draw(Game.screen)
            pygame.display.flip()

            # gestion d'évenements
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

                if event.type == KEYDOWN:
                    self.pressed[event.key] = True
                elif event.type == KEYUP:
                    self.pressed[event.key] = False
                    
            if self.pressed.get(K_RIGHT):
                self.anim.move()


if __name__ == '__main__':
    Game().run()