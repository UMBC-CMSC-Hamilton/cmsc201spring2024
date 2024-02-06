"""
    print formatting has a lot of options in python
        we don't care which one you use.
"""

x = 14
# the f tells python that the string is a "format string"
print(f'The value of x = {x}')
print('The value of x =', x)
print('The value of x = %d' % x)  # C-style print formatting
print('The value of x = {}'.format(x))
# example of string concatenation
print('The value of x = ' + str(x))

name = 'Eric'
food = 'Sushi'
time = 1137

print(f'My name is {name}, I like {food}, the time is {time}')

# string concatenation is when you can put strings together
# no spaces will be put between them
# the idea is addition for strings
a_string = 'Hello I am a string'
b_string = 'string cheese'

print(a_string + ' ' + b_string)
