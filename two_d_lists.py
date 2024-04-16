"""
    Already seen them, not new
    
    But what is a 2d list?
        a list with lists inside it
"""

weird_lists = [[1, 2, 3], [1, 2, 3, 4, 5, 6], [], [2, 3, 4, 5]]
"""
    We always have to check with a list like this whether the index is allowed.
    
"""

i, j = list(map(int, input("enter two ints ").split()))
# boilerplate legalism that you need
if 0 <= i < len(weird_lists) and 0 <= j < len(weird_lists[i]):
    print(weird_lists[i][j])
else:
    print('That was out of the range')


# how do you create through a 2d grid?
the_grid = []
ROWS = 3 # 2d lists are indexed by "rows" and then "columns"
COLS = 5

# version 1
for i in range(ROWS):
    new_row = []
    for j in range(COLS):
        new_row.append(f'({i + 1}, {j + 1})')
    the_grid.append(new_row)
for row in the_grid:
    print(row)


# version 2

the_grid = []
new_row = []

for j in range(COLS):
    new_row.append('*')

for i in range(ROWS):
    # have to remember the list keyword otherwise it doesn't make a copy
    # it makes a reference and then all the rows are the same list
    the_grid.append(list(new_row))


the_grid[2][1] = 'a'
for row in the_grid:
    print(row)


for i in range(ROWS):
    for j in range(COLS):
        if j != COLS - 1:
            print(the_grid[i][j], end=' | ')
        else:
            # end == '\n' if we don't specify
            print(the_grid[i][j])
    if i < ROWS - 1:
        print("-" * 18)


"""
    if the user enters coordinates then always check if they're valid
"""

in_string = input('Enter row and col separated by a space: ')
str_values = in_string.split()
if len(str_values) == 2:
    print('Good')
    row = int(str_values[0]) - 1
    col = int(str_values[1]) - 1
    # once you do all this input validation, now we have to check if it's
    #       in bounds
    if 0 <= row < ROWS and 0 <= col < COLS:
        print('That is in bounds')
        # do the rest of the stuff that you care about
        print(the_grid[row][col])
    else:
        print('The row and col were invalid in some way')
else:
    print('Bad')
    
students = {'ab12345': {'Name': 'Eric H',
                        'Grades': [1, 2, 3, 4, 5],
                        'email': 'eric8',
                        'random': 8743
                        },
            'cd23232': {'Name': 'Alice',
                        'Grades': [3, 4,5, 5, 6],
                        'email': 'alice2',
                        'random': 3848743
                        },
            }

student_id = input('Enter a student id: ')
if student_id in students:
    print(students[student_id]['Grades'])