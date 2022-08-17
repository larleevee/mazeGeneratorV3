import random


class Cell:

    def __init__(self, x_coord, y_coord):
        
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.visited = False
        self.walls = {"left": True, "right": True, "up": True, "down": True}

    def validateAdj(self, grid, x_len, y_len, x_coord, y_coord): #makes sure a cell is in the grid

        findIndex = lambda x_coord, y_coord: (x_coord + y_coord) * y_len

        if (x_coord < 0) or (x_coord > y_len - 1) or (y_coord < 0) or (y_coord > x_len - 1):
            return False

        print(x_coord, y_coord)
        
        return grid[findIndex(x_coord, y_coord)]

    def nextCell(self, grid, x_len, y_len):

        self.grid = grid
        adjacent_cells = list()
        left = self.validateAdj(grid, x_len, y_len, self.x_coord - 1, self.y_coord)
        right = self.validateAdj(grid, x_len, y_len, self.x_coord + 1, self.y_coord)
        up = self.validateAdj(grid, x_len, y_len, self.x_coord, self.y_coord - 1)
        down = self.validateAdj(grid, x_len, y_len, self.x_coord, self.y_coord + 1)

        if left and not left.visited:
            adjacent_cells.append(left)
        if right and not right.visited:
            adjacent_cells.append(right)
        if up and not up.visited:
            adjacent_cells.append(up)
        if down and not down.visited:
            adjacent_cells.append(down)

        if adjacent_cells:
            return random.choice(adjacent_cells)
        else:
            return False #there are no adjacent cells, dead end


def removeWalls(current_cell, adjacent_cell):
    pass
        

def iterativeDFS(initialCell, stack, grid, x_len, y_len): #the standard algorithm
    
    initial_cell.visited = True
    stack.append(initial_cell)

    while len(stack) != 0:
        print("while")
        print(stack)
        current_cell = stack.pop()
        
        if current_cell.nextCell(grid, x_len, y_len) != False:
            print("if 1")
            stack.append(current_cell)
            next_cell = current_cell.nextCell(grid, x_len, y_len)

            if next_cell:
                print("if 2")
                #current_cell.removeWalls(current_cell, next_cell)
                next_cell.visited = True
                stack.append(next_cell)
                

x_len = 5
y_len = 5

grid = list()
for row in range(x_len):
    for column in range(y_len):
        new_cell = Cell(column, row)
        grid.append(new_cell)
        
initial_cell = grid[0]
stack = list() #stack
iterativeDFS(initial_cell, stack, grid, x_len, y_len)
print("done")
            

