from Constants import Constants
from Cell import Cell

class Grid():
    
    def __init__(self, constants):
        
        self.constants = constants
        self.cols = self.constants.get_cols()
        self.rows = self.constants.get_rows()
        self.maze = []
        self.current_cell = None

    def construct_grid(self):
        """
        Initialise the 1D grid array
        """
        
        self.maze = [Cell(col, row, self.constants) for row in range (self.rows) for col in range (self.cols)]
        self.current_cell = self.maze[0]

    def display_grid(self):
        """
        Draws each Cell object in the pygame window
        """
        [cell.draw(self.constants) for cell in self.maze]