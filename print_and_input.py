"""
    Triple quotes is a comment, it won't execute
    
    Today we'll talk about print and input
    
    Talk about print first.
        print outputs to the console/command line/"screen"
        
        print is a built in function in python.
"""
# this is also a comment, but only a single line
if False:
    print(17, 3, 5, -100)  # integers
    print(3.14, 5.9823281732, -2.7182818459)  # floating point, float
    print('hello', 'robots', 'chicken')
    print('you can have spaces in strings like this')
    print("you can also use double quotes for strings like this")
    # if you start with a single quote end with a single quote
    # if you start with a double quote end with a double quote
    
    print('this is a double quote " see?')
    print("cat's")
    print(True, False)  # booleans
    """
        currently talked about:
            integers (int)
            floating point (float)
            strings (str)
            booleans (bool)
    """
    
    """
    Variables:
        A variable is a location in RAM that stores some data.
            also a variable has a name in the program, so we can
            access that memory location.
    """
    
    my_integer = 17
    my_string = "hello there"
    the_boolean = True
    the_float = 3.2
    
    """
    LHS is the variable name
    RHS is the thing you want to assign
    LHS <== RHS
    
    won't work
    21 = lucky
    """
    lucky = 21
    non_lucky = 13
    
    """
        Allowable variable names
        
            a variable can start with a letter or underscore
                not a number, or symbol @#$%^&*()
            a variable then is made of letters, numbers, underscores
    """
    Upper_Case_Variable = "upper"
    __hello = 2
    number7 = 7
    """
        In python, in general they have a preferred style
            snake case
                lower case letters (maybe numbers) and underscores
                spelled out words
    """
    # bad style in python
    __g_2_p = 5
    # snake case, better style
    general_purpose_2 = 5
    radius = 12
    welcome_string = "welcome to the program"
    #
    camelCaseIsThis = 12
    
    """
        input is a built in function that gets input from the
            command line or console
        input(prompt which is a string)
    """
    
    my_name = input('What is your name? ')  # put a space at the end of prompts
    # you can print out variables
    print(my_name, my_integer, the_float)
    
    """
        We can get text, but can we get numbers?
            We cast to an integer.
            
            use the int constructor "int"
    """
    x = int(input('Tell me your favorite integer: '))
    x_plus_2 = x + 2
    print(x + 2, x_plus_2)
    
    # don't want to do this exactly
    result = print(x + 2)
    print(result)
    
    y = float(input('What is your favorite floating point number? '))
    
    print(x, y)
    
    """
        You can do algebra with variables and literals
            what is a literal? a hard coded value
                3, 3.0, "happy"
    """
    mass = float(input('What is the mass? '))
    velocity = float(input('What is the velocity? '))
    # kinetic energy is 1/2 m v^2 <-- caret is wrong
    print('The kinetic energy is: ', (1/2) * mass * velocity ** 2)

    """
    d = sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2)
    """
    x2 = float(input('Tell me x2'))
    y2 = float(input('Tell me y2'))
    
    x1 = float(input('Tell me x1'))
    y1 = float(input('Tell me y1'))
    
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
    
    print('The distance is ', distance)

# don't divide by zero, it's just as illegal in programming print(5/0)

"""
    In python we have two different divisions
        / floating point division -> a float comes out
        // integer division -> an int comes out
        A lot of the time we'll be using integer division
"""
print(5/3, 5//3, 12//4, 14//4, 2//3)
print(20 / 5, 72 / 12, 72//12)

result = int(7/2)
print(result, int(3.999999))
"""
    Casting floating points truncates (kills off) the decimal
        it doesn't round
"""
print(int(-7/2), -7//2)

print(round(3.1415926, 2))
"""
    roundoff error - floating point numbers are not exact
"""



