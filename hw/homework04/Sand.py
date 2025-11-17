from Particle import *
class Sand(Particle):
    def is_move_okay(self,x,y):
        """Checks if the move is valid

        Args:
            x int: X cord for Sand to move to.
            y int: Y cord for Sand to move to.

        Returns:
            Boolean: Is Valid move
        """
        if not self.grid.in_bounds(x,y) or self.grid.get(x,y) != None: # Is the space in bounds and not occupied
            return False 
        if (self.x-1 == x or self.x+1 == x) and self.grid.get(x,y-1) != None:
            return False
        return True
    
    def physics(self):
        """Moves the particle down, then down left, then down right, if valid.

        Returns:
            tuple: (x,y)
        """
        if self.is_move_okay(self.x,self.y+1):
            return (self.x,self.y+1)
        if self.is_move_okay(self.x-1,self.y+1):
            return (self.x-1,self.y+1)
        if self.is_move_okay(self.x+1,self.y+1):
            return (self.x+1,self.y+1)