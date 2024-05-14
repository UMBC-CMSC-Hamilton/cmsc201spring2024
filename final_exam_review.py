"""
    For this section 20, you will go to PHYS 101

    Friday May 17th 6-8pm
        Common Final Schedule NOT regular schedule

1) port_8080
    3_blind starts with a number
    rest have illegal symbols
2) a - 1
3) b - mutable lists passed by reference
4) b - scope
5) a
    dict.get(thing) ==> not in the dict returns None
    dict.get(thing, val) ==> not in dict, returns val
    dict.get prevents KeyErrors
    dict[thing] causes keyErrors when it's not in the dictionary
6) b - def
7) b - need a base case (any case that ends in a return or end of function without a recursive call)
8) d list must be sorted otherwise middle element doesn't really mean anything
9) c) - float, int, bool, string are immutable
10) b - you can modify elements in a for-i loop
11) a - skipped loop
12) a - test your code

bubble sort
[51, 24, 33, 71, 89, 31, 12, 5, 19, 1]
1st iteration - [24, 33, 51, 71, 31, 12, 5, 19, 1, 89]
2nd iteration - [24, 33, 51, 31, 12, 5, 19, 1, 71, 89]
3rd iteration - [24, 33, 31, 12, 5, 19, 1, 51, 71, 89]

selection sort - picks the min and puts it into the right place and swaps
[5,7,12,31,24,1,17,3,9,2]
1st iteration - [1,7,12,31,24,5,17,3,9,2]
2nd iteration - [1,2,12,31,24,5,17,3,9,7]
3rd iteration - [1,2,3,31,24,5,17,12,9,7]

15) Write a boolean expression which is True if and only if a
list sandwich contains the strings
'ham', 'cheese', and 'mayo', but not 'tuna'.

'ham' in sandwich and 'cheese' in sandwich and 'mayo' in sandwich
    and 'tuna' not in sandwich

16) Write a boolean expression which is True if and only if a
variable x is at least two times the value of a variable y
or 'happy' is in the string emotion but not both <--

(a and not b) or (not a and b)

((x >= 2 * y) and 'happy' not in emotion) or
    ('happy' in emotion and not(x >= 2 * y))
                            (x < 2 * y)

17. Explain why a sorted list must be used in binary search.
    Use examples to justify your answer.
    
    A sorted list is necessary because when you look at the middle element
        you need to determine whether the list elements are greater or less
        than it.
                  |
         less     v  greater
        [2, 3, 4, 9, 17, 25, 46]
           ???      v   ???
        [14, 25, 3, 9, 71, 4, 36]

18. Describe a problem where you should use recursion rather than loops and explain why that
problem is best solved with recursion.
    a's and b's problems "need" recursion because you have to branch both to the
    a case and the b case for every string.
    aab + a
    aab + b
    
    Pathfinding, you have a bunch of different ways to go, you need to check
        them all, and then you need to check the paths leading from them too
        Because you need to constantly check all the destinations from any source
        you need recursion.
"""


def search_list(a_list, element):
    print('searching for', element)
    for x in a_list:
        if x == element:
            print(element, 'found')
            return True
    print(element, 'not found')
    return False


def create_list(start, stop, step):
    new_list = []
    for i in range(start, stop, step):
        new_list.append(i)
    return new_list


a_list = create_list(3, 100, 2)  # [3, 5, 7, 9, ... 99]
b_list = create_list(0, 51, 5)   # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
search_list(a_list, 77)
search_list(a_list, 22)
search_list(b_list, 50)
search_list(b_list, 24)

"""
Searching for 77
77 found
Searching for 22
22 not found
Searching for 50
50 found
Searching for 24
24 not found
"""

"""
work:
co(3)
       a  b
z = cm(6, 3)
    x = ci(6, 3, 0)
    x = 0
    return 2 * x + 6
z = 6

w = cm(3, 6)
    x = ci(3, 6, 9)
    x = 18
    return 2 * 18 + 3
            39
print('outer', a, z, w)

result/answer:

inner 6 3 0
middle 6 3 0 // no such thing as y
inner 3 6 9
middle 3 6 18
outer 3 0 39
"""
def double_string(the_string):
    print(the_string + the_string)
    return the_string + the_string

my_string = 'stringy'
double_string(my_string)
print(my_string)
"""
stringystringy
stringy  // value didn't get saved and mutability
"""

big_string = 'helloeveryone'
print(big_string[2:8])  # lloeve
print(big_string[0:2])  # he
print(big_string[6:])   # veryone
print(big_string[6: 200000]) # not an error slices are forgiving
# veryone

value = 1
while value < 50:
    value += 3
    value *= 2
    print(value)
    
"""
8
22
50
"""

my_list = []
row_list = []
for i in range(4):  # row_list = [1, 2, 3, 4]
    row_list.append(i + 1)
my_list = [row_list , row_list , row_list]  # references to row_list itself
my_list[2][2] = 7 # [1, 2, 7, 4]
for row in my_list:
    print(row)
"""
[1, 2, 7, 4]
[1, 2, 7, 4]
[1, 2, 7, 4]
"""
"""
0xFE327D
1111 1110 0011 0010 0111 1101
"""


def abcs(n, current):
    if n == 0:
        print(current)
        return
    
    abcs(n - 1, current + 'a')
    abcs(n - 1, current + 'b')
    abcs(n - 1, current + 'c')


""" hint """
def countdown(n):
    if n == 0:
        print('Blastoff')
    else:
        countdown(n - 1)
        print(n)

"""
users = {
’eric8’: {’credits’: 3, cart: [’typewriter’], ’last-access’: 27},
’jeanlucp’: {’credits’: 7, cart: [’flute’], ’last-access’: 55},
’rikerwt’: {’credits’: 100, cart: [’trombone’], ’last-access’: 31}
}
When you receive this dictionary you should return [’jeanlucp’, ’rikerwt’].
"""

def find_inactive_users(users):
    log_out = []
    for username in users:  # user is the key not the value
        if users[username]['last-access'] >= 30:
            log_out.append(username)
    return log_out


countdown(10)