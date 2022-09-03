import pygame
import time
import random
from Constants import Constants 


class Cell(Constants):

    def __init__(self, cols, rows):
        
        Constants.__init__(self)
        
        self.x_coord = cols
        self.y_coord = rows
        self.tile = self.get_tile()
        self.screen = pygame.display.get_surface()

        self.x_len = self.x_coord * self.tile
        self.y_len = self.y_coord * self.tile
        
        self.walls = {"north": True, "south": True, "east": True,  "west": True}
        self.visited = False
        
    
    def draw(self):
    
        if self.visited == True:
            pygame.draw.rect(self.screen, pygame.Color(0,0,0), (self.x_len, self.y_len, self.tile, self.tile))

        #draws in walls that the cell has left
        if self.walls["north"]:
            pygame.draw.line(self.screen, pygame.Color(230,230,250), (self.x_len, self.y_len), (self.x_len + self.tile, self.y_len), 2)
        if self.walls["east"]:
            pygame.draw.line(self.screen, pygame.Color(230,230,250), (self.x_len + self.tile, self.y_len), (self.x_len + self.tile, self.y_len + self.tile), 2)
        if self.walls["south"]:
            pygame.draw.line(self.screen, pygame.Color(230,230,250), (self.x_len + self.tile, self.y_len + self.tile), (self.x_len, self.y_len + self.tile), 2)
        if self.walls["west"]:
            pygame.draw.line(self.screen, pygame.Color(230,230,250), (self.x_len, self.y_len + self.tile), (self.x_len, self.y_len), 2)


    def mark_cell(self):
        
        pygame.draw.rect(self.screen, pygame.Color(253,253,150), (self.x_len + 2, self.y_len + 2, self.tile - 2, self.tile - 2))


    def check_valid(self, grid, x_coord, y_coord): #makes sure a given cell is in the grid

        cols = self.get_cols()
        rows = self.get_rows()
        find_index = lambda x_coord, y_coord: (x_coord + y_coord) * cols

        if (x_coord < 0) or (x_coord > cols - 1) or (y_coord < 0) or (y_coord > rows - 1):
            return False
        
        return grid[find_index(x_coord, y_coord)]
    

    def get_neighbours(self, grid):

        neighbours = []
        north = self.check_valid(grid, self.x_coord, self.y_coord - 1)
        east = self.check_valid(grid, self.x_coord + 1, self.y_coord)
        south = self.check_valid(grid, self.x_coord, self.y_coord + 1)
        west = self.check_valid(grid, self.x_coord - 1, self.y_coord)

        if north and not north.visited:
            neighbours.append(north)
        if east and not east.visited:
            neighbours.append(east)
        if south and not south.visited:
            neighbours.append(south)
        if west and not west.visited:
            neighbours.append(west)

        return neighbours
    
    
    def get_next(self, grid):
        
        if self.has_unvisited_neighbours(grid):
            return random.choice(self.get_neighbours(grid))
        

    def has_unvisited_neighbours(self, grid):

        if len(self.get_neighbours(grid)) != 0:
            return True
    

    def remove_wall(self, current_cell, chosen_cell):
        
        x_diff = current_cell.x_coord - chosen_cell.x_coord
        if x_diff == 1:
            current_cell.walls["west"] = False
            chosen_cell.walls["east"] = False
        elif x_diff == -1:
            current_cell.walls["east"] = False
            chosen_cell.walls["west"] = False

        y_diff = current_cell.y_coord - chosen_cell.y_coord
        if y_diff == 1:
            current_cell.walls["north"] = False
            chosen_cell.walls["south"] = False
        elif y_diff == -1:
            current_cell.walls["south"] = False
            chosen_cell.walls["north"] = False

