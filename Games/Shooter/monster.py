import pygame
import random


class Monster(pygame.sprite.Sprite):
    """Créer un montre dans notre jeu"""

    def __init__(self,  game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 2
        self.velocity = random.randint(1, 3)
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 800 + random.randint(0, 300)
        self.rect.y = 385

    def damage(self, amount):
        self.health -= amount

        # vérifier si un monstre a 0 point de vie
        if self.health <= 0:
            self.rect.x = 800 + random.randint(0, 300)
            self.health = 100
            self.velocity = random.randint(1, 3)


    def update_health_bar(self,  surface):
        # dessine l'arrière de la jauge
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])

        # dessine notre barre de vie
        pygame.draw.rect(surface,  (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])
        
    
    def update(self):
        if not self.game.check_collison(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
        self.update_health_bar(self.game.screen)
    

        


