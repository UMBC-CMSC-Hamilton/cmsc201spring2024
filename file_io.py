"""
File IO - what if you want to read or write from a file?
    inputting from files gives a way to get a lot of data into the
        program without having to do it manually, through text input
        more accurate than typing it, better than copy-paste
    outputting to files gives a way to remember data we calculated
        during the program run.

    How do you do this in python?
"""

# open is a built-in function
reader = open("first_file.txt")
# what does this thing return?
# it doesn't return the text in the file, it returns a "file object"

# this doesn't really help us too much
print(reader)

"""
    file.read()
        read all of the contents of the file
        this one is just a little dangerous
        it will read a 4GB file and give it to you as a string
        this will probably crash your program.
        nothing in this class will get anywhere close to that
    file.readlines()
        nice thing this does for you is that it splits on newlines
        but it doesn't take them out...
        
    file.readline()
        read in a single line.
"""

result = reader.read()
print(result)
print(result.split('\n'))
# be slightly careful of extra newlines or whitespace at the end of a file

# what happened?
print(reader.readlines())
# cursor is at the end of the file
# frees the file up, tells the OS that next time we want to start at the
#       beginning again
reader.close()
# make sure you close your files, in read mode it's less important
# read mode doesn't lock them, but it's 'good practice'

new_reader = open('first_file.txt')
the_lines = new_reader.readlines()
print(the_lines)

for x in the_lines:
    # why are there tons of extra newlines?
    # how does print work? how does readlines() work?
    # print inserts a newline, readlines() doesn't remove the newlines from the data
    print(x, end='')  # this turns off the print newline
    print(x.strip())  # this removes the newline from the string itself
    
new_reader.close()
# notice that the .readlines() doesn't remove the \n characters

print('\n\nSingle line read now: ')
single_line = open('first_file.txt', 'r')

the_line = single_line.readline()
while the_line:  # as long as the line itself is not empty [\n is not empty]
    if not the_line.strip():
        print('Empty line')
        # just going to ignore this do nothing
    else:
        print(the_line, end="")
    the_line = single_line.readline()
    
# secretly this is just readline()
the_file = open('second_file.txt', 'r')
for the_line in the_file:
    print(the_line, end='')
    if the_line.strip():
        split_line = the_line.split(',')
        print('name: ', split_line[0], 'number: ', split_line[1])


"""
    Let's get to the write mode
"""
if input('Do you want to overwrite movies? ').lower() == 'yes':
    movie_file = open('movies.txt', 'w')
    """
        When you open a file in write mode, it erases the entire file
            If you care about that file, or anything in it, don't open it
            in write mode.
    """
    movie = input('Tell me movie: ')
    while movie != 'quit':
        # remember to add the newline otherwise it won't be there
        movie_file.write(movie + "\n")
        movie = input('Tell me movie: ')
    
    movie_file.close()

# file.writelines(list of strings)

new_file = open('things', 'w')
thing = input('Tell me thing: ')
list_of_things = []
while thing != 'quit':
    # remember to add the newline otherwise it won't be there
    list_of_things.append(thing + '\n')
    thing = input('Tell me thing: ')

new_file.writelines(list_of_things)
new_file.close()


"""
    The last mode of file IO
        append mode, like write mode but different
            it opens the file in write mode BUT doesn't erase
        
"""

# shorthand for movie_file = open('movies.txt', 'a')
# but it has one advantage, it closes the file automatically.
# can't use it when you want the file to stay open all the time

with open('movies.txt', 'a') as movie_file:
    movie = input('Tell me movie: ')
    while movie != 'quit':
        # remember to add the newline otherwise it won't be there
        movie_file.write(movie + "\n")
        movie = input('Tell me movie: ')

"""
    byte mode exists you won't need it yet (if you do in the future)
    'rb', 'wb', 'ab'
"""