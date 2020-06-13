import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = 5
        self.game = game
        self.image = pygame.image.load('images/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.x = game.player.rect.x + 15
        self.rect.y = game.player.rect.y

    def remove(self):
        self.game.player.all_bullets.remove(self)

    def update(self):
        self.rect.y -= self.velocity

        # vérifie si la balle est en dehors de l'écran puis on la supprime
        if self.rect.y < 0:
            # supprime la balle
            self.remove()

        # détecte si la balle est en collision
        if pygame.sprite.spritecollide(self, self.game.all_enemies, False, pygame.sprite.collide_mask):
            self.remove()