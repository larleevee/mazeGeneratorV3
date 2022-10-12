import pygame

class Square(pygame.sprite.Sprite):

    def __init__(self, tile):

        pygame.sprite.Sprite.__init__(self)
        self.x_pos = 0
        self.y_pos = 0
        self.step = tile #the size of each gridspace, and the amount the tile will move
        self.screen = pygame.display.get_surface()
        self.highlight_colour = (0,0,0)

    def draw_square(self):
        sprite = pygame.Rect(self.x_pos,self.y_pos,self.step,self.step) #makes a square which will fit into a grid space
        pygame.draw.rect(self.screen, self.highlight_colour, sprite)


class Player(Square):

    def __init__(self, tile):
        Square.__init__(self, tile)
        self.highlight_colour = (253,253,150) #polymorphism(?)

    def key_w(self):
        self.y_pos -= self.step

    def key_a(self):
        self.x_pos -= self.step

    def key_s(self):
        self.y_pos += self.step

    def key_d(self):
        self.x_pos += self.step

    def draw_square(self):
        sprite = pygame.Rect(self.x_pos,self.y_pos,self.step,self.step) #makes a 40x40 square which will move 40
        pygame.draw.rect(self.screen, self.highlight_colour, sprite)

    def collision(self):
        pass


class Endpoint(Square):

    def __init__(self, tile, width, height):
        Square.__init__(self, tile)
        self.highlight_colour = (253,253,150) #polymorphism(?)

        #draws from the top left corner of the bottom right tile
        self.x_pos = width - tile
        self.y_pos = height - tile

    def draw_square(self):
        sprite = pygame.Rect(self.x_pos,self.y_pos,self.step,self.step) #makes a 40x40 square which will move 40
        pygame.draw.rect(self.screen, self.highlight_colour, sprite)

    def collision(self):
        pass
