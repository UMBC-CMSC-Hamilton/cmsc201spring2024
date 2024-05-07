"""
    Asymptotic Analysis - Complexity Theory / Computational Complexity
    
    Measure how many steps our code takes to run based on an input size.
    
    The number of steps can grow quickly, if it does then eventually
        you won't be able to calculate the result within a human lifespan.
    
    Talk about it in terms of big-O
    
    What is big-O?
    
        f(n) is O(g(n)) when there are constants C and N0 so that
        f(n) <= C g(n) for n >= N0
        
        5n^2 is O(n^2)
        pick C = 5
        
        What is the purpose of the constant C?
            When you run an algorithm on a computer it depends on many things:
                CPU speed
                 - it could? GPU speed
                RAM speed
                
            Algorithm may be implemented slightly more efficiently or slightly less
        
        All about the growth of the time as input size goes up.
        
"""

"""
    For loops become summations
    
          Σ         Σ       1
    (from 1 to n)  (from j = i to n)

    <=      Σ         Σ       1
    (from 1 to n)  (from j = i to n)

         Σ    1 =   1 + 1 + 1 + 1 ... + 1 = (n - i + 1)
    (from j = i to n)

        Σ   (n - i + 1) =
    (from 1 to n)
    
    
        Σ (n + 1) - Σ i = n(n + 1) - n(n + 1)/2 = n(n + 1)/2
        both sums from i = 1 to n
    
        this function is O(n^2)
        (n^2 + n) / 2 < n^2
    
    think about it this way
         Σ    1  =      1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10 - 2 + 1
         from 2 to 10 (inclusive)

    1 + ... + (i - 1) + i + (i + 1) + (i + 2) + (i + 3) + ... + n
    - (1 + ... + (i - 1))
    n(n + 1)/2 - i(i - 1)/2
    
    1 + 2 + 3 + ... + n = n(n + 1)/2

    What that means to us is that as the input size increases the runtime
        goes up by a factor of n^2.
        
        it takes you 3 seconds to run selection sort on a size of 1000
        how long does it take to run on a size of 10,000?
        
        time = C * (10,000)^2 / (C * (1000)^2)) * 0.046875 sec
        good news is that the C's cancel.
            = 10000^2 / 1000^3 * 0.046875 sec
            = (10000/1000)^2 * 0.046875 sec = 4.7 seconds [estimate]
            
    Best Case = Worst Case = Average Case = All Cases O(n^2)
"""
def selection_sort(the_list):
    for i in range(len(the_list)):
        min_index = i
        for j in range(i, len(the_list)):
            if the_list[j] < the_list[min_index]:
                min_index = j
        if i != min_index:
            temp = the_list[min_index]
            the_list[min_index] = the_list[i]
            the_list[i] = temp
    
    return the_list

"""
    we set len(the_list) = n
    
    there's actually going to be two different runtimes
    
    One is the best, = Ω(--) = Ω(1) = Constant time number of operations
    one is the worst = O(--) = O(n) = linear time worst case
"""
def linear_search(the_list, the_thing):
    for x in the_list:
        if x == the_thing:
            return True
        
    return False

"""
    What about binary search?
        how does that work?
        
    
"""


def binary_search(the_list, the_element):
    if not the_list:
        return False
    elif len(the_list) == 1:
        return the_list[0] == the_element
    
    middle_index = len(the_list) // 2
    if the_element == the_list[middle_index]:
        return True
    elif the_element < the_list[middle_index]:
        return binary_search(the_list[0:middle_index], the_element)
    else:
        return binary_search(the_list[middle_index + 1:], the_element)

"""
Every time we go through this function we divide the list size in half.

Time(n) = Time(n/2) + 1
n ==> n/2 ==> n / 4 ==> n / 8 ==> n / 16 ==> n / 32
We stop this process when n / 2^k = 1 ==> multiply up by 2^k
k = # steps we have to do

n = 2^k
log_2(n) = lg(n) = lg(2^k) = k * lg(2) = k
lg(n) are usually transcendental horrible things
technically you'd have to round up or something

best case is when you you find the element without searching too many times
                                                            Ω(1)
if it has to go the whole way down, it'll take lg(n) steps =
                                                            O(lg(n))
"""

"""
    MergeSort
        cuts the list in exactly half
        
        merge process on the way up
        
"""


def merge(first_list, second_list):
    """
        Let's say that the first list is size N and the second is size M
        how many steps does this thing go?
            O(N + M) runtime
            n = N + M
            linear time O(n)
    """
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

"""
    If merge is linear time then what is this?
    [ ------------ n ------------]
    [n / 2 ------]  [n / 2 ------]
    [-n/4-] [-n/4-] [-n/4-] [-n/4-]
    so on...
   num steps is lg(n)
   cost per step is O(n)
   total cost is O(n) * lg(n) = O(n lg(n))
"""
def merge_sort(a_list):
    # print(a_list)
    if len(a_list) <= 1:
        return a_list
    middle = len(a_list) // 2
    left_side = merge_sort(a_list[0: middle])
    right_side = merge_sort(a_list[middle: len(a_list)])
    return merge(left_side, right_side)


def quick_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    
    pivot = the_list[0]
    less_list = []
    greater_list = []
    for i in range(1, len(the_list)):  # O(n) = linear time
        if the_list[i] < pivot:
            less_list.append(the_list[i])
        else:
            greater_list.append(the_list[i])
    less_list = quick_sort(less_list)
    greater_list = quick_sort(greater_list)
    
    return less_list + [pivot] + greater_list

"""

    QuickSort what does it do?
    
        partitions the list => uses a pivot element
            puts anything less in the less list and anything greater
            in the greater list [also equal]
            O(n) time, that's fine.
        
    Problem:
        if the lists divide evenly then this looks like merge sort
            O(n lg(n))
            
        What if it doesn't?
        big_list -> [0] pivot [all the rest]
        all the rest -> [0] pivot [all the rest2]
        
        [1, 2, 3, 4, 5, 6]
        pivot = 1, [] [2, 3, 4, 5, 6]
        pivot = 2, [] [3, 4, 5, 6]
        pivot = 3, [] [4, 5, 6]
        pivot = 4, [] [5, 6]
        pivot = 5, [] [6]
        
        if the number of steps is like n - 1 (which it is)
            then (n - 1) * O(n) = O(n^2)
"""

"""
    if you have an nlg(n) algorithm then what's happening?
    
    5.3 sec on 10^6 elements
    what about 10^7 elements [10 million]
    
    10^7 * lg(10^7) / (10^6 * lg(10^6)) * 5.3 sec
    10 * 7 lg(10) / [6 * lg(10)] * 5.3
    7/6 * 10 * 5.3 sec = 61.8 seconds
    Good news = 65.78 seconds.
    
    10^8 * lg(10^8) / (10^6 * lg(10^6)) * 5.3 sec
    100 * 8/6 * 5.3 sec = 706 sec for 100 million
    
    Quick Sort its best case is Ω(n lg(n))
                   worst case is O(n^2)
    If you remember there is a way to fix this.
        pick pivot as the median then you can avoid any problems.
        when you get to 441 we'll talk about it maybe...
        
"""

def matrix_multiply(A, B, n):
    C = [[0 for x in range(n)] for _ in range(n)]
    for i in range(n):         # runs n times with j loop inside n * (n^2) = n^3 ops
        for j in range(n):     # runs n times with the k loop inside n * n operations
            for k in range(n): # runs n times
                C[i][j] = A[i][k] * B[k][j]
    return C
"""
This function is Θ(n^3) = we use theta when the best case = worst case
Also can use big-O
"""

def is_prime(num):  #runs O(sqrt(n))
    for i in range(2, int(num ** (1/2)) + 1):  #runs about sqrt(n) times
        if num % i == 0:
            return False
        
    return True

"""
But if you know just a little about numbers, if the thing has a factor
num = x * y
one of them or both has to be <= sqrt(num) why is that?
    if both factors are greater than the square root:
        x * y > sqrt(n) * sqrt(n) contradiction impossible
"""