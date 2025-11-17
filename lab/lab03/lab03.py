def average_temperature(temps):
    """
    Given a list of temperatures, TEMPS, compute the average
    temperature and return it to the user
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> average_temperature(temp_data)
    75.15
    """
    ### Takes a list of floats and returns the average
    temp_average = 0.0
    for i in range(len(temps)):
        temp_average += temps[i]
    temp_average = temp_average / len(temps)
    return temp_average


def hot_days(temps):
    """
    Given a list of temperatures, TEMPS, count the number of days
    more than five degrees above the average.  Print the number of
    days and the average and return the number of days.
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> hot_days(temp_data)
    There were 2 day(s) more than 5 degrees above the average of 75.2.
    2
    """
    ### Counts how many days where the temperature was at least 5 degrees higher than the avg. temp
    avg_temp = average_temperature(temps)
    hot_day_counter = 0
    for i in range(len(temps)):
        if (temps[i] - 5.0) > avg_temp:
            hot_day_counter += 1
    print(f"There were {hot_day_counter} day(s) more than 5 degrees above the average of {round(avg_temp, 1)}.")
    return hot_day_counter

def is_palindrome(word):
    """
    Given a single word, WORD, determine if it is a palindrome or not.
    Print a message that includes the word stating it is or is not a
    palindrome and return True if it is and False otherwise
    >>> is_palindrome('rotator')
    rotator is a palindrome.
    True
    >>> is_palindrome('apple')
    apple is not a palindrome.
    False
    """
    ### Checks if the word is a palindrome and returns true or false
    reversed_word = word[::-1]
    if reversed_word == word:
        print(f"{word} is a palindrome.")
        return True
    else:
        print(f"{word} is not a palindrome.")
        return False

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    ### This code takes the list and returns a list of the numbers at the even indexes multiplied by their index
    return [s[i]*i for i in range(len(s)) if i % 2 == 0]