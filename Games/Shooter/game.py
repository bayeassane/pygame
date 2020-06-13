import pygame
from pygame.locals import *
from player import Player
from monster import Monster



class Game:

    def __init__(self):
        # initialise les modules de pygame
        pygame.init()
        Game.screen = pygame.display.set_mode((1080, 600))

        # fps 
        self.clock = pygame.time.Clock()

        # fond d'écran du jeu
        self.background = pygame.image.load('assets/bg.jpg')

        # importer notre bannière
        self.banner = pygame.image.load('assets/banner.png')
        self.banner = pygame.transform.scale(self.banner, (500, 500))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = 1080 // 4

        # charger notre bouton
        self.play_button = pygame.image.load('assets/button.png')
        self.play_button = pygame.transform.scale(self.play_button, (400, 150))
        self.button_rect = self.play_button.get_rect()
        self.button_rect.center = self.banner_rect.center
        self.button_rect.y = self.banner_rect.y + 360


        # run
        self.running = True

        # status du jeu
        self.is_playing = False

        # groupe de player
        self.all_players = pygame.sprite.Group()

        # player
        self.player = Player(self)
        self.all_players.add(self.player)

        # groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        

        # raccourcis de touche
        self.pressed = {}
    
    def spawn_monster(self):
        self.all_monsters.add(Monster(self))


    def check_collison(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def start(self):
        self.spawn_monster()
        self.spawn_monster()
        self.is_playing = True
    
    def game_over(self):
        # remettre le jeu à neuf
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self):
        # charger le joueur
        Game.screen.blit(self.player.image, self.player.rect)


        # jauge de vie player
        self.player.update_health_bar(Game.screen)

        # mise à jour des projectiles
        self.player.all_projectiles.update()

        # mise à jour des monstres
        self.all_monsters.update()

        # appliquer les projectiles
        self.player.all_projectiles.draw(Game.screen)

        # appliquer les monstres
        self.all_monsters.draw(Game.screen)

        # déplacements du joueur
        if self.pressed.get(K_RIGHT):
            self.player.move_right()
        elif self.pressed.get(K_LEFT):
            self.player.move_left()
            

    def run(self):
        while self.running:
            # fps
            self.clock.tick(60)

            # background
            Game.screen.blit(self.background, (0, 0))

            

            # vérifier si le jeu a démarré
            if self.is_playing:
                self.update()
            else:

                # button
                Game.screen.blit(self.play_button, self.button_rect)

                # banner 
                Game.screen.blit(self.banner, self.banner_rect)

            # mise à jour
            pygame.display.flip()

            # gestion des évenements
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                
                if event.type == KEYDOWN:
                    self.pressed[event.key] = True

                    # détecter si la touche espace est enfoncée pour lancer une projectile
                    if event.key == K_SPACE:
                        self.player.launch_projectile()
                if event.type == KEYUP:
                    self.pressed[event.key] = False

                elif event.type == MOUSEBUTTONDOWN:
                    # vérifier que si le bouton est en collision avec la souris
                    if self.button_rect.collidepoint(event.pos):
                        # mettre le jeu lancé
                        self.start()


if __name__ == '__main__':
    Game().run()