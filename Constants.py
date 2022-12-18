

class Constants(object):

    def __init__(self):
        
        self._tile = 30
        self._resolution = self._width, self._height = 600,600
        self._cols = self._width // self._tile
        self._rows = self._height // self._tile

        self._wall_colour = (253, 253, 178)
        self._highlight_colour = (230,230,250)
        self._background_colour = (0,0,0)

    def get_tile(self) -> int: #getter method
        return self._tile

    def get_resolution(self) -> tuple: #getter method
        return self._resolution

    def get_width(self) -> int: #getter method
        return self._width

    def get_height(self) -> int: #getter method
        return self._height

    def get_cols(self) -> int: #getter method
        return self._cols

    def get_rows(self) -> int: #getter method
        return self._rows

    def get_wall_colour(self) -> tuple: #getter method
        return self._wall_colour

    def get_highlight_colour(self) -> tuple: #getter method
        return self._highlight_colour

    def get_background_colour(self) -> tuple: #getter method
        return self._background_colour

    def set_tile(self, tile) -> None: #setter method

        self._tile = tile
        self._resolution = self._width, self._height = 600,600
        self._cols = self._width // self._tile
        self._rows = self._height // self._tile

    def set_wall_colour(self, colour) -> None: #setter method
        self._wall_colour = colour

    def set_highlight_colour(self, colour) -> None: #setter method
        self._highlight_colour = colour

    def set_background_colour(self, colour) -> None: #setter method
        self._background_colour = colour

constants = Constants()

def get_constants():
    return constants