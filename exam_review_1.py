"""
Write an expression that is True if and only if chance rain is greater
than 0.01 and umbrella is True and rain coat is also True.
"""
# dont need these on the exam
chance_rain = 0.05
umbrella = False
rain_coat = True
# i only wrote these to prevent an error from happening
# this is the actual answer:
chance_rain > 0.01 and umbrella and rain_coat
# alternatively:
chance_rain > 0.01 and umbrella == True and rain_coat == True
# don't need an if statement

"""
Write an expression that is True if and only if either x is
greater than 20 or y is greater than 12 but not both.
"""
x = 15
y = 21
# here is the actual answer
(x > 20 and y <= 12) or (x <= 20 and y > 12)
# also fine
(x > 20 or y > 12) and not (x > 20 and y > 12)

"""
18. What kind of loop can result in an infinite loop?
Give an example consisting of 5 or less lines
of code demonstrating an infinite loop.

A while loop.

while True:
    pass
    
x = 1
while x > 0:
    x += 1

x = 0
while True or not False:
    x += 1

19. Explain what happens when we replace an elif with an
 if statement instead. For instance consider the code below:
num = int(input(’>>’))
if num > 10:
    print(’num is larger than 10’)
elif num > 20:
    print(’num is larger than 20’)
    

Ans: Currently if you pick a number like num= 25 then only
    the first statement will print.
    
    Conversely, if you change the elif to an if,
    then both statements will print.

20)
    start stop step
    start stop
    stop <-- don't get too poetic
    
21) True
22) True
23) False


"""

doubles = 1
while doubles < 50:
    print(doubles)
    doubles *= 2
    
"""
1
2
4
8
16
32
-- done
"""

doubles = 1
while doubles < 50:
    doubles *= 2
    print(doubles)

"""
2
4
8
16
32
64
"""

for i in range(5, 27, 3):
    print(i, end=" ")

"""
instead: 5 8 11 14 17 20 23 26
here's what it actually was:
5
8
11
14
17
20
23
26
"""

s = "hello"
n = 15
if n == 20 and s == "hello":
    print("Both are true.")
elif n == 15:
    print("15 is equal to 3 times 5")
elif s == "hello":
    print("Well Hello There")
else:
    print("Obi Wan Kenobi , You’re my only hope")

"""
15 is equal to 3 times 5
"""

"""
7   |   add a colon or rewrite the line with the colon (longer and more work)
8   |   for j in range(len(has_list)):
11  | if need_counts[i] > has_counts[j]:  flip inequality
14  | print(’We have enough’, needs[i]) or has_list[j]
17  | for x in needs_counts: to for x in has_counts:
18  | total += x
"""

def get_two_max_values(L):
    # get rid of any bad list to prevent index errors
    if not L:
        return [-1, -1]
    elif len(L) == 1:
        return [L[0], -1]
    
    if L[0] > L[1]:
        first_max = L[0]
        second_max = L[1]
    else:
        first_max = L[1]
        second_max = L[0]

    for x in L:
        if x > first_max:
            second_max = first_max
            first_max = x
    
    return [first_max, second_max]

    
    
def distance_three_match(s, c):
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] == c:
            return True
    
    return False

[1, 2, 3,4 ] in [[1,2, 3, 4], 6, 7, 8]