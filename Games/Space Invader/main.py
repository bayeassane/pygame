import pygame
from pygame.locals import *

from game import Game


class Main:

    def __init__(self):
        # initialise les modules de pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

        # fond d'écran du jeu
        self.background = pygame.image.load('images/background.png')

        # fps le nombre d'éxécution de la boucle while
        self.fps = pygame.time.Clock()

        # définition des composants du jeu
        self.game = Game()



        self.running = True

    def run(self):
        while self.running:
            # fps
            self.fps.tick(150)

            # mise à jour du fond d'écran
            self.screen.blit(self.background, (0, 0))

            # gestion d'évenement
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.game.player.launch_bullet()

            keys = pygame.key.get_pressed()
            if keys[K_RIGHT]:
                self.game.player.move_right()
            elif keys[K_LEFT]:
                self.game.player.move_left()

            # mise à jour des groupe
            self.game.all_players.update()
            self.game.player.all_bullets.update()
            self.game.all_enemies.update()

            # dessine
            self.game.all_players.draw(self.screen)
            self.game.player.all_bullets.draw(self.screen)
            self.game.all_enemies.draw(self.screen)

            # mise à jour
            pygame.display.flip()


if __name__ == '__main__':
    Main().run()