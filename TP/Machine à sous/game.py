import pygame
from pygame.locals import *
import random
from fruit import Fruit


class Game:

    def __init__(self):
        # initialisation du modules de pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 480))
        pygame.display.set_caption('Machine à sous')

        # fps
        self.fps = pygame.time.Clock()

        # fond d'écran de l'arrière plan
        self.background = pygame.image.load('images/slot.png')

        # score
        self.font = pygame.font.Font(None, 20)
        self.score = 0
        self.font_score = self.font.render(f'{self.score} €', True, Color('black'))

        # ajout du fruit dans chaque emplacement
        self.list_fruit = ['ananas', 'cerise', 'orange', 'pasteque', "pomme_doree"]

        # les jetons pour chaque fruit
        self.tokens = {
            'ananas': 50,
            'cerise': 15,
            'orange': 5,
            'pasteque': 150,
            "pomme_doree": 10_000
        }

        # chosir 3 fruits parmis la listes des fruits
        self.choice_fruits = random.choices(self.list_fruit, [20, 25, 40, 10, 5], k=3)
        # groupe de fruits
        self.all_fruits = pygame.sprite.Group()
        # ajout des fruits dans le groupe
        self.add_fruits()
        # place les fruits dans les emplacements
        self.place_fruits()

        self.running = True

    def start(self):
        # on choisit une liste de 3 fruits au hasard en tenant compte de la probabilité
        self.choice_fruits = random.choices(self.list_fruit, [20, 25, 40, 10, 5], k=3)

        # on supprime les fruits dans le groupe pour y mettre les nouveaux
        self.all_fruits = pygame.sprite.Group()
        self.add_fruits()
        self.place_fruits()

        # on teste si les trois fruits sont identiques
        if all(fruit == self.choice_fruits[0] for fruit in self.choice_fruits):
            # on cummule le nombre de jetons
            fruit = self.choice_fruits[0]
            score = self.tokens[fruit]
            self.score += score
            self.font_score = self.font.render(f'{self.score} €', True, Color('black'))

    def add_fruits(self):
        """Ajoute trois fruit dans le groupe de fruits"""
        for fruit in self.choice_fruits:
            self.all_fruits.add(Fruit(fruit))

    def place_fruits(self):
        """Place les fruits dans les trois emplacements"""
        x = 0
        for fruit in self.all_fruits:
            fruit.rect.x += x
            x += 101

    def run(self):
        while self.running:
            self.fps.tick(30)

            self.screen.fill(Color('white'))

            # appliquer le fond d'écran
            self.screen.blit(self.background, (0, 0))
            # score
            self.screen.blit(self.font_score, (20, 20))

            # mise à jour du groupe
            self.all_fruits.update()

            # dessine le groupe
            self.all_fruits.draw(self.screen)

            # gestion des événements
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.start()

            # mise à jour de l'écran
            pygame.display.flip()


if __name__ == '__main__':
    Game().run()
