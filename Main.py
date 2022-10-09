import pygame
import random
import time
from Constants import Constants
from Cell import Cell
from Grid import Grid
from Player import Player


def mainCode():
    
    constants = Constants()
    pygame.init()
    screen = pygame.display.set_mode(constants.get_resolution())
    clock = pygame.time.Clock()
    grid = Grid()
    grid.construct_grid()
    maze = grid.maze
    current_cell = grid.current_cell
    player = Player(constants.get_tile())

    running = True
    constructing = True


    while running: #gameloop

        for event in pygame.event.get(): #iterates through all user input/commands
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN: #if a key is pressed
                if event.key == pygame.K_w:
                    player.key_w()
                if event.key == pygame.K_a:
                    player.key_a()
                if event.key == pygame.K_s:
                    player.key_s()
                if event.key == pygame.K_d:
                    player.key_d()

        while constructing: #constructs the base maze
            screen.fill(constants.get_wall_colour())
            dfs(maze, clock, grid.current_cell)
            pygame.display.flip()
            [cell.draw() for cell in maze] #redraws the base maze (clears the screen)
            constructing = False #finished constructing the base maze
            
        [cell.draw() for cell in maze] #redraws the base maze (clears the screen)
        player.draw_player()

    pygame.quit() #quits if exit game loop   


def dfs(maze, clock, current_cell):
    
    [cell.draw() for cell in maze]

    current_cell.visited = True

    while current_cell.has_unvisited_neighbours(maze):
        chosen_cell = current_cell.get_next(maze)
        current_cell.remove_wall(current_cell, chosen_cell)
        pygame.display.flip()
        clock.tick(120) #fps
        
        dfs(maze, clock, chosen_cell)
    
    return maze
       
mainCode()
