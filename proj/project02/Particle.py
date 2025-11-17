from Grid import *

class Particle:
    """A particle within a given grid with x,y cords.
    """
    def __init__(self, grid, x=0, y=0):
        """
        Args:
            grid (Grid): Grid Object
            x (int): x coordinate of the particle. Defaults to 0.
            y (int): y coordinate of the particle. Defaults to 0.
        """
        self.grid = grid
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{type(self).__name__}({self.x},{self.y})"
    
    def move(self):
        """If the move is valid it updates the particles position in the grid.
        """
        if self.physics() == None:
            return
        out_tuple = self.physics()
        self.grid.set(self.x,self.y,None)
        self.x = out_tuple[0]
        self.y = out_tuple[1]
        self.grid.set(self.x,self.y,self)