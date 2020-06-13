import pygame


class Fruit(pygame.sprite.Sprite):

    def __init__(self, name_fruit):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f'images/{name_fruit}.png')
        self.rect = self.image.get_rect()
        self.rect.x = 226
        self.rect.y = 250
