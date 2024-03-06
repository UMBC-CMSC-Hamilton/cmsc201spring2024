"""
    Exam:
        Next Thursday Mar 7
    Functions
        Declaring functions
        need the def keyword, you need the function name, any parameters
        
        types in the parameters are not fixed, so be careful
            function now requires that you pass two "arguments"
        scope
            a variable created inside of a function is considered "local"
            a local variable lives as long as the function does
            once the function ends, that variable is "lost", destroyed
            
            not local = global
            a global variable lives for the length of the program
            
            you can access a global variable from the local scope
        
        pass by value
            a variable is passed by value when it is a basic data type
            (immutable)
            bool, int, string, float, None
            
            pass by value makes a local copy of the variable
        pass by reference
            a pass by reference means that we are modifying the same exact
                underlying memory/variable
            mutable things are passed by reference
            lists, classes, dictionaries
"""


#                  parameters
def my_function(my_int, my_list):
    for i in range(my_int):
        my_list.append(int(input('Tell me an int: ')))


the_list = [1, 2, 3]
#           arguments
# my_function(4, the_list)

print(the_list)


def is_even(x):
    my_variable = 17
    if x % 2 == 0:
        my_variable += 1
        return True
    else:
        my_variable -= 1
        return False


print(is_even(4))


# print(my_variable)


def modify_count(my_count):
    my_count = 5
    print('Inside the function', my_count)


count = 7  # because count is an int, gets passed by value not reference
modify_count(count)
print(count)

robots = 16


def modify_robots():
    # i banned this, for good reason
    global robots
    robots += 5


modify_robots()
print(robots)

SPACE = ' '
TTT_X = 'x'
TTT_O = 'o'


def display_board(board):
    for i in range(len(board)):
        print(' | '.join(board[i]))
        if i == 0 or i == 1:  # i < len(board) - 1
            print('-' * 9)


def pick_location(the_board):
    choose_location = input('Enter a location in row col notation')
    location = choose_location.split()
    location[0] = int(location[0])
    location[1] = int(location[1])
    while location[0] not in [0, 1, 2] or location[1] not in [0, 1, 2] or \
            the_board[location[0]][location[1]] != SPACE:
        choose_location = input('Enter a location in row col notation')
        location = choose_location.split()
        location[0] = int(location[0])
        location[1] = int(location[1])
    return location


def check_rows(the_board):
    for i in range(len(the_board)):
        complete_row = the_board[i][0]
        for j in range(len(the_board[i])):
            if the_board[i][j] != complete_row:
                complete_row = SPACE
        if complete_row != SPACE:
            return complete_row
    
    return SPACE


def check_cols(the_board):
    for i in range(len(the_board[0])):
        complete_col = the_board[0][i]
        for j in range(len(the_board)):
            if the_board[j][i] != complete_col:
                complete_col = SPACE
        if complete_col != SPACE:
            return complete_col
    
    return SPACE


def check_diagonals(the_board):
    """
        (0, 0) (0, 1) (0, 2)
        (1, 0) (1, 1) (1, 2)
        (2, 0) (2, 1) (2, 2)
    """
    diagonal = the_board[0][0]
    for i in range(len(the_board)):
        if diagonal != the_board[i][i]:
            diagonal = SPACE
    
    if diagonal != SPACE:
        return diagonal
    anti_diagonal = the_board[2][0]
    for i in range(len(the_board)):
        if anti_diagonal != the_board[i][2 - i]:
            anti_diagonal = SPACE
    
    return anti_diagonal

def game_over(the_board):
    row_win = check_rows(the_board)
    col_win = check_cols(the_board)
    diag_win = check_diagonals(the_board)
    # print(row_win, col_win, diag_win, sep = ":")
    if row_win != SPACE:
        return row_win
    if col_win != SPACE:
        return col_win
    return diag_win


def filled_board(the_board):
    for i in range(len(the_board)):
        for j in range(len(the_board[i])):
            if the_board[i][j] == SPACE:
                return False
    return True


def tic_tac_toe_game():
    the_board = [
        [SPACE, SPACE, SPACE],
        [SPACE, SPACE, SPACE],
        [SPACE, SPACE, SPACE],
    ]
    turn = 0
    
    while game_over(the_board) == SPACE and not filled_board(the_board):
        display_board(the_board)
        location = pick_location(the_board)
        if turn % 2 == 0:
            the_board[location[0]][location[1]] = TTT_X
        else:
            the_board[location[0]][location[1]] = TTT_O
        
        turn += 1
    
    display_board(the_board)
    if game_over(the_board) != SPACE:
        print("The Winner Was", game_over(the_board))
    else:
        print('You tied, filled the board.')
    

if __name__ == '__main__':
    tic_tac_toe_game()
