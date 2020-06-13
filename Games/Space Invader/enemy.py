import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = random.randint(4, 6)
        self.game = game
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 700)

    def update(self):
        self.rect.x += self.velocity
        if self.rect.right > 800:
            self.velocity = -self.velocity
            self.rect.y += 70
        elif self.rect.left < 0:
            self.velocity = -self.velocity
            self.rect.y += 70

        # détecte si la balle est en collision
        if self.game.collision(self, self.game.player.all_bullets):
            self.velocity = random.randint(5, 10)
            self.rect.x = random.randint(0, 700)
            self.rect.y = 0
