import pygame
import random
from Constants import Constants
from Cell import Cell
from Grid import Grid


def mainCode():
    
    constants = Constants()
    pygame.init()
    screen = pygame.display.set_mode(constants.get_resolution())
    clock = pygame.time.Clock()
    grid = Grid()
    grid.construct_grid()
    maze = grid.maze
    current_cell = grid.current_cell

    while True:
        screen.fill(constants.get_wall_colour())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        dfs(maze, clock, grid.current_cell)
        # current_cell.mark_as_start()
        # grid[len(grid)-1].mark_as_end()

        pygame.display.flip()
        clock.tick(60)


def dfs(maze, clock, current_cell):
    
    [cell.draw() for cell in maze]

    current_cell.visited = True
    current_cell.mark_cell()

    while current_cell.has_unvisited_neighbours(maze):
        chosen_cell = current_cell.get_next(maze)
        current_cell.remove_wall(current_cell, chosen_cell)
        pygame.display.flip()
        clock.tick(40) #fps
        
        dfs(maze, clock, chosen_cell)

    
        
mainCode()
