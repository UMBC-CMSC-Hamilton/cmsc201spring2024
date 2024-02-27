"""
    Strings, strip, split, join, slices

    A string is a "list of characters" - in python it is slightly different
    strings are actually immutable

"""
# how do we replace a character, or add in a substring

a_string = "hi_i_am_a_string"
print(a_string[7], a_string[12])
# can't do this because of immutability
# a_string[7] = 'p'

print(list(a_string))
my_string_list = list(a_string)
my_string_list[7] = 'proper'
print(my_string_list)

"""
    join method is part of the string class
    
        separator.join(list of strings) make a string separated by the separator
        separator must be a string
"""

print(''.join(my_string_list))

path = ['afs', 'umbc.edu', 'e', 'r', 'eric8', 'pub', 'cmsc201']

linux_slash = '/'
win_slash = '\\'
print(linux_slash.join(path))
print(win_slash.join(path))

print('hello'.join(['a', 'b', 'c', 'd']))

print(' : '.join(['a', 'b', 'c', 'd']))

print(', '.join(['summit', 'urban', 'theocracy', 'drumstick']))

happy = 'happy'
happy += 'ness'
# this happy is a new memory location from the last one more line up
print(happy)

"""
    split
"""

ip_address = '134.27.83.155'
ip_parts = ip_address.split('.')
print(ip_parts)
# can't do this: ip_parts = int(ip_parts)
for i in range(len(ip_parts)):
    ip_parts[i] = int(ip_parts[i])

print(ip_parts)

phone_number = '443-295-0123'
phone_number_parts = phone_number.split('-')
print(phone_number.split('-'))
for j in range(len(phone_number_parts)):
    phone_number_parts[j] = int(phone_number_parts[j])

print(phone_number_parts)

the_sentence = "A quick brown fox jumped over the lazy dog."
print(the_sentence.split())

# are you going to use this all the time? no probably not
this_other = 'Robots\rattack\t\tand\ndestroy\nthe world.'
print(this_other.split())

row_in_csv = '3,2,5,7,hello,turnip'
print(row_in_csv.split(','))
row_in_csv_with_tabs = "hi\tbye\tsomething else\t3"
print(row_in_csv_with_tabs.split('\t'))

"""
    strip function - a bit simpler than split
        removes whitespace from both sides of the string
"""

the_command = input('Enter a command: ').strip().lower()
# the_command = the_command.strip()
if the_command == 'start':
    print('we are starting up')
elif the_command == 'stop':
    print('STOP!!!')

# even though there's an "a" in blah, the bl and the h protects it.
print('aaaaaaaaaaaablahaaaaaaaaaaa'.strip("a"))
print("    here are a\tbunch of words        \t\t\t\n".strip())

"""
    Slices

        What are slices?
            a pythonic specific thing which allows us to take a substring
                or a sublist in order
"""
my_fav_string = "rambunctious"
# takes a substring starting at index three and going up to BUT NOT INCLUDING
#  index 8
print(my_fav_string[3:8])

"""
    We are told to look for the substring "fun" but we're not allowed to use
        find.
"""
fun_found = False
the_word = input('Tell me a word that maybe has fun in it: ')
for i in range(len(the_word)):
    if "fun" == the_word[i: i + 3]:
        fun_found = True

print('Was fun found? ', fun_found)

# why don't we have an index error?

# for some reason python has decided to be nice here no index error
print(the_word[5:2000])
print('here it is: ', the_word[1800: 5000])

# there are also list slices:

my_list = ['a', 't', 'q', 'z', 'r', 'm', 'l', 't']
print(my_list[2:5])

# no comma print(my_list[2, 5])

# if you ever need it there's a step size in the slice
print("random_string"[0: 100: 2])
# the step argument can be negative [be advised, careful]

"""
    Nice slice things
    
        if you don't enter a first argument, then it auto-sets to 0
        if you don't enter a second argument it sets to the len(the string)
"""
nonsense = "this is a long string with many words in it but generally meaningless"
print(nonsense[:18])

print(nonsense[5:len(nonsense)])
print(nonsense[5:])

# a slice that starts at 0 and goes to the length
print(nonsense[:])

# deep copy = a real copy
my_super_list = [12, 7, 3, 5, 6, 19, 8, 5, 4, 3]
my_copy = list(my_super_list)
print(my_copy)
slice_copy = my_super_list[:]
slice_copy[3] = 0
print(slice_copy)
print(my_super_list)

# it makes a "reference" (shallow copy = not a copy)
not_copy = my_super_list
not_copy[2] = 170
print(not_copy)
print(my_super_list)