"""
    insertion sorting
        pulling back elements into position
        
    
    [10, 7, 12, 9, 3, 5, 18, 2]
    [7, 10, 12, 9, 3, 5, 18, 2] i = 2, nothing to do 12 is in the right spot
    [7, 9, 10, 12, 3, 5, 18, 2] i = 3 swap 9 two positions.
    [3, 7, 9, 10, 12, 5, 18, 2] i = 4
    [3, 5, 7, 9, 10, 12, 18, 2] i = 5
    [3, 5, 7, 9, 10, 12, 18, 2] i = 6, 18 doesn't need to move, leave it
    [2, 3, 5, 7, 9, 10, 12, 18] i = 7
    
    bubble, insertion, selection all use swapping in order to sort the list

"""

from quadratic_sorting import bubble_sort, selection_sort
import random
import time
import sys

sys.setrecursionlimit(10000)

def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        cur_ind = i
        while cur_ind > 0 and a_list[cur_ind] < a_list[cur_ind - 1]:
            temp = a_list[cur_ind]
            a_list[cur_ind] = a_list[cur_ind - 1]
            a_list[cur_ind - 1] = temp
            
            cur_ind -= 1
    return a_list

a_list = [1, 2, 3, 5, 7, 19, 21, 4]
x = a_list.sort()  # uses merge sort and insertion sort.
print(x, a_list)

# changes the original list
# sorted keyword returns a new list which is sorted with the original data

rand_list = [random.randint(0, 100) for _ in range(20)]
print(rand_list)
insertion_sort(rand_list)
print(rand_list)


"""
    MergeSort
    
        first example should be on a list of size 8
        
        MS([3, 20, 8, 17, 15, 2, 4, 1])
        MS([3, 20, 8, 17]) MS([15, 2, 4, 1])
        [3, 20]     [8, 17]
        [3] [20]    [8] [17]
             .              .
        [3, 20]     [8, 17]
        [3, 8, 17, 20] (sorted the list)
        
        [15, 2, 4, 1]
        [15, 2]     [4, 1]
         .      .    .     .
        [15] [2]    [4] [1]
             v         v
        [2, 15] [1, 4]
        [1, 2, 4, 15]
               v                        v
        [3, 8, 17, 20]    [1, 2, 4, 15]
        [1, 2, 3, 4, 8, 15, 17, 20]
        
        compare n^2 to n lg(n) <-- will win because lg(n) <<<  n
"""

def merge(first_list, second_list):
    first_index = 0
    second_index = 0
    
    results = []
    
    while first_index < len(first_list) and second_index < len(second_list):
        if first_list[first_index] < second_list[second_index]:
            results.append(first_list[first_index])
            first_index += 1
        else:
            results.append(second_list[second_index])
            second_index += 1
    
    for i in range(first_index, len(first_list)):
        results.append(first_list[i])
    
    for j in range(second_index, len(second_list)):
        results.append(second_list[j])
        
    return results


def merge_sort(a_list):
    # print(a_list)
    if len(a_list) <= 1:
        return a_list
    middle = len(a_list) // 2
    left_side = merge_sort(a_list[0: middle])
    right_side = merge_sort(a_list[middle: len(a_list)])
    return merge(left_side, right_side)

print('Ready to merge')
new_list = [random.randint(0, 50) for _ in range(16)]
print(new_list)
new_list = merge_sort(new_list)
print(new_list)


"""
    insertion and all of merge sort

    The last sort we'll talk about is "QuickSort"
    
"""
L = []
L.sort()  # uses merge sort on large lists

"""
    QuickSort may remind you of MergeSort
    
    in QuickSort we pick a pivot element
        form two lists (maybe even 3 if we're creative)
        less_list (less than the pivot)
        greater_list (greater than or equal to the pivot)
     p
    [7 3 9 2 1 5 4 8 7 6]
    p = 7
    DO NOT ADD THE PIVOT TO EITHER LIST
    less_list = [3, 2, 1, 5, 4, 6]
        p = 3
        [2, 1] [5, 4, 6]
        2 [1] [] ==> [1, 2]
        p = 5 [4] [6]
        [4, 5, 6]
        [1, 2, 3, 4, 5, 6]
    greater_list = [9, 8, 7]
        p = 9
        [8, 7] []
        p = 8 [7] [] ==> [7, 8]
        [7, 8, 9]
    
    [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
    notice is that the less_list and greater_list don't always split
        perfectly in half.
        
    [1, 2, 3, 4, 5, 6, 7]
    p = 1
    less_list = []
    greater_list = [2, 3, 4, 5, 6, 7]
    
    [1, 2, 3, 4, 5]
    
    p = 1
    [] [1, 2, 3, 4, 5]
"""

def quick_sort(the_list):
    if len(the_list) <= 1:
        # print('Base Case: ', the_list)
        return the_list
    
    pivot = the_list[0]
    less_list = []
    greater_list = []
    # partition process
    for i in range(1, len(the_list)):
        if the_list[i] < pivot:
            less_list.append(the_list[i])
        else:
            greater_list.append(the_list[i])
    # print(pivot, less_list, greater_list)
    
    less_list = quick_sort(less_list)
    greater_list = quick_sort(greater_list)
    
    return less_list + [pivot] + greater_list

print('\n\n')
test_qs_list = [random.randint(1, 100) for _ in range(20)]
print(test_qs_list)
qs_sorted = quick_sort(test_qs_list)
print(qs_sorted)
if qs_sorted == sorted(qs_sorted):
    print('It worked')
else:
    print('Error somewhere')


def time_test(sorting_algorithm, list_size):
    new_list = [random.randint(0, 100) for _ in range(list_size)]
    start_time = time.process_time()
    sorting_algorithm(new_list)
    end_time = time.process_time()
    
    print(f'That took {end_time - start_time} to sort using {sorting_algorithm.__name__} on a list of size {list_size}')


for ls in [10, 100, 1000, 10000, 100000, 1000000, 100000000]:
    # time_test(insertion_sort, ls)
    # time_test(selection_sort, ls)
    time_test(merge_sort, ls)


"""
    Because merge sort is guaranteed to split the list in half every time
    we know exactly (+/- 1) how many recursion levels it's going to run.
    
    100 => 50 => 25 => 13 => 7 => 3 => 1 Base Case
    
    100 / 2 ** 7 = 100 / 128 ~= 1
    
    250 / 2 ** s ~= 1
    250 ~= 2 ^ s
    lg(250) ~= lg(2^s) = s * lg(2) = s * 1 = s
    
    s = 7.96 blah blah blah
    s = 8 (round it up)
    
    lg(n) = ln(n) / ln(2) = log(n) / log(2)
    
    log_a(x) = log_b(x) / log_b(a)
"""


"""
    Time complexity / asymptotic analysis
    
    1 + 2 + 3 + 4 + 5 + ... + (n - 1) + n = n(n + 1) / 2
    1 + 2       + 3       + 4       + 5       + ... n / 2
    n + (n - 1) + (n - 2) + (n - 3) + (n - 4) + ... n / 2 + 1
    (n + 1) + (n + 1) + (n + 1) + (n + 1) + ... + (n + 1) how many? n/2
    n/2 * (n + 1)
    
    1 + 2 + 3 + 4  ..+ 5 + 6 + 7 + 8
    8 + 7 + 6 + 5
    9 + 9 + 9 + 9 (9 * 4) = 9 * 8/2
    Gauss Sum
    
    Bubble Sort, Insertion Sort and Selection Sort all take about
    n(n + 1)/2 ~ n^2/2 steps
    
    (100,000)^2 / 2 steps = 5 billion steps ~ 11 minutes close to done
    (10,000)^2 / 2 steps = 6.6875 seconds
    7.5 million steps / second
    
    think super simple
    
    When I say that Bubble, Selection, Insertion are all quadratic sorts
        their runtimes are approximately n^2 steps
"""