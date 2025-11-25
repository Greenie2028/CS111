def hack_it(func):
    def hacked_func(lst):
        return "Git Hakt"

    return hacked_func

@hack_it
def double_list(some_list:list) -> list:
    """Simple function that concatenates a function to itself

    Args:
        some_list (list): a list

    Returns:
        list: a list twice as long
    """
    return some_list*2

print(double_list([1,2,3]))