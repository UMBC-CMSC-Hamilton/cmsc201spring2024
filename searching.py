"""
    There are two types of sorting that we'll do in this class.
        One is linear searching -
            on an unsorted list
"""

"""
    Linear searching, scanning through the list element by element
    
    Let's say that the list is size = n.
    Worst Case: linear search can take up to n "steps"
        [this is the important one for now]
    In the best case: We take about 1 step.
    Average Case: about n/2 steps on average <--
"""
def look_for_element(my_list, the_element):
    for i in range(len(my_list)):
        if my_list[i] == the_element:
            return True
        
    return False

"""
    What if the list is sorted? Is there a better way to find elements?
     0  1  2  3  4  5   6   7   8   9  10   11  12
    [1, 3, 5, 8, 9, 12, 15, 20, 31, 32, 37, 50, 53] n = 13 things
    1, 3, 5, 8, 9, 12, 15 or 20, 31, 32, 37, 50, 53 <-- this one
    [20, 31, 32, 37, 50, 53] n = 6, use n // 2 6//2 = 3
      0   1   2   3   4   5
    [20, 31, 32] n = 3, 3 // 2 == 1
     find 31 and we're good
     0  1   2  3   4   5   6   7   8
    [2, 8, 10, 15, 17, 21, 25, 31, 77] look for 13
    n = 9
    9//2 = 4 13 < 17 so low
    [2, 8, 10, 15] n = 4 // 2 == 2
     0  1   2   3
     check 10 < 13 go up
    [15] n = 1 n//2 == 0
        return False
"""

def binary_search(the_list, the_element):
    print(the_list, end=' ')
    if not the_list:
        print()
        return False
    elif len(the_list) == 1:
        print()
        return the_list[0] == the_element
    
    middle_index = len(the_list) // 2
    print(the_list[middle_index])
    if the_element == the_list[middle_index]:
        return True
    elif the_element < the_list[middle_index]:
        return binary_search(the_list[0:middle_index], the_element)
    else:
        return binary_search(the_list[middle_index + 1:], the_element)
    
"""
    How many steps does this thing take?
        100 => 50 => 25 => 12 => 6 => 3 => 1 (the end)\
        6 steps for a list of about size 100
        400 => 200 => 100 => 6 more steps
        8 steps
        Number of times you can divide by 2 until you reach approx 1.
        
        n / ( 2 * 2 * 2 * ... * 2 ) ~= 1
        n / 2^steps ~= 1
        n ~= 2^steps
        lg = log_2 <-- very common
        ln = log_e  <-- rare
        log = log_10 <-- sometimes
        
        lg(n) ~ steps
"""

import random

my_list = [random.randint(0, 50) for _ in range(20)]
my_list.sort()
# need a sorted list to run binary search
# [4, 2, 77, 3, 9, 12, 5, 81]
print(my_list)
x = int(input('What element to search for: '))
print(binary_search(my_list, x))
