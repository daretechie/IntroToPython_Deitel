# TODO: 17 (Nested Loops) Write a script that displays the following triangle patterns separately, one below the
#  other. Separate each pattern from the next by one blank line. Use for loops to generate the patterns. Display all
#  asterisks (*) with a single statement of the form print('*', end='') which causes the asterisks to display side by
#  side. [Hint: For the last two patterns, begin each line with zero or more space characters.]
#  (a)     (b)    (c)     (d)
#  * ********** ********** *
#  ** ********* ********* **
#  *** ******** ******** ***
#  **** ******* ******* ****
#  ***** ****** ****** *****
#  ****** ***** ***** ******
#  ******* **** **** *******
#  ******** *** *** ********
#  ********* ** ** *********
#  ********** * * **********

print("(a)")

for row in range(1, 11):
    for _ in range(row):
        print("*", end='')
    print()

print("(b)")

for row in range(10, 0, -1):
    for _ in range(row):
        print("*", end='')
    print()

print("(c)")
for row in range(10, 0, -1):
    for _ in range(10 - row):
        print(end=" ")
    for _ in range(row):
        print("*", end='')
    print()

print("(d)")
for row in range(1, 11):
    for _ in range(1, 11 - row):
        print(end=" ")
    for _ in range(row):
        print(f"*", end='')
    print()
