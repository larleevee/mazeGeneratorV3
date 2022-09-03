

class Constants:

    def __init__(self):
        
        self.tile = 30
        self.resolution = self.width, self.height = 600,600
        self.cols = self.width // self.tile
        self.rows = self.height // self.tile

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
