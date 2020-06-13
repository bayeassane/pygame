import pygame
from pygame.locals import *

from player import Player
from enemy import Enemy


class Game:

    def __init__(self):
        self.player = Player(self)

        # groupe de player
        self.all_players = pygame.sprite.GroupSingle()
        self.all_players.add(self.player)

        # groupe d'enemies
        self.all_enemies = pygame.sprite.Group()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()

    def collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False)

    def spawn_enemy(self):
        self.all_enemies.add(Enemy(self))
