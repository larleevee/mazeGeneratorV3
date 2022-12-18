import pygame
from Walls import Walls


class Sprite(pygame.sprite.Sprite): #draws a square
    """
    Parent class for any object which will be drawn onto the base grid
    """

    def __init__(self, tile):

        pygame.sprite.Sprite.__init__(self)
        self.x_pos = 0
        self.y_pos = 0
        self.step = tile #the size of each gridspace, and the amount the tile will move
        self.screen = pygame.display.get_surface()
        self.highlight_colour = (0,0,0)

    def draw_square(self):
        """
        Draws the sprite
        """
        sprite = pygame.Rect(self.x_pos,self.y_pos,self.step,self.step) #makes a square which will fit into a grid space
        pygame.draw.rect(self.screen, self.highlight_colour, sprite)


class Player(Sprite):

    def __init__(self, tile):
        Sprite.__init__(self, tile)
        # self.mask = pygame.mask.from_surface(self.image)
        # self.walls = pygame.sprite.GroupSingle(Walls())
        self.highlight_colour = (253, 178, 230) #polymorphism

    def key_w(self, player):
        """
        Procedure for when user presses W key
        """
        #if not pygame.sprite.spritecollide(player.Sprite, self.walls.walls, False, pygame.sprite.collide_mask):
        self.y_pos -= self.step//10

    def key_a(self, player):
        """
        Procedure for when user presses A key
        """
        self.x_pos -= self.step//10

    def key_s(self, player):
        """
        Procedure for when user presses S key
        """
        self.y_pos += self.step//10


    def key_d(self, player):
        """
        Procedure for when user presses D key
        """
        self.x_pos += self.step//10

    def draw_square(self):
        """
        Draws the sprite (modified - polymorphism)
        """
        sprite = pygame.Rect(self.x_pos+self.step//5,self.y_pos+self.step//5,self.step//5,self.step//5)
        pygame.draw.rect(self.screen, self.highlight_colour, sprite)

    def collision(self, player, walls):
        pass


class Endpoint(Sprite):

    def __init__(self, tile, width, height):
        Sprite.__init__(self, tile)
        self.highlight_colour = (253, 178, 230) #polymorphism

        #draws from the top left corner of the bottom right tile
        self.x_pos = width - tile
        self.y_pos = height - tile

    def draw_square(self):
        """
        Draws the sprite (modified - polymorphism)
        """
        sprite = pygame.Rect((self.x_pos),(self.y_pos),self.step,self.step)
        pygame.draw.rect(self.screen, self.highlight_colour, sprite)