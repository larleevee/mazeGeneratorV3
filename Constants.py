

class Constants:

    def __init__(self):
        
        self.tile = 30
        self.resolution = self.width, self.height = 600,600
        self.cols = self.width // self.tile
        self.rows = self.height // self.tile
        
        self.wall_colour = (230,230,250)
        self.highlight_colour = (253,253,150)
        self.background_colour = (0,0,0)

    def get_tile(self):
        return self.tile

    def get_resolution(self):
        return self.resolution

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows
    
    def get_wall_colour(self):
        return self.wall_colour

    def get_highlight_colour(self):
        return self.highlight_colour

    def get_background_colour(self):
        return self.background_colour
