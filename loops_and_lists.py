"""
    The ability to have our program repeat things - iteration
        iteration = concept that there is a next thing and we'll keep doing those things
            until we reach the "end"
    
    Two types of loops in python:
        for loop
            for each loop - iterates through elements
            for-i loop - iterates through indices
        while loop
        
    What is the purpose of loops?
        allow us to repeat a piece of code (functionality) as many times as we need
    
    keyword is actually for
    for [variable name] in range(n): <-- remember the colon
"""

# starts at 0 and counts up to n - 1 whatever n is inside the range(n)
for i in range(5):
    print("counting", i)

# since lists and for loops are built to work together, the first index in a list is 0
# therefore the range will produce 0 as the first number.

n = int(input('Tell me some number: '))
# goal: add up all the numbers between 1 and n.
if False:
    total = 0
    # sometimes you'll have to modify the value inside of range
    for i in range(n + 1):
        # total = total + i
        total += i
        
    print('The total is', total)
    
    """
        A list is a collection of elements of basically any type
    """
    
    # use square brackets to make a list
    #             0   1      2       3      4    5
    first_list = [3, 1.2, 'types', False, True, 17]
    """
        To access an element in a list, you use the square brackets after the list name
    """
    print(first_list[2], first_list[0], first_list[5])
    
    first_list[2] = 'happy'
    first_list[3] = 'sad'
    
    
    
    """
        How do we know that we're at the end of the list?
            len(new_list)
    """
    new_list = [1, 7, 2, 9, 3, 7, 12]
    new_total = 0
    print(len(new_list), '\n\n')
    
    for index in range(len(new_list)):
        print(index, new_list[index])
        new_total += new_list[index]
    
    print('The total of the list was', new_total, new_total / len(new_list))
    
    empty_list = []      # set builder notation
    also_empty = list()  # class constructor
    print(len(empty_list), len(also_empty))
    my_list = [1, 2, 3, 4, 5]
    if len(my_list) > 0:
        print('Ok now we can take averages, divide, do something with the elements')
    else:
        print('This list is empty, don\'t do anything here.  ')
    
    my_string = 'Hello, this is a story about robots. Of course it is.'
    
    # len also works on strings.
    # does the index operator [] also work? yes
    
    for j in range(len(my_string)):
        print(j, my_string[j])
    
    """
        Goal is to test whether or not two letters next to each other are the same (or not).
        01234
        sheep
        nuance
    """
    the_word = input('Tell me a word to check: ')
    
    found_match = False
    for current in range(len(the_word) - 1):
        if the_word[current] == the_word[current + 1]:
            found_match = True
    
    print(f'Does the word have a match? {found_match}')
    
    
    test_num = int(input('Enter a number to test for primality: '))
    """
        A prime number is an whole number that is not divisible by anything except 1 and itself
            * only checking between 1 and itself
            1 not prime ==> by definition
    """
    is_prime = True
    if test_num > 1:
        for i in range(2, test_num):
            if test_num % i == 0:
                is_prime = False
        print(f'{test_num} is prime? {is_prime}')
    else:
        print('It isn\'t prime.')

"""
    Full definition of range:
        range(start = 0, stop (whatever we put in), step = 1)
        
        range(stop) = from 0 up to (not inclusive of) stop
        range(start, stop)
        range(start, stop, step)
            step = increment
"""

for i in range(3, 17, 2):
    print(i)
print('\n---------------------------------\n')
for i in range(10, -1, -1):
    print(i)

print('Starting impossible range: ')
for index in range(3, 100, -2):
    print(i)
# the loop does not run
print('Starting next impossible range: ')
for index in range(100, -100, 5):
    print(index)
    
print('Done with impossible ranges')
"""
Do not run:
for i in range(1, 1000000000000000000000000000000000000000):
    if i % 1000000 == 0:
        # slowest operation is print
        print(i)
"""

# import math
# print(math.log(1000000000000000000000000000000000000000, 10))

