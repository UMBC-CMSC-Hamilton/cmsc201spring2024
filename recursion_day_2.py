"""
    Binary problem = hint : you don't have to know anything about binary

    Recursion = when a function calls itself
        function doesn't end up in an "infinite loop"
        function(5) -> function(5) -> function(5) -> function(5) -> "forever"
    
    What python has done is implemented a RecursionError
        prevents more than a depth of 990-1000 recursions
        
        In this class that "should never happen"
    
    Recursions are terminated with base cases
    Base Cases - any part of the function that returns before you
        get to a recursion. Without base cases you'd also end up
        in infinite recursion.
    Recursive Cases - any part of the function that has a recursive call
    

    Here's an example of a's and b's type of problem:
        what if we want to list ALL combinations of a's and b's of a
        given length
        
    len = 1
    a   b
    
    len = 2
    aa ab ba bb [order matters so ab != ba]
    
    len = 3
    aaa aab aba abb
    baa bab bba bbb
    
    len = 4
    aaaa aaab aaba aabb abaa abab abba abbb
    baaa baab baba babb bbaa bbab bbba bbbb
    
    In order to get the strings of length n, you calculate the strings
    of length n - 1 and then add either a or b [to the start or the end]
"""


def as_and_bs(n, current=''):
    if n == 0:
        print(current)
        return  # why do we need this?
    
    as_and_bs(n - 1, current + 'a')
    as_and_bs(n - 1, current + 'b')


"""
as_and_bs(4, '')
    as_and_bs(3, 'a')
        as_and_bs(2, 'aa')
            as_and_bs(1, 'aaa')
                as_and_bs(0, 'aaaa') -> print aaaa
                as_and_bs(0, 'aaab') -> print aaab
            as_and_bs(1, 'aab')
                as_and_bs(0, 'aaba') -> print aaba
                as_and_bs(0, 'aabb') -> print aabb
        as_and_bs(2, 'ab')
            as_and_bs(1, 'aba')
                as_and_bs(0, 'abaa') -> print abaa
                as_and_bs(0, 'abab') -> print abab
            as_and_bs(1, 'abb')
                as_and_bs(0, 'abba') -> print abba
                as_and_bs(0, 'abbb') -> print abbb
    as_and_bs(3, 'b')
        as_and_bs(2, 'ba')
            as_and_bs(1, 'baa')
                as_and_bs(0, 'baaa') -> print baaa
                as_and_bs(0, 'baab') -> print baab
            as_and_bs(1, 'bab')
                as_and_bs(0, 'baba') -> print baba
                as_and_bs(0, 'babb') -> print babb
        as_and_bs(2, 'bb')
            as_and_bs(1, 'bba')
                as_and_bs(0, 'bbaa') -> print bbaa
                as_and_bs(0, 'bbab') -> print bbab
            as_and_bs(1, 'bbb')
                as_and_bs(0, 'bbba') -> print bbba
                as_and_bs(0, 'bbbb') -> print bbbb
    

"""

# what is the total number of combinations is 2 ** n
#
as_and_bs(4, '')

"""
    What if you want to print out where there are always more a's than b's in
    the sequence
    ba would not get printed because there's already a b before an a
    ab could get printed
    aab could work
    abb would not because there's more b's then a's in the first three
"""


def more_as_than_bs(n, num_as, current):
    num_bs = len(current) - num_as
    if n == 0:
        if num_as >= num_bs:
            print(current)
        return
    
    if num_as >= num_bs:
        more_as_than_bs(n - 1, num_as + 1, current + 'a')
        more_as_than_bs(n - 1, num_as, current + 'b')


"""
    You can count up the difference between a's and b's
"""

more_as_than_bs(5, 0, '')


def more_as_than_bs_diff(n, diff_as=0, current=''):
    if n == 0:
        if diff_as >= 0:
            print(current)
        return
    
    if diff_as >= 0:
        more_as_than_bs(n - 1, diff_as + 1, current + 'a')
        more_as_than_bs(n - 1, diff_as - 1, current + 'b')


more_as_than_bs_diff(6)

"""
    Maybe the first letter is an x, if it is add one to the count
    if it's not don't add 1
        after that ask how many x's there are in the rest of the string
        trust the recursion to produce the right answer
"""
def count_xs(a_string):
    print('Starting', a_string)
    if not a_string:
        print('Empty String, returning 0')
        return 0
    # think about slices
    if a_string[0].lower() == 'x':
        #          this should return the number of x's doesn't include the
        #              first letter. Slice will remove a_string[0]
        # We return 1 + result because we found an x and want to increment
        print(f'Found x calling on {a_string[1:]}')
        count = 1 + count_xs(a_string[1:])
        print(f'Found x, returning {count}, {a_string}')
        # passing the answer back up to the previous level of the recursion
        return count
    else:
        # we don't add 1 because it's not an x, and we call it on the
        # remainder of the string to count the rest of the x's.
        print(f'Not found x calling on {a_string[1:]}')
        count = count_xs(a_string[1:])
        print(f'Not found x, returning {count}, {a_string}')
        return count
    
"""
    You might end up with a NoneType Error
    TypeError - plus is unsupported between int and NoneType
    
    Python Specific - at the end of a function that doesn't return anything
        it returns None [special object/keyword]
"""


in_string = input('Enter string: ')
while in_string != 'quit':
    print(count_xs(in_string))
    in_string = input('Enter string: ')


"""
    Matching Parentheses
        (a + b * (c - d))
        )) a - (( b = invalid
        ))) a = invalid
        () () (()) (()()(())) = valid
        ((()( more opens than closes
        )(( = more closes than opens
        )( = wrong order
    calculate the difference between opens and closes
        steal that from the a's and b's examples
        if the thing is an open, then we'll add one to the difference
        if the thing is a close we'll subtract one
    difference must always be non-negative >= 0
    at the end we expect it to be 0 exactly
    () () () = ok
    ( () () () = not ok there's an extra open that doesn't get closed
"""

def matching_parens(a_string, difference):
    if not a_string:  # if len(a_string) == 0: or if a_string == "":
        return difference
    if difference < 0:
        return -1
    
    if a_string[0] == '(':
        return matching_parens(a_string[1:], difference + 1)
    elif a_string[0] == ')':
        return matching_parens(a_string[1:], difference - 1)
    else:
        return matching_parens(a_string[1:], difference)


def non_rec_parens(a_string):
    diff = 0
    for x in a_string:
        if x == "(":
            diff += 1
        elif x == ")":
            diff -= 1
        else:
            diff += 0 # does nothing but it's like the recursion
            
        if diff < 0:
            return -1
    
    return diff

in_string = input('Enter string: ')
while in_string != 'quit':
    print(matching_parens(in_string, 0))
    in_string = input('Enter string: ')

"""
    doesn't work... almost works but not quite
    identifies )))((( as valid
"""
def matching_parens_alt(a_string):
    if not a_string:
        return 0
    
    if a_string[0] == "(":
        count = matching_parens_alt(a_string[1:])
        if count >= 0:
            return 1 + count
        else:
            return -1
    elif a_string[0] == ")":
        count = matching_parens_alt(a_string[1:])
        return (-1) + count
    else:
        return 0 + matching_parens_alt(a_string[1:])

"""
    )))((( -> valid
"""

in_string = input('Enter string: ')
while in_string != 'quit':
    print(matching_parens_alt(in_string))
    in_string = input('Enter string: ')
