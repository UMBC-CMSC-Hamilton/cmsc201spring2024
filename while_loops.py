"""
    if name equals main
    
    a python script runs from the top of the code down to the bottom
    
    in C++ for instance
        int main()
    in java for instance
        public static void main()
        there are "main" methods or functions which tells the program where to
            start
    there is no function main
        def main()
            this implies that python cares somehow about this main function
            python doesn't actually care about a function called main
            it's the same as all other function that we'll learn about
            next week. - not the entry point
            
        There's a secret variable called __name__
"""

import other_file


def run_chess():
    print('We are running chess')

if False:
    print(__name__)
    
    if __name__ == '__main__':
        # all of your starter code should go in here
        print('we are in the while loop file')
        # at the end you call your main game function
        run_chess()
    
    """
        While Loops
            a while loop is an if statement on repeat
        
        while [condition]:
            code in here which executes
            when the condition is true
            it only checks the condition once it reaches the top
            if it's false here, it still runs
            and keeps running until
            the end of the loop
            now it will recheck
    """
    
    num = int(input('Enter a number between 1 and 10: '))
    # input validation loop: idea is we trap the user while they're not
    # doing what we want
    while num < 1 or num > 10:  # not(1 <= num <= 10)
        print('That wasn\'t right try again.')
        num = int(input('Enter a number between 1 and 10: '))
    
    password = "the secret"
    user_password = input('Tell me the password: ')
    lockout = 3
    while user_password != password and lockout > 0:
        print(f'You have {lockout} attempts left.')
        user_password = input('Sorry that was not correct, Tell me the password: ')
        lockout -= 1
    
    if user_password == password:
        print('You got in.')
    else:
        print('You are a hacker, banned forever.  Or maybe you just forgot your roomba password.')
    
    """
        Let's explain why I teach for loops first.
        
            1) 98% of the loops you write are going to be for loops.
                (except input validation)
            2) For loops protect you against infinite loop conditions
    """
    
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1  # if you change this to += you get an infinite loop
        # you just have to imagine there are 20+ lines in here, the last
        # you type is the countdown line and just forget.
    
    number = 0
    # if number not less than 4, then the loop just won't even run
    # "skipped loop"
    while number < 4:  # in order to get out it just has to be >= 4
        print('hello there')
        number = int(input('The number: '))
    
    """
        Game loops
        
        usually the way games work is that there are two players
            some way to track turn
        
            
    """
    
    turn_count = 0
    game_over = False
    
    while not game_over:
        if turn_count % 2 == 0:
            if input('Did player 1 win?').lower() in ['y', 'yes']:
                game_over = True
        else:
            if input('Did player 2 win?').lower() in ['y', 'yes']:
                game_over = True
        # game_over = is_game_over()
        turn_count += 1
    
    """
        Anything you can do as a FOR loop you can do as a while loop
    """
    
    my_list = [4, 3, 6, 8, 9, 0, 14]
    
    index = 0
    while index < len(my_list):
        print(f"my_list at {index} is {my_list[index]}")
        index += 1  # because this isn't a for loop we have to increment the var ourselves
    
    print('Now we will do the same thing as a for loop.  ')
    for index in range(len(my_list)):
        print(f"my_list at {index} is {my_list[index]}")
    
    option_string = """1) play
    2) run
    3) load
    4) save
    5) download
    6) exit"""
    
    PLAY = 1
    RUN = 2
    LOAD = 3
    SAVE = 4
    DOWNLOAD = 5
    EXIT = 6
    
    print(option_string)
    option = int(input('Choose an option: '))
    while option != EXIT:
        print(option_string)
        option = int(input('Choose an option: '))
        if option < 1 or option > EXIT:
            print('That was a bad option')
        else:
            print(f'Doing option {option}')


total = 0
how_big = int(input('How big do we want to get? '))
count = 1
while total < how_big:
    print(count, total)
    total += count
    count *= 2
    
print(count, total)

total = 0
count = 0
while total < how_big:
    # we just don't know how many times it's going to have to loop
    total += 3 * count ** 2 + count + 1
    print(count, total)
    count += 1

print(count, total)

the_num = int(input('What number do you want to divide? '))
times = 0
while the_num > 1:
    the_num //= 2
    times += 1
    print(the_num, times)


print(the_num, times)
