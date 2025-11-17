from Grid import Grid
from random import random

"""*** BEGIN PROVIDED CODE ***"""
def print_grid(grid):
    """
    Prints a Grid object with all the elements of a row
    on a single line separated by spaces.
    """
    for y in range(grid.height):
        for x in range(grid.width):
            print(grid.get(x, y) if grid.get(x, y) is not None else 0, end=" ")
        print()
    print()
"""*** END PROVIDED CODE ***"""

# Randomly spreads rocks over a grid, only filling empty spaces.
def random_rocks(grid, chance_of_rock):
    """
    Take a grid, loop over it and add rocks randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.
    """
    """*** YOUR CODE HERE ***"""
    new_grid = grid.copy()
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x,y) == None and chance_of_rock > random():
                new_grid.set(x,y,'r')
    return new_grid

# Randomly spreads bubbles over a grid, only filling empty spaces.
def random_bubbles(grid, chance_of_bubbles):
    """
    Take a grid, loop over it and add bubbles 'b' randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.
    """
    """*** YOUR CODE HERE ***"""
    new_grid = grid.copy()
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x,y) == None and chance_of_bubbles > random():
                new_grid.set(x,y,'b')
    return new_grid

# Combines the other functions, randomly distrubuting the character throughout the list
def modify_grid(grid, char, prob):
    """
    Write a function which can take in a grid, a single character
    and a probability as parameters and updates the grid using
    the character passed in.
    """
    """*** YOUR CODE HERE ***"""
    new_grid = grid.copy()
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x,y) == None and prob > random():
                new_grid.set(x,y,char)
    return new_grid

# Moves a single bubble up
def bubble_up(grid, x, y):
    """
    Write a function that takes a bubble that is known
    to be able to bubble up and moves it up one row.
    """
    """*** YOUR CODE HERE ***"""
    new_grid = grid.copy()
    if y > 0:
        new_grid.set(x,y-1,'b')
        new_grid.set(x,y,None)
    return new_grid

# Checks if there is nothing above a bubble and causes it to move up, replacing its old spot with a None value
def move_bubbles(grid):
    """
    Write a function that loops over the grid, finds
    bubbles, checks if the bubble can move upward, moves
    the bubble up.
    """
    """*** YOUR CODE HERE ***"""
    new_grid = grid.copy()
    for y in range(1, grid.height):
        for x in range(grid.width):
            if new_grid.get(x,y-1) == None and new_grid.get(x,y) == 'b':
                new_grid.set(x,y-1,'b')
                new_grid.set(x,y,None)
    return new_grid

"""*** BEGIN PROVIDED CODE ***"""
def animate_grid(grid, delay):
    """
    Given an Grid object, and a delay time in seconds, this
    function prints the current grid contents (calls print_grid),
    waits for `delay` seconds, calls the move_bubbles() function,
    and repeats until the grid doesn't change.
    """
    from time import sleep
    prev = grid
    count = 0
    message = "Start"
    while True:
        print("\033[2J\033[;H", end="")
        message = f"Iteration {count}"
        print(message)
        print_grid(prev)
        sleep(delay)
        newGrid = move_bubbles(prev)
        if newGrid == prev:
            break
        prev = newGrid
        count += 1
"""*** END PROVIDED CODE ***"""