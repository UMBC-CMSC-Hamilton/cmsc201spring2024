"""
    Sorting lists is something you'll find yourself doing a lot
    
        Bubble Sort is a "kinda useless" sort but we teach it.
            it's pretty simple
    
    [4, 9, 2, 5, 6, 1, 8]
    bubble sort scans through the list and exchanges any two adjacent elements
    that are out of order
    [4, 9, 2, 5, 6, 1, 8]
    4 < 9 do nothing
    9 < 2 ? nope, out of order, swap
    [4, 2, 9, 5, 6, 1, 8]
    9 < 5 false, swap
    [4, 2, 5, 9, 6, 1, 8]
    9 < 6 false swap
    [4, 2, 5, 6, 9, 1, 8]
    9 < 1 false swap
    [4, 2, 5, 6, 1, 9, 8]
    9 < 8 false, swap
    [4, 2, 5, 6, 1, 8, 9] start: [4, 9, 2, 5, 6, 1, 8]
    
    again!
    [2, 4, 5, 6, 1, 8, 9]
    [2, 4, 5, 6, 1, 8, 9]
    [2, 4, 5, 1, 6, 8, 9]
    again!
    [2, 4, 5, 1, 6, 8, 9]
    [2, 4, 1, 5, 6, 8, 9]
    again!
    [2, 1, 4, 5, 6, 8, 9]
    again!
    [1, 2, 4, 5, 6, 8, 9]
    again!
    [1, 2, 4, 5, 6, 8, 9]
    no swaps means sorted
"""


def bubble_sort(the_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(the_list)):
            if the_list[i] > the_list[i + 1]:
                temp = the_list[i]
                the_list[i] = the_list[i + 1]
                the_list[i + 1] = temp
                swapped = True
    
    return the_list


"""
    Selection Sort - find min sort
"""

def selection_sort(the_list):
    #  notice that there's not really any choices
    for i in range(len(the_list)):
        min_index = i
        # start at position i because if we look before it, we'll accidentally
        # select already sorted elements
        for j in range(i, len(the_list)):
            if the_list[j] < the_list[min_index]:
                min_index = j
        # swap as usual
        if i != min_index:
            temp = the_list[min_index]
            the_list[min_index] = the_list[i]
            the_list[i] = temp
    
    return the_list