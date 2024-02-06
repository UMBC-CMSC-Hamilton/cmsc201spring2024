"""
    conditionals are statements that allow the program to
        branch / make decisions

    Use if statements
    the condition evaluates to True or False
    The colon is "syntactic"
    Word syntax - structural rules of a language (form not meaning)
    if [a condition / an expression] :
        [the next line of code must be tabbed]
        [more code must also be tabbed]
        
"""
if False:
    x = int(input('Tell me an int: '))
    if x > 0:
        print(f'{x} is positive')

print('Does this code run? yes because it isn\'t in the if block')

"""
    Escape Sequences
    
    You have to know these:
    \n = newline
    \r = carriage return
    \t = tab
    \' = apostrophe or single quote or tick mark
    \" = double quote
    \\ = a single backslash
    
    Mostly not used anymore, and there's more of them
    \v = vertical tab, not really used anymore
    \a = computer beep
"""

print('hi\nbye')
print('a\tb\thello\tc\twhatever')
print('\\\\\\neighbor')

# what happens is that hello gets typed, we go back to the start
# of the line and then something gets typed, makes hello vanish
print('hello\rsomething')
# every newline in windows is actually \r\n

"""
    Getting back to if statements
"""
if False:
    the_word = input('Tell me a word: ')
    if the_word == 'chicken':
        print('The word is apparently chicken. 1')
    
    if the_word.lower() == 'chicken':
        print('The word is apparently chicken. 2')

# str.upper()

# ASCII is case sensitive
# A = 65, a = 97

"""
    3 logical quantifiers in python
    and and or are "binary operators"
    and
        A and B = True if both A and B are true
        
        B \ A True  False
        True  True  False
        False False False
    
    or
        A or B = A is True or B is True or (both)
            we mean inclusive or here. allows for both to be true
        
        B \ A True  False
        True  True  True
        False True  False
    not is a "unary operator"
    not
    
        A   True    False
     not A  False   True
     
    
"""

x = int(input('Tell me x: '))
y = int(input('Tell me y: '))

# if the first statement is false, it doesn't need to check
# the second
if x > 5 and y > 2:
    print('The numbers are big enough')
else:
    print('Something wasn\'t the right size')


if x > 5 or y > 2:
    print('Some of the numbers are big enough')
else:
    print('Neither were the right size')
    
# short circuiting = if the first statement of an or is true
# it won't execute the second.

if not(x > 15):  # x is less than or equal to 15
    print('when exactly does this print?')


"""
    Equals versus not equal
    
    x = y what this means is "I want to take the value of y
            and put it into the variable x"
    x == y "are x and y equal?" comparison operator
    x != y "are x and y not equal to each other?" not-equals operator
    
    not(x == y) is the same as x != y
    not(x == y) is probably very rare
"""

if x == y:
    print('They are equal.')
else:
    print('They are not equal.')

password = 'password1'  # the most secure password
user_pw = input('What is your password? ')
if password == user_pw:
    print('You have logged in')
else:
    print('Access Denied')


"""
    Now let's talk about else if
 
    the first condition is always "if"
    but what if that is false?
    we can add more conditions as we go
    we must use the term "elif" in python
    elif is a contraction of 'else if'
"""

user_option = int(input('Tell me a number beteen 1 and 5:'))

if user_option == 1:
    print('You want to start a new game')
elif user_option == 2:
    print('You want to save the game')
elif user_option == 3:
    print('You want to load a game')
elif user_option == 4:
    print('You want to change settings')
elif user_option == 5:
    print('You want to quit')
else:
    print('You didn\'t pick an option on the menu.')


x = int(input('Tell me a number: '))

if x == 2:
    print('x is smallest prime, also even, also 2.')
elif x == 17:
    print('x is a mersenne prime or something')
elif x > 0:
    print('x is positive')