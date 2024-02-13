"""
    Conditionals are a way to branch in code.
        The idea is that based on user input, some state,
        some event that happens changes the way the code executes.
    
    Control Flow:
        Sequential Flow - One line executes and then the next
            line executes. [Don't have any choices]
        Conditional Flow - We execute code based on a statement
            whether a certain expression is true or false
        Iterative - loops haven't talked about yet
        Functional - also haven't discussed yet
"""

the_int = int(input('Tell me an integer: '))

# you can do chained inequalities like in "regular math"
if 1 <= the_int <= 10:
    print('The number is in range')
else:
    print('The number was not in range.')
"""
This code is identical, if you do this, no points lost or anything.
if 1 <= the_int and the_int <= 10:
    print('The number is in range')
else:
    print('The number was not in range.')
"""

"""
    if statement
    elif statement
    elif statement
    elif statement
    else
    
    if starts the expression, without it you can't have any
        elifs or elses
    How many elif statements can we have in an if-block?
        as many as you want (until you crash python)
        infinity (not quite)
    How many elif statements will execute in a given if-block?
        As soon as it finds an elif that's true, that one executes
        none of the rest do.
        
        "at most one will execute"
    Does an if-block need an else?
        no, even if there's elifs
"""
spongebob = False
if spongebob:
    emotion = input('Tell me an emotion: ')
    value = int(input('Tell me a value: '))
    
    # usually you go from the most specific cases
    #             to less specific cases
    
    if emotion == 'happy' and value > 7:
        print('you are very happy')
    elif emotion == 'happy' or value > 7:
        print('You are either happy or feel strongly about it.')
    else:
        print("Sorry about that, whatever it is")
    
    """
        Nesting, you can put if statements inside of if statements
    """
    
    krusty = input('Do you work at the Krusty Krab? ')
    if krusty.lower() == 'yes' or krusty.lower() == 'y':
        owner = input('Do you own the joint? ')
        if owner.lower() == 'yes' or owner.lower() == 'y':
            print('You are Mr. Krabs')
        else:
            hate_job = input('Do you hate your job? ')
            if hate_job.lower() == 'yes' or hate_job.lower() == 'y':
                print('You are Squidward')
            else:
                print('You are Spongebob')
    else:
        # plankton is in, sandy, patrick
        evil = input('Are you evil? ')
        if evil.lower() == 'yes' or evil.lower() == 'y':
            print('You are honest plankton.')
        else:
            love_gas = input('Does your oxygen have to come in a gas state? ')
            if love_gas.lower() == 'yes' or love_gas.lower() == 'y':
                print('You are Sandy.')
            else:
                print('You are Patrick.')

"""
    Modulus division (mod)
        
        modulus division is the remainder of an integer division
        
        5 // 3 = 1
        5 % 3 = 2 "five mod three is 2"
        
        17 % 4 = 1
        16 % 7 = 2
        13 % 5 = 3
        
        n = q * d + r
        
        n = original number
        q = quotient
        d = divisor
        r = remainder
        
        0 <= remainder < divisor
        
        -7 // 2 =
        -7 = -4(2) + 1
        -7 % 2 = +1 not -1
"""

print(5 % 3, 17 % 5, 13 % 5, 19 % 7)
print(-7 % 2, -7 // 2)  # +1 = rem, -4 = quotient

"""
    if you mod a number by 2:
        and it's zero:
            it's even
        and if it's one:
            it's odd
            
    is 0 even, odd, or neither?
        0 is even
        0 // 2 = 0 also even.

    turn counts use this a lot, very useful for that kind of thing
"""

"""
    +=
    -=
    *=
    **=
    
    What are all of these operators?
        programmer laziness
"""

count = 5
how_many_to_add = int(input('How many should we add to count? '))
# count = count + how_many_to_add
# just short-hand for the line above
count += how_many_to_add

# for those who know a 0 <= Java, there's no ++ or -- operator
a_value = 3
a_value += 1
#
b_value = 7
b_value -= 1

a_value += 2 * b_value - how_many_to_add

pow_value = 7
pow_value **= 3
# pow_value = pow_value ** 3

print(16 // 2 * (2 + 2))
stuff = 10
radius = 3.77
the_power = 5
# HW1 stuff
print(stuff / (radius * 10 ** the_power))


"""
    https://winscp.net/eng/index.php
    
    Host Name:
        gl.umbc.edu
    username:
        your username that works on GL
        
    once logged in, you open the pycharm folder on your machine
        by right clicking and select open in-> Explorer
                                for mac     -> Finder
    Drag and drop.
"""

