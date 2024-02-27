"""
    First midterm next thursday, in class
    
    I'll release a practice test
    
    Functions - What are they?
        A function is a block of code that we can call whenever we want
        You don't have to run it just once, or you can run it zero times
        
        You can break up the pieces of code that you write into little
            functional blocks.  Each block [function] should do one thing.
            
        You can test this function and see that it does all the things you expect
            the alternative is basically copy-paste
            here's the problem:
                if you find a bug in one of the versions you have to then go back
                    and fix ALL of the copies
            Advantage of a function is that it only has the piece of code once
                you call it seven times.

    Syntax:
    
    def function_name(x, the_int, y):
        all code in the function
        must be tabbed in
        to exit the function
        you stop tabbing
"""


def find_average(the_list):
    """
    :param the_list:
    :return: the average of the list, or zero if empty?
    """
    # this is an edge case
    if not the_list:  # a list evaluates to false iff it is empty
        return 0
    #  a return allows us to give a value back to the calling position
    # as soon as you hit a return statement, the function ends
    
    total = 0
    for x in the_list:  # for each loop gives us elements
        total += x
    
    return total / len(the_list)


value = find_average([])
print(value)

another = find_average([3, 7, 29, 3, 2, 19, 77, 15])
print(another)

a_string = input('Tell me a story: ')
print(a_string)


def is_prime(n):
    """
    :param n: an integer we're going to check
    :return: True if prime, False if not
    """
    # edge cases
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            # once we get to this return statement the function ends
            # be careful if you want the loop to finish don't do this.
            return False
    # we return true if the loop doesn't exit at some point
    # we've checked from 2 up to n - 1 and none divide
    return True


x = int(input('Tell me a number to test (0 to exit): '))
while x != 0:
    print(x, is_prime(x))
    x = int(input('Tell me a number to test (0 to exit): '))


def count_the_as(a_string):
    count = 0
    for i in range(len(a_string)):
        # no return statement in here, reason is we want this to finish
        # every time.  Never exit early.
        if a_string[i].lower() == 'a':
            count += 1
    return count


def count_the_sevens(a_list):
    count = 0
    for i in range(len(a_list)):
        # no return statement in here, reason is we want this to finish
        # every time.  Never exit early.
        if a_list[i] == 7:
            count += 1
    return count


"""
   Return doesn't print, it just gives us the value back
   
   you don't have to print it, you can save it into a variable
   or you can just let the value go.
"""

print(count_the_as("aardvark"))
print(count_the_as("ascii"))
print(count_the_as("robot chicken"))
print(count_the_as("abstain salamander banana"))

"""
    Does a function have to return something?
        no... but... python actually does secretly.
"""


def random_garbage(x, y):
    print(x + y, x - y)
    # secret return None


test_var = random_garbage(5, 2)
print(test_var)

# print returns None / not returning
x = print("hello")
print(x)


def test_thing():
    for i in range(1, 10):
        print(i)
        # if you're going to put a return inside of any loop
        # make sure it's probably in an if statement
        return i


test_thing()

"""
    Let's talk a little bit about parameters
        
        Concept Scope
"""


def three_numbers(x, y, z):
    # x, y, z are the parameters
    print(x ** 2 - y * z)
    x = x ** 2 - y * z
    y = 4 * z
    z = y + 2
    print(x, y, z)


three_numbers(14, 5, 6)
# TypeError if the number of argument is wrong
# three_numbers(6, 7)

a = 17
b = 12
c = 4
three_numbers(a, b, c)
three_numbers(c, a, b)
three_numbers(b, 3, 16)
"""
    if it's a value, 3 or 16 then we call those literals
"""
x = 3
y = 2
z = 1

three_numbers(x, y, z)
print(x, y, z)
"""
    Scope:
        Variables can live a shorter time than the entire program
        They only are visible inside of the function that creates them
        
    Outside of functions:
        Global scope - these variables have indefinite lifetime (live
            as long as the program does)
            accessible anywhere.
        Local scope - exists only as long as the function does
            variables are basically only 'accessible' or visible from
            within the function
"""

count = 14
print("number of as", count_the_as("hello asdf"))
print("number of sevens", count_the_sevens([7, 7, 6, 5, 4, 7, 8]))
print("global count", count)

"""
    Mutability - determines how things are passed into functions
        basic data types - primitive types / primitives
        "immutable" (int, bool, string, float)
            datetime, timedelta
        mutable - it can be changed.
            it can be changed inside of a function if you pass it as a
            parameter
            lists, dicts, classes [most of them]
            
            
        mutable objects are "passed by reference"
            a reference is a renaming of the original object
            multiple variables accessing the same object
        if you pass an IMMUTABLE object [int bool float string]
            this passes by "value"
            the variable in the function [the parameter] is a copy
            the original is left unchanged
            
            If you ever need to change a group of numbers/strings
            pass it as a list and then modify each element
            
"""

def change_avar(a_var, the_val):
    a_var = the_val
    print(a_var)

def add_random_to_list(the_list):
    the_list.append(7)
    the_list.append(3)
    the_list.append(19)
    print(the_list)

my_list = [4, 5, 6, 7]
add_random_to_list(my_list)
print(my_list)

a_var = 14
change_avar(a_var, 3)
print(a_var)