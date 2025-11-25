# s is a list
def avg(s):
    '''
    This function is supposed to return the average of the values
    of s.
    >>> avg([2,2,2])
    2.0

    '''
    return sum(s) / len(s)
    
avg([2.1234,2,2])