import pygame
import random
import time
from Constants import get_constants
from Cell import Cell
from Grid import Grid
from Sprite import Player, Endpoint
from Walls import Walls


def mainCode(difficulty):
    
    #Initialise all objects and variables
    constants = get_constants()
    constants.set_tile(difficulty)

    pygame.init()
    screen = pygame.display.set_mode(constants.get_resolution())
    clock = pygame.time.Clock()
    grid = Grid(constants)
    grid.construct_grid()
    maze = grid.maze
    current_cell = grid.current_cell
    player = Player(constants.get_tile())
    endpoint = Endpoint(constants.get_tile(), constants.get_width(), constants.get_height())

    #loops for different processes
    running = True
    constructing = True

    while constructing: #constructs the base maze
        screen.fill(constants.get_wall_colour())
        dfs(grid, maze, clock, grid.current_cell, constants)
        pygame.display.flip()
        grid.display_grid() #redraws the base maze (clears the screen)
        constructing = False #finished constructing the base maze

    walls = Walls()
        
    while running: #gameloop
        for event in pygame.event.get(): #iterates through all user input/commands
            if event.type == pygame.QUIT:
                running = False
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                player.key_w(player)
                clock.tick(20)
            if keys[pygame.K_a]:
                player.key_a(player)
                clock.tick(20)
            if keys[pygame.K_s]:
                player.key_s(player)
                clock.tick(20)
            if keys[pygame.K_d]:
                player.key_d(player)
                clock.tick(20)
        
        grid.display_grid() #redraws the base maze (clears the screen)
        player.draw_square()
        endpoint.draw_square()
        pygame.display.flip()

    pygame.quit() #quits if exit game loop   


def dfs(grid, maze, clock, current_cell, constants):
    """
    Recursive DFS algorithm
    """
    
    grid.display_grid()

    current_cell.visited = True

    while current_cell.has_unvisited_neighbours(maze, constants): #once false, routine unwinds
        chosen_cell = current_cell.get_next(maze, constants)
        current_cell.remove_wall(current_cell, chosen_cell)
        pygame.display.flip()
        clock.tick(60) #fps
        
        dfs(grid, maze, clock, chosen_cell, constants)
    
    return maze
