from sys import argv; from Grid import *; from random import shuffle

def file_write(maze:Grid, filename:str) -> None:
    with open(filename,'w') as file:
        for line in maze.array:
            file.write(''.join(line)+"\n")

def find_start(grid:Grid) -> list:
    """Finds the start of the maze in a given grid

    Args:
        grid (Grid): The maze

    Returns:
        list: [x,y] of the start. 
    """
    # All the test cases have the start in (1,1), so this saves resources.
    if grid.get(1,1) == "S":
        return [1,1]
    
    # So it still works if the start isn't (1,1).
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x,y) == "S":
                return [x,y]

def grid_search() -> None:
    """Searches the provided grid and returns a valid solution if one is found.
    """
    # Reading in the file
    grid_list = []
    args = argv[1:]
    with open(args[1]) as file:
        for line in file:
            grid_list.append(list(line.strip()))

    Grid.check_list_malformed(grid_list)

    grid = Grid.build(grid_list)
    solution_found = False

    def recursive_search(grid:Grid,xy:list) -> bool:
        nonlocal solution_found
        x = xy[0]
        y = xy[1]
        if solution_found:
            return solution_found
        if grid.get(x,y).upper() == "E":
            solution_found = True
            return solution_found
        if not grid.in_bounds(x,y) or grid.get(x,y) in ["#","."]:
            return solution_found
        if grid.get(x,y) == " ":
            grid.set(x,y,".")

        recursive_search(grid,[x+1,y])
        recursive_search(grid,[x-1,y])
        recursive_search(grid,[x,y+1])
        recursive_search(grid,[x,y-1])
        if grid.get(x,y) != "S" and not solution_found:
            grid.set(x,y," ")
        return solution_found
    
    if recursive_search(grid, find_start(grid)):
        print("Success! The path is as follows:")
        for line in grid.array:
            for item in line:
                print(item,end ="")
            print()
    else:
        print("Error! Solver could find no solution to maze!")

def grid_generate(w, h, filename):
    if w % 2 == 0:
        w += 1
    if h % 2 == 0:
        h += 1

    grid = Grid(w,h)
    for x in range(w):
        for y in range(h):
            grid.set(x,y,'#')
    
    def gen_helper(x,y):
        nonlocal grid
        grid.set(x,y,' ')
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        shuffle(dirs)
        for dir in dirs:
            new_x = x + 2*dir[0]
            new_y = y + 2*dir[1]
            if grid.in_bounds(new_x,new_y) and grid.get(new_x,new_y) == '#':
                grid.set(x+dir[0],y+dir[1],' ')
                grid.set(new_x, new_y, ' ')
                gen_helper(new_x,new_y)
            else:
                continue
            
    gen_helper(1,1)
    grid.set(1,1,'S')
    grid.set(w-2,h-2,'E')
    file_write(grid, filename)

def main():
    try:
        args = argv[1:]
    except:
        print("Error: Invalid number of arguments")
        return
    if len(args) < 2 or len(args) > 4:
        print("Usage: python3 maze_solver.py [-s maze_file] [-g width height maze_file]") 
        return
    if args[0] == '-s':
        if len(args) > 2:
            print("Usage: [-s maze_file]")
            return
        try:
            grid_search()
        except RecursionError:
            print("Error! maximum recursion depth exceeded!")
            return
    elif args[0] == '-g':
        if len(args) < 4:
            print("Usage: [-g width height maze_file]")
            return
        try:
            int(args[1])
            int(args[2])
        except:
            print("Invalid height or width! Must be intergers!")
            return
        if int(args[1]) < 3 or int(args[2]) < 5:
            print("Error! Minimum maze size is 3x5!")
            return
        grid_generate(int(args[1]),int(args[2]),args[3])
    else:
        print("Error! Invalid flag. [-s maze_file] [-g maze_file]")
        return

if __name__ == "__main__":
    main()
