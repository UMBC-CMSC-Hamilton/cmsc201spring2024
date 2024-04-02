"""
Recursion - what is it?

    Any kind of process that calls itself
    [process = function]
    
    function that calls itself with a different argument
        eventually that function will stop
        
    Base Case - there needs to be a way to stop, the base case detects this
        and stops the function from running.
    
        think about it like a while condition, when the condition becomes
            false you want the loop to stop.
        [there can be multiple]
    Recursive Case - any case that calls the original function
        [there can be multiple]

    What if we want to calculate
        1 + 2 + 3 + 4 + 5 + ... + n (argument that we pass in to the function)
        Right answer: a for loop
"""
"""
total = 0
for i in range(1, n + 1):
    total += i
"""

def recursive_gauss(n):
    print('Entering', n)
    # base case
    if n == 0:
        print('Base Case')
        return 0
    # recursive case
    input(">>")
    temp = recursive_gauss(n - 1) + n
    print("Leaving", n, 'The current result is: ', temp)
    input(">>")
    return temp


# n = int(input('What do you want to add up to? '))
# print(recursive_gauss(n))

"""
    rg(5) = rg(4) + 5 = 10 + 5 = 15
    rg(4) = rg(3) + 4 = 6 + 4 = 10
    rg(3) = rg(2) + 3 = 3 + 3 = 6
    rg(2) = rg(1) + 2 = 1 + 2 = 3
    rg(1) = rg(0) + 1 = 0 + 1 = 1
    rg(0) = 0
"""

n = int(input('How far do you want to count down?'))

def countdown(n):
    if n == 0:
        print('Blastoff')
        return
    print(f"T = {n}")
    countdown(n - 1)

countdown(n)
"""
countdown(10) calls countdown(9)
countdown(9) calls countdown(8)
countdown(8) calls countdown(7)
...
countdown(1) calls countdown(0)
countdown(0) says blastoff

Each copy of the recursion gets its own set of local variables.
"""

"""
palindromes

racecar
tacocat
gnudung
amanaplanacanalpanama
"""

def recpal(a_string):
    """
    :param a_string: a string to test if it's a palindrome
    :return: True or False, depending
    
        If it is a palindrome, i know that the first letter and the last letter
        are the same.
        
        We'll test that, if it's true then maybe it is
        If it's not true... return False immediately.
    """
    if len(a_string) == 0:  # not a_string
        return True
        
    if a_string[0] != a_string[-1]: # a_string[len(a_string) - 1]
        return False
    # a_string[1:-1] takes off the first letter and goes up to but doesn't
    # include the last letter
    print(a_string[1:-1])
    return recpal(a_string[1:-1])


test_string = input('What do you want to check for palindromeness? ')
while test_string != 'quit':
    test_string = ''.join(test_string.split())
    print(recpal(test_string))
    test_string = input('What do you want to check for palindromeness? ')


"""
    factorial recursively
    
    Is it true that ??? :
    n! = n * [(n - 1)!]
    factorial(n) = n * factorial(n - 1)
    
    n! = n * (n - 1) * (n - 2) * (n - 3) ... * 1
    0! = defined = 1
"""


def factorial(n):
    if n == 0:
        return 1
    # you have to believe that the answer to (n - 1)! will come out of that function
    return n * factorial(n - 1)


n = int(input('What factorial do you want? '))
while n >= 0:
    print(factorial(n))
    n = int(input('What factorial do you want? '))


"""
    fibonacci numbers
    0  1  2  3  4  5  6    7   8  9   10   11
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
    add the previous two fibonacci's to get the next one

    f_n = f_{n -1} + f_{n - 2}
    fib(n) = fib(n - 1) + fib(n - 2)
"""

def fib(n):
    print('Now calling', n)
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def actual_fib(n):
    current = 0
    prev = 1
    prev_prev = 1
    for i in range(2, n + 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    
    return current


def actual_fib_list(n):
    fib_list = [1, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    return fib_list[-1]


n = int(input('What fibonacci number do you want? '))
while n >= 0:
    print(actual_fib_list(n))
    n = int(input('What fibonacci number do you want? '))

