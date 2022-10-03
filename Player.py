import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0,0,40,40)
        self.screen = pygame.display.get_surface()
        self.highlight_colour = (253,253,150)

    def draw_player(self):
        pygame.draw.rect(self.screen, self.highlight_colour, self.rect)
        pygame.display.flip()
