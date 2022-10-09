import pygame

class Square(pygame.sprite.Sprite):

    def __init__(self, tile):

        pygame.sprite.Sprite.__init__(self)
        self.x_pos = 0
        self.y_pos = 0
        self.step = tile
        self.screen = pygame.display.get_surface()
        self.highlight_colour = (253,253,150)

    def draw_player(self):
        sprite = pygame.Rect(self.x_pos,self.y_pos,self.step,self.step) #makes a 40x40 square which will move 40
        pygame.draw.rect(self.screen, self.highlight_colour, sprite)
        pygame.display.flip()

    def key_w(self):
        self.y_pos -= self.step

    def key_a(self):
        self.x_pos -= self.step

    def key_s(self):
        self.y_pos += self.step

    def key_d(self):
        self.x_pos += self.step


class Player(Square):

    def __init__(self, tile):
        Square.__init__(self, tile)
