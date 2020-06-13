import pygame
from pygame.locals import *

from bullet import Bullet


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.attack = 10
        self.health = 100
        self.max_health = 100
        self.velocity = 5
        self.game = game
        # bullets
        self.all_bullets = pygame.sprite.Group()

        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 700 // 2
        self.rect.y = 500

    def launch_bullet(self):
        self.all_bullets.add(Bullet(self.game))

    def move_right(self):
        if self.rect.right < 800:
            self.rect.x += self.velocity

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.velocity

    def update(self):
        if self.game.collision(self, self.game.all_enemies):
            print('game over')

