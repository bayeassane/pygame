import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = 7
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0
    
    def rotate(self):
        """Tourner le projectile"""
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def update(self):
        self.rect.x += self.velocity
        self.rotate()

        # vérifier si le projectile est en collision
        for monster in self.player.game.check_collison(self, self.player.game.all_monsters):
            self.remove()
            # infliger des dégâts
            monster.damage(self.player.attack)
        
        # vérifier si notre projectile n'est plus présent sur l'écran
        if self.rect.x > 1080:
            # supprimer le projectile
            self.remove()
           