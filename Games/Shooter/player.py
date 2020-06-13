
import pygame
from projectile import Projectile



class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 340

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()


    def update_health_bar(self,  surface):
        # dessine l'arrière de la jauge
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])

        # dessine notre barre de vie
        pygame.draw.rect(surface,  (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])
        

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collison
        if self.rect.right < 1080 and not self.game.check_collison(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.velocity