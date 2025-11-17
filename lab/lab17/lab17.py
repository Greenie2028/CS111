def load_grid(filename:str) -> list:
    """Loads a grid from provided file name

    Args:
        filename (str): Name of input file

    Returns:
        list: 2d grid
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    pieces = [line.strip() for line in lines]
    return [list(word) for word in pieces]

def exists(grid:list, word:str) -> bool:
    r = 0
    c = 0
    for x in range(len(grid)):
        print(f"x:{x}")
        for y in range(len(grid[0])):
            print(f"y:{y}")
            if grid[x][y] == word[0]:
                r = x
                c = y
                break

    def search(grid:list, word:str, row:int, col:int) -> bool:
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return False
       
        if word[0] == grid[row][col]:
            if len(word) == 1:
                return True
            char = word[0]
            grid[row][col] = '#'
            if search(grid, word[1:],row+1,col):
                grid[row][col] = char
                return True
            if search(grid, word[1:],row-1,col):
                grid[row][col] = char
                return True
            if search(grid, word[1:],row,col+1):
                grid[row][col] = char
                return True
            if search(grid, word[1:],row,col-1):
                grid[row][col] = char
                return True
        return False
        
    return search(grid, word, r, c)