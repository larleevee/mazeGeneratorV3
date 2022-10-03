from Constants import Constants
from Cell import Cell


class Grid(Constants):
    
    def __init__(self):
        
        Constants.__init__(self)
        self.cols = self.get_cols()
        self.rows = self.get_rows()
        self.maze = []
        self.current_cell = None

    def construct_grid(self):
        
        self.maze = [Cell(col, row) for row in range (self.rows) for col in range (self.cols)]
        self.current_cell = self.maze[0]