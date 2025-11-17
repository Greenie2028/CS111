class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [[None for y in range(width)] for x in range(height)]

    def in_bounds(self,x,y):
        return 0 <= x < self.width and 0 <= y < self.height
    
    def get(self, x, y):
        if self.in_bounds(x,y):
            return self.array[y][x]
        else:
            raise IndexError
    
    def set(self,x,y,val):
        if self.in_bounds(x,y):
            self.array[y][x] = val
            return
        else:
            raise IndexError
        
    def __str__(self):
        # Grid(<width>, <height>, first = <first element>)
        return f"Grid({self.width}, {self.height}, first = {self.array[0][0]})"

    def __repr__(self):
        return f"Grid({self.width}, {self.height}, first = {self.array[0][0]})"
    
    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        elif self.array == other.array:
            return True