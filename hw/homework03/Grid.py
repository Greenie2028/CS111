from copy import deepcopy
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
        return f"Grid.build({repr(self.array)})"
    
    # Checks if two Grids or if the list is equal to the Grid
    def __eq__(self, other):
        if isinstance(other, Grid) and self.array == other.array:
            return True
        elif isinstance(other, list) and self.array == other:
            return True
        return False
        
    # Checks if the given list is a valid one to make a list from
    @staticmethod
    def check_list_malformed(import_list):
        if not isinstance(import_list, list):
            raise ValueError(f"Incorrect type. Expected type: List. Recieved Type {type(import_list)}")
        if len(import_list) < 1:
            raise ValueError("Invalid List size. List must contain 1 or more values")
        all_lists = True
        for item in import_list:
            if type(item) != list:
                all_lists = False
        if not all_lists:
            raise ValueError("Invalid items in list. Must contain only lists")
        list_len = len(import_list[0])
        same_len = True
        for item in import_list:
            if len(item) != list_len:
                same_len = False
        if not same_len:
            raise ValueError("Invalid list sizings. All nested lists must be the same size.")
    
    # Creates a new Grid from a valid list
    @staticmethod   
    def build(new_grid_list):
        Grid.check_list_malformed(new_grid_list)
        height = len(new_grid_list)
        width = len(new_grid_list[0])
        new_Grid_obj = Grid(width,height)
        for y in range(len(new_grid_list)):
            for x in range(len(new_grid_list[y])):
                new_Grid_obj.set(x,y,new_grid_list[y][x])
        return new_Grid_obj
    
    # Copies the list it is called on
    def copy(self):
        return Grid.build(self.array)

