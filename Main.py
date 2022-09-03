import pygame
import time
import random
from Constants import Constants
from Cell import Cell


def mainCode():
    
    constants = Constants()
    pygame.init()
    screen = pygame.display.set_mode(constants.get_resolution())
    clock = pygame.time.Clock()
    grid = [Cell(col, row) for row in range (constants.get_rows()) for col in range (constants.get_cols())]
    current_cell = grid[0]

    while True:
        screen.fill(pygame.Color(215,210,203))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        dfs(grid, current_cell)

        pygame.display.flip()
        clock.tick(300)


def dfs(grid, current_cell):
    
    [cell.draw() for cell in grid]

    current_cell.visited = True
    current_cell.mark_cell()

    while current_cell.has_unvisited_neighbours(grid):
        chosen_cell = current_cell.get_next(grid)
        current_cell.remove_wall(current_cell, chosen_cell)

        dfs(grid, chosen_cell)

    
        
mainCode()
