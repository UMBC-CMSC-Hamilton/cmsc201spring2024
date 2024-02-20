"""
    Let's talk a bit more about lists
"""
#           0  1  2  3  4  5  6
the_list = [1, 5, 8, 9, 2, 3, 4]
word_list = ['up', 'down', 'sideways', 'backwards']

# legal in python but avoid it if you can
mixed_list = [4, 'up', 2, 'down', 3, 'left', 1, 'right']

# notice that the code and the command now have the same index
code_entered = [4, 2, 3, 1]
command_list = ['up', 'down', 'left', 'right']

total = 0
for i in range(len(mixed_list)):
    if i % 2 == 0:
        total += mixed_list[i]

print(total)
#           0   1    2     3    4    5    6    7
#           index is how far you have to go from the start, offset
my_list = ['a', 'z', 'q', 't', 'r', 'p', 'n', 'v']
# if I use the word array -> list

# if you plug in an index that is out of bounds, you get
# IndexError, know that an error will occur if you do this
index = int(input('Tell me the index: '))
# lots of code
# 0 is included, the length of the list is not
if 0 <= index < len(my_list):
    print(my_list[index])
else:
    print('Bad human.')

"""
    How do we add elements into a list?
        append method
"""

# sentinel value is a value where we understand it's not from
# user input, it's a signal to us to tell us something
sentinel = -1
number = int(input('Tell me a positive number, or -1 to exit'))

if number == sentinel:
    print('We know we should exit')
else:
    print('We do whatever the user wants')

"""
    How do we use the append method?
        takes the list and adds a new last element
"""

new_list = []
new_list.append(5)
new_list.append(17)
new_list.append(21)
new_list.append(72)
new_list.append(55)
print(new_list)
if False:
    another_list = []
    for i in range(10):
        the_number = int(input(f'Tell me a number {i + 1}: '))
        another_list.append(the_number)
    
    print(another_list)

movie_list = []
num_movies = int(input('Tell me how many you want to enter: '))

for i in range(num_movies):
    movie = input('Tell me a good movie or at least a movie: ')
    movie_list.append(movie)

print(movie_list)
# instead of producing indices it's going to produce elements
#  "for-each" loop when you say for each what you mean is that
# elements are being produced not indices.
for movie in movie_list:
    print('A movie is', movie)

# not a for-i loop, this is a for-each loop.
for i in [5, 4, 3, 9, 8, 7]:
    print(i)

# for i loop - range(len(something)) - produces indices.
for index in range(len(movie_list)):
    print(index, movie_list[index])

"""
    In a for each loop, you can't actually modify
        the underlying list
    For i loops can modify the list
"""
change_me = [4, 5, 2, 8, 9, 1, 3]
"""
    in a for each loop, the variable is a kind of copy of the original
        you can modify the copy but you aren't changing the original
"""
if False:
    for element in change_me:
        new_num = int(input(f'Do you want to change the number {element}? -1 for no'))
        if new_num != -1:
            element = new_num
            print(element)
    
    """
        For i construction can be used to change elements
            in a list like this.
    """
    for i in range(len(change_me)):
        new_num = int(input(f'Do you want to change the number {change_me[i]}? -1 for no'))
        if new_num != -1:
            change_me[i] = new_num
            print(change_me[i])
    
    """
        find the maximum using a for loop
    """
    
    print(change_me)
    
    # current_max = 0 (what if there are only negatives?)
    if len(change_me) > 0:
        current_max = change_me[0]  # what if the list is empty?
        for x in change_me:
            # if we ever find something that is bigger than what we think the max is
            if x > current_max:
                # set the current max to that
                current_max = x
    else:
        current_max = 0
    
    print(f'The max of the list is {current_max}')

names_list = ['Eric', 'Robin', 'Sam', 'Cathy', 'Brian', 'Sam']
"""
    To remove a specific element <-- not index
        we are removing a name, a specific number from the list
    Make sure to use the in keyword to protect yourself from
        the ValueError
"""
print(names_list)
names_list.remove('Sam')
print(names_list)
if 'Sam' in names_list:
    names_list.remove('Sam')
else:
    print('That wasn\'t in the list')

if 'Sam' in names_list:
    names_list.remove('Sam')
else:
    print('That wasn\'t in the list')

print(names_list)

# if not(7 in [3, 1, 9, 2, 4]):
if 7 not in [3, 1, 9, 2, 4]:
    print('7 wasnt in that list')

"""
    Can you remove an element by index?
        yes
    You have to use the del keyword [delete]
"""
#               0  1  2  3  4  5  6  7  8  9  10
#              [5, 9, 5, 2, 8, 6, 7, 9, 1, 3, 4]
numbers_list = [5, 2, 9, 5, 2, 2, 8, 6, 7, 9, 1, 3, 4]
print(numbers_list)
index = int(input('Which index do you want to remove? '))
if 0 <= index < len(numbers_list):
    del numbers_list[index]
else:
    print('Nothing was removed. ')

print(numbers_list, len(numbers_list))

for i in range(len(numbers_list)):
    print(i)
    if i >= len(numbers_list):
        print('Out of range')
    elif numbers_list[i] == 2:
        del numbers_list[i]

print(numbers_list)

"""
    You can have lists inside of lists
    instead of using 1 bracket you need two brackets
"""

three_list = [['x', 'y', 'z'],  # index 0
              ['w', 'r', 's'],  # index 1
              ['t', 'e', 'v']]  # index 2

print(len(three_list))
print(three_list[1], three_list[0])
print(three_list[1][2], three_list[0][1])

