def slicer_notes():
    # Slicing a string
    mystr = "Hello world"

    # Prints Hello
    print(mystr[:5])

    # Print world
    print(mystr[6:])

    # Print even indices starting at 0
    print(mystr[::2])

    # Print odd indices starting at 1
    print(mystr[1:0:2])

    # It works on regular strings
    print("tester"[::2])

    # Print it backwards!
    print(mystr[::-1])

def ranges():
    # Ranges
    for i in range(1,5):
        print(i)

def lst_comprehensions():
    # Making a list of even numbers from 0-20
    my_lst = []
    for i in range(0,21,2):
        my_lst.append(i)
    print(my_lst)

    # Making a list of multiples of 5 from 0-20 with a list comprehension
    comp_lst = [myvar for myvar in range(21) if myvar % 5 == 0]
    print(comp_lst)

    # All numbers from 0-100
    print([num for num in range(101)])

    # All even numbers from 2-200
    print([num * 2 for num in range(1,101)])

    # Even indices multipled by their value at that index
    lst = [1,2,3,4,5,6,7,8,9]
    print("\n")
    for index, item in enumerate(lst):
        if index % 2 == 0:
            print(index * item, end = " ")
    print("\n")
    
    # Even indices multipled by their value at that index with list comprehensions
    print([index * item for index, item in enumerate(lst) if index % 2 == 0])

if __name__ == "__main__":
    lst_comprehensions()