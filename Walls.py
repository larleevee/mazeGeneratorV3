import pygame


class Walls(pygame.sprite.Sprite):
    
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.mask = pygame.mask.from_surface(self.screen)

