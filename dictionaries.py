"""
    In other languages, dictionaries are usually called Hashes
    Hash, HashMap, HashTable

    A dictionary is a collection of elements instead of giving them
        indices from 0 ... len(list) - 1
        we give them "keys" instead
    You store data and access data using the key.
        Use the array brackets to access and store data.
        keys have to be immutable = int, bool, string, float[probably not]
"""

# declare a dictionary
new_dictionary = {}
other_new_thing = dict()
#          key     : value  key : val, key  : val, key : val
animals = {'rabbit': 5, 'gerbil': 7, 'horse': 16, 'lion': 19, 'turtle': 7}
print(animals['rabbit'], animals['horse'])
#  if you try to look up a value, you get a KeyError
# print(animals[7])
#  looking up a key that doesn't exist will also give a KeyError
# print(animals['penguin'])
# KeyErrors are like IndexErrors for dictionaries.

# in keyword ONLY checks keys
if 'penguin' in animals:
    print(animals['penguin'])
else:
    print('That isn\'t in the dictionary.')

order_list = ['burger', 'burger', 'fries', 'pie']
total = 0
fast_food = {'burger': 5, 'fries': 2.5, 'drink': 3}
# fast_food.get(thing) if it's not in the dictionary it returns None
for thing in order_list:
    total += fast_food.get(thing, 4)
print('The total order is', total)

"""
    What if you have student IDs?
"""

student_map = {'eric8': ['professor', 3], 'someone2': ['student', 7]}

print(student_map['eric8'])
print(student_map['someone2'])
student_map['someone2'].append('cmsc201')
print(student_map['someone2'])

# insert into a dictionary by accessing and assigning the key the first time
student_map['mary17'] = ['student', 27]
print(student_map)
student_map['fallon4'] = ['grad student', 1]
print(student_map)

del student_map['mary17']
print(student_map)

# avoid this but it exists (be careful that you have a key specified)
# del student_map
# print(student_map)

# print(globals())
"""
    Created dictionaries,
    added elements
        my_dict[new_element] = new_thing
    remove elements
        del my_dictionary[kill_element]
    test if elements are in the dictionary
        either use the in keyword
        dict.get(key, default value)
"""

nest = {1: {'happy': 3, 'sad': 7}, 2: {'robot': 14, 'chicken': 5},
        8: {'python': 2, 'future': 17}}

print(nest[1], nest[2], nest[8])
print(nest[2]['robot'])

list_in_dict = {'England': [1, 5, 8, 9], 'Turkey': [2, 4, 6, 8],
                'Argentina': [9, 6, 5, 4]}

print(list_in_dict['Turkey'][2])

"""
    What are the keys in a dictionary?
    
    How do we scan through it?
"""
my_dict = {'hi': 13, 'sam': 17, 'nor': 3, 'nand': 4, 'not': 5, 'xor': 31}

for key in my_dict:  # for -i loop for dictionaries
    print(key, my_dict[key])
    my_dict[key] += 5

print(my_dict)

grades = {'Exam 1': 92, 'Exam 2': 85, 'Project 1': 75, 'Project 2': 99, 'Project 3': 82}
total = 0
for assign in grades:  # for i loop (analogy)
    total += grades[assign]
print('The average is', total / len(grades))

total = 0
num_projects = 0
for assign in grades:  # for i loop (analogy)
    if 'Project' in assign:
        total += grades[assign]
        num_projects += 1
if num_projects > 0:
    print('The average is', total / num_projects)
else:
    print('There were no projects.')

print(grades.keys())
gk = grades.keys()

# that is a dict_keys object, what is that? dunno
list_of_gk = list(grades.keys())
list_of_gk.append('hi')
print(list_of_gk)
print(grades)
grades['Homework 1'] = 50
print(grades)

"""
    Dictionaries are mutable so they pass by reference
    
"""


def modify_keys(my_dict):
    remove_keys = []
    for key in my_dict:
        if 'a' in key:
            remove_keys.append(key)
    
    # why does this work? remove_keys is a list, NOT my_dict
    for remkey in remove_keys:
        del my_dict[remkey]


the_dict = {'a1': 3, 'b2': 5, 'a4': 7, 'a9': 2, 'c3': 6}

# What if we don't want to destroy the dictionary?
# make a copy explicitly
copy_dict = dict(the_dict)

modify_keys(the_dict)
# all the keys with a are removed.
# this tells us that dictionaries are mutable = pass them by reference
# don't pass a copy, you pass a renamed version of the same object
print(the_dict)
print(copy_dict)

horror_example = {'a': [1, 2, 3], 'b': [2, 4, 6], 'c': [3, 7, 9]}
copy_horror = dict(horror_example)  # only copies one level deep

true_copy = {}
for key in horror_example:
    true_copy[key] = list(horror_example[key])

copy_horror['a'][1] = 7
print(horror_example)
print(true_copy)
