import pygame
import time
import random
#from Constants import Constants 


class Cell():
    
    def __init__(self, cols, rows, constants):

        constants = constants

        self.x_coord = cols
        self.y_coord = rows
        self.tile = constants.get_tile()
        self.screen = pygame.display.get_surface()

        self.x_len = self.x_coord * self.tile
        self.y_len = self.y_coord * self.tile
        
        self.walls = {"north": True, "south": True, "east": True,  "west": True}
        self.visited = False #backtrack marker
        
        
    def draw(self, constants):
        """
        Draws in all walls which haven't been "knocked down"
        """

        if self.visited:
            pygame.draw.rect(self.screen, constants.get_background_colour(), (self.x_len, self.y_len, self.tile, self.tile))
        if self.walls["north"]:
            pygame.draw.line(self.screen, constants.get_wall_colour(), (self.x_len, self.y_len), (self.x_len + self.tile, self.y_len), 2)
        if self.walls["south"]:
            pygame.draw.line(self.screen, constants.get_wall_colour(), (self.x_len + self.tile, self.y_len + self.tile), (self.x_len, self.y_len + self.tile), 2)
        if self.walls["east"]:
            pygame.draw.line(self.screen, constants.get_wall_colour(), (self.x_len + self.tile, self.y_len), (self.x_len + self.tile, self.y_len + self.tile), 2)
        if self.walls["west"]:
            pygame.draw.line(self.screen, constants.get_wall_colour(), (self.x_len, self.y_len + self.tile), (self.x_len, self.y_len), 2)

    def check_valid(self, grid, x_coord, y_coord, constants):
        """
        Makes sure a given Cell is actually in the grid
        """

        cols = constants.get_cols()
        rows = constants.get_rows()
        find_index = lambda x_coord, y_coord: x_coord + y_coord * cols

        if (x_coord < 0) or (x_coord > cols - 1) or (y_coord < 0) or (y_coord > rows - 1):
            return False

        return grid[find_index(x_coord, y_coord)]

    def get_next(self, grid, constants):
        """
        Random select an unvisited neighbour cell to traverse to
        """
        
        if self.has_unvisited_neighbours(grid, constants):
            return random.choice(self.get_neighbours(grid, constants))   

    def has_unvisited_neighbours(self, grid, constants):
        """
        Check if the current cell has neighbours which can be traversed to
        (If not, this is the base case for the recursive DFS)
        """

        if len(self.get_neighbours(grid, constants)) != 0:
            return True

    def get_neighbours(self, grid, constants):
        """
        Returns all neighbour cells which are in the grid
        """

        neighbours = []
        north = self.check_valid(grid, self.x_coord, self.y_coord - 1, constants)
        if north and not north.visited:
            neighbours.append(north)
        
        south = self.check_valid(grid, self.x_coord, self.y_coord + 1, constants)
        if south and not south.visited:
            neighbours.append(south)
        
        east = self.check_valid(grid, self.x_coord + 1, self.y_coord, constants)
        if east and not east.visited:
            neighbours.append(east)

        west = self.check_valid(grid, self.x_coord - 1, self.y_coord, constants)
        if west and not west.visited:
            neighbours.append(west)
        
        return neighbours


    def remove_wall(self, current_cell, chosen_cell):
        """
        "Knocks down" a wall between the current cell and the next (chosen) cell
        """
        
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

