from sys import argv

def file_read(file_name:str) -> list:
    """Opens a file and output each line in a list.

    Args:
        file_name (string): file name

    Returns:
        list: Contains each line of the file
    """
    with open(file_name, 'r') as input_file:
        lines = input_file.readlines()
    output_list = []
    for line in lines:
        output_list.append(line.strip())
    return output_list

def file_write(file_name:str, lst:list) -> None:
    """Writes a list to a file

    Args:
        file_name (string): file name
        lst (list): list to write to file
    """
    with open(file_name, 'w') as out_file:
        for line in lst:
            out_file.write(f"{line}\n")

def merge(list_a:list,list_b:list) -> list:
    """Merge sorts two already sorted lists

    Args:
        list_a (list): Sorted list
        list_b (list): Sorted list

    Returns:
        list: A sorted list combining the two inputs
    """
    a = 0
    b = 0
    a_max = len(list_a) - 1
    b_max = len(list_b) - 1
    sorted_list = []
    while a <= a_max and b <= b_max:
        if list_a[a] < list_b[b]:
            sorted_list.append(list_a[a])
            a += 1
        else:
            sorted_list.append(list_b[b])
            b += 1
    if a_max >= a:
        sorted_list += list_a[a:]
    if b_max >= b:
        sorted_list += list_b[b:]
    return sorted_list

def sort(lst:list) -> list:
    """Recursively sorts an unsorted list using merge sort

    Args:
        lst (list): Unsorted list

    Returns:
        list: Sorted list

    >>> sort([3, 1, 4, 1, 5, 9])
    [1, 1, 3, 4, 5, 9]
    >>> sort([])
    []
    >>> sort([42])
    [42]
    >>> sort([5, -2, 0, 7])
    [-2, 0, 5, 7]
    """
    return merge(sort(lst[0:len(lst)//2]), sort(lst[len(lst)//2:])) if not len(lst)<=1 else lst

def main():
    file_write(argv[2], sort(file_read(argv[1])))
    
    
    

if __name__ == "__main__":
    main()